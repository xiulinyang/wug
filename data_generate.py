import pandas as pd
import json
# with open('data/natural.jsonl', 'w') as natural, open('data/pseudo.jsonl', 'w') as pseudo:
#     sub= pd.read_pickle('subj_rel.pickle')
#     for k, v in sub.items():
#         for v1, v2 in v:
#             if 'is' in v1 or 'is' in v2:
#                 continue
#             else:
#                 natural_pair = {'sentence_good': v1+'.', 'sentence_bad': v2+'.', 'Phenomenon': 'natural'}
#                 json.dump(natural_pair, natural)
#                 natural.write('\n')
#         # natural.write()

with open('data/pseudo.jsonl', 'w') as p, open('data/')