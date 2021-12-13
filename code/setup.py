import os
from misc import scan_spacy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", action="store_true")
#sets up static files for HTML and does NER on documents
p = os.popen('./pdffirst.sh')
print(p.read())
print("Done duping, beginning spacy scan")
scan_spacy()
args = parser.parse_args()

if args.f:
    from scan_flair import scan_flair
    print("Done spacy scan, beginning flair scan")
    scan_docs("flair")
    print("Done flair scan")