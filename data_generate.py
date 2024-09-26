import pandas as pd
import json
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM

model2 = 'openai-community/gpt2'
with open('simple_svo/natural.jsonl', 'w') as natural, open('verbs.txt', 'r') as verbs:
    for v in verbs.readlines():
        text_correct = 'He '+v.strip()+'s'
        text_wrong = 'He ' + v.strip()+''
        natural_pair = {'sentence_good': text_correct+'.', 'sentence_bad': text_wrong+'.', 'Phenomenon': 'natural'}
        json.dump(natural_pair, natural)
        natural.write('\n')
        text_correct1 = 'They ' + v.strip() +''
        text_wrong1 = 'They ' + v.strip() + 's'
        natural_pair1 = {'sentence_good': text_correct1 + '.', 'sentence_bad': text_wrong1 + '.', 'Phenomenon': 'natural'}
        json.dump(natural_pair1, natural)
        natural.write('\n')
        # natural.write()



