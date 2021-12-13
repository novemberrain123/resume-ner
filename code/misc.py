import os
import re
import sys
import fitz
from ner_spacy_pred import spacy_predict

#parses search query and returns list of file indexes
def search(q, ner):
    query = q.lower()
    directory = "static/" + ner
    special = 0
    matches = list() #tuple(doc_number, entity_text, line)
    for filename in os.listdir(directory):
        num = filename[-8:-4]
        tokens = []
        selected = False
        with open(os.path.join(directory, filename)) as f:
            for idx,line in enumerate(f):
                #return entites alone
                if ner == "spacy": 
                    s = re.findall('- (.+)$', line)[0]
                else:
                    s = re.findall('"(.+)"', line)[0]
                s_lower = s.lower()
                s_new = [i for i in s_lower.split(" ")]
                if query in (s_new or s_lower):
                    f2 = open(os.path.join(directory,filename))
                    full = list()
                    for line in f2:
                        line = line.replace('"','')
                        line = line.replace('\n','')
                        full.append(line)
                    matches.append((num, full, idx))
                    f2.close()
                    break

    if matches == []:
        matches = special_search(query, ner)
        special = 1
    print(f"{len(matches)} matches returned with {ner} NER")
    print(matches)
    return matches, special

#if normal search doesnt yield docs
def special_search(q, ner):
    matches = list()
    if ner == "spacy":
        test_doc, s = spacy_predict(q)
        if s == "":
            return matches
        tag = re.findall(r'^\S*', s)[0]
    else:
        s = flair_predict(q)
        if s == "":
            return matches
        tag = re.findall(r'Labels: (.{3})', s)[0]

    print(tag)
    directory = "static/" + ner
    for filename in os.listdir(directory):
        num = filename[-8:-4]
        tokens = []
        selected = False
        with open(os.path.join(directory, filename)) as f:
            for idx,line in enumerate(f):
                if tag in line:
                    print("yes")
                    f2 = open(os.path.join(directory,filename))
                    full = list()
                    for line in f2:
                        line = line.replace('"','')
                        line = line.replace('\n','')
                        full.append(line)
                    matches.append((num, full, idx))
                    f2.close()
                    break
    return matches

#Does NER
def scan_spacy():
    directory = "static/"
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            num = filename[-8:-4]
            text = read_pdf(os.path.join(directory, filename))
            f = open(directory + "raw_" + num + ".txt", "w")
            f.write(text)
            f.close()
            test_doc, s = spacy_predict(text) 
            f = open(directory + "spacy/" + "ner_" + num + ".txt", "w")
            f.write(s)
            f.close()
                

#Does rough OCR
def read_pdf(filepath):
    pdf_file = filepath
    input_doc = fitz.open(pdf_file)
    text = ""
    for page in input_doc:
        text = text + str(page.getText() )
    text = " ".join(text.split('\n'))
    text = text.lower()
    return text
