import spacy

nlp_model = spacy.load('nlp_model')

def spacy_predict(text):
    test_doc = nlp_model(text.lower()) 
    s = ""
    for ent in test_doc.ents:
        s += f'{ent.label_.upper():{30}}- {ent.text}' + '\n'
    return test_doc, s

