#refer to this https://github.com/chakki-works/seqeval

from seqeval.metrics import classification_report

def class_report(y_true, y_pred):
    print(classification_report(y_true, y_pred))