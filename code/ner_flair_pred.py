from flair.models import SequenceTagger
from flair.data import Sentence
import torch
import gc
try:
    model
except NameError:
    pass
else:
    del model
    gc.collect()
    print("MODEL DELETED")
torch.cuda.empty_cache()
torch.cuda.set_per_process_memory_fraction(1.0)
model = SequenceTagger.load('resources/taggers/sota-ner-flair/final-model.pt')


def flair_predict(text):
    # create example sentence
    sentence = Sentence(text)

    # predict tags and print
    model.predict(sentence)

    s = ""
    for entity in sentence.get_spans('ner'):
        s += str(entity) + '\n'
        
    return s