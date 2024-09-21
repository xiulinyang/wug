import pandas as pd
import spacy
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM

nlp = spacy.load('en_core_web_sm')
model = 'google-bert/bert-base-uncased'

tokenizer = AutoTokenizer.from_pretrained(model)


transitivity = pd.read_csv('verb_transitivity.tsv', sep='\t')[['verb', 'intrans', 'percent_intrans']]
transitivity_sorted = transitivity.sort_values(by='intrans', ascending=False)
transitivity_sorted = transitivity_sorted.sort_values(by='percent_intrans', ascending=False)[:10000][['verb']].values.tolist()
transitivity_sorted = [y for x in transitivity_sorted for y in x]
with open('intransitive_tokens.txt', 'r') as t, open('multi_tokens.txt', 'w') as sa:
    for token in t.readlines():
        lemma_token = token.strip()
        third_person = token.strip()+'s'
        tokenized_lemma = tokenizer.tokenize(token)
        tokenized_third_person = tokenizer.tokenize(third_person)
        # print(tokenized_third_person, tokenized_lemma)
        # if len(tokenized_third_person) == len(tokenized_lemma):
        #     pass
        #     # sa.write(f'{lemma_token}\n')
        # else:
        #     print(tokenized_third_person, tokenized_lemma)
        #     print(lemma_token)
        #     sa.write(f'{lemma_token}\n')
        if len(tokenized_lemma)>1:
            print(tokenized_third_person, tokenized_lemma)
            print(lemma_token)
            sa.write(f'{lemma_token}\n')

# for x in tokenizer.vocab:
#     if x[-1] =='s' and x in transitivity_sorted:
#         print(x)


'''
lemmatize possible intransitive verbs
'''
# intransitive_tokens = []
# for word in transitivity_sorted:
#     for w in nlp(word):
#         lemma = w.lemma_
#         if lemma not in intransitive_tokens:
#             intransitive_tokens.append(lemma)

# with open('intransitive_tokens.txt', 'w') as intrans:
#     for token in intransitive_tokens:
#         intrans.write(f'{token}\n')