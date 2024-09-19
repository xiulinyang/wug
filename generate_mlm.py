import json
with open('data/natural.jsonl', 'r') as natural, open('data/natrual_mlm.jsonl', 'w') as mlm:
    for sent_natural in natural.readlines():
        natural_example = json.loads(sent_natural)
        sent_good = natural_example['sentence_good'].split()
        sent_bad = natural_example['sentence_bad'].split()
        for i, word in enumerate(sent_good):
            if word!=sent_bad[i]:
                output = sent_good[:i] + ['[MASK]'] + sent_good[i+1:]




