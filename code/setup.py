import os
from misc import scan_docs

#sets up static files for HTML and does NER on documents
p = os.popen('./pdffirst.sh')
print(p.read())
print("Done duping, beginning spacy scan")
scan_docs("spacy")
print("Done spacy scan, beginning flair scan")
scan_docs("flair")
print("Done flair scan")