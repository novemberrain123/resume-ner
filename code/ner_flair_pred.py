from flair.models import SequenceTagger
from flair.data import Sentence
import torch

torch.cuda.empty_cache()

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