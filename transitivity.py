import json

import pandas as pd
import spacy
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM

nlp = spacy.load('en_core_web_sm')
model1 = 'google-bert/bert-base-uncased'

model2 = 'openai-community/gpt2'
tokenizer1 = AutoTokenizer.from_pretrained(model1)
tokenizer2 = AutoTokenizer.from_pretrained(model2)

transitivity = pd.read_csv('verb_transitivity.tsv', sep='\t')[['verb', 'intrans', 'percent_intrans']]
transitivity_sorted = transitivity.sort_values(by='intrans', ascending=False)
transitivity_sorted = transitivity_sorted.sort_values(by='percent_intrans', ascending=False)[:10000][['verb']].values.tolist()
transitivity_sorted = [y for x in transitivity_sorted for y in x]


# with open('intransitive_tokens.txt', 'r') as t, open('multi_tokens.txt', 'w') as sa:
#     for token in t.readlines():
#         lemma_token = token.strip()
#         third_person = token.strip()+'s'
#         tokenized_lemma = tokenizer.tokenize(token)
#         tokenized_third_person = tokenizer.tokenize(third_person)
#         # print(tokenized_third_person, tokenized_lemma)
#         # if len(tokenized_third_person) == len(tokenized_lemma):
#         #     pass
#         #     # sa.write(f'{lemma_token}\n')
#         # else:
#         #     print(tokenized_third_person, tokenized_lemma)
#         #     print(lemma_token)
#         #     sa.write(f'{lemma_token}\n')
#         if len(tokenized_lemma)>1:
#             print(tokenized_third_person, tokenized_lemma)
#             print(lemma_token)
#             sa.write(f'{lemma_token}\n')

# for x in tokenizer.vocab:
#     if x[-1] =='s' and x in transitivity_sorted:
#         print(x)

# c=0
#
# with open('blimp/irregular_plural_subject_verb_agreement_1.jsonl', 'r') as p, open('blimp/irregular_plural_subject_verb_agreement_1_same.jsonl', 'w') as sa, open('blimp/irregular_plural_subject_verb_agreement_1_diff.jsonl', 'w') as di:
#     for f in p.readlines():
#         result = json.loads(f)
#         # tokenized_single = tokenizer1.tokenize(result['sentence_good'])
#         # tokenized_plural = tokenizer1.tokenize(result['sentence_bad'])
#
#         tokenized_single2 = tokenizer2.tokenize(result['sentence_good'][:-1].split()[-1])
#         tokenized_plural2 = tokenizer2.tokenize(result['sentence_bad'][:-1].split()[-1])
#         if len(tokenized_single2) == len(tokenized_plural2):
#             json.dump(result, sa)
#             sa.write('\n')
#             c+=1
#         else:
#             json.dump(result, di)
#             di.write('\n')
#
#             # if ''.join(tokenized_plural) not in diff:
#             #     diff.append(''.join(tokenized_plural))
#
#     print(c)
# with open('diff_tokens.txt', 'r') as d:
#     for t in d.readlines():
#         tokenized = tokenizer(t.strip())
#         tokenized2 = tokenizer(t.strip()+'s')
#         if len(tokenizer(t.strip())) == len(tokenizer(t.strip()+'s')):
#             print(t)
#             print(tokenizer.convert_ids_to_tokens(tokenized.input_ids), tokenizer.convert_ids_to_tokens(tokenized2.input_ids))

'''
lemmatize possible intransitive verbs
'''
intransitive_tokens = []
for word in transitivity_sorted:
    for w in nlp(word):
        lemma = w.lemma_
        if lemma not in intransitive_tokens:
            intransitive_tokens.append(lemma)

with open('intransitive_tokens_test.txt', 'w') as intrans:
    for token in intransitive_tokens:
        intrans.write(f'{token}\n')