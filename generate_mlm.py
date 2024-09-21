import json
with open('data/pseudo.jsonl', 'r') as natural, open('data_mlm/pseudo_mlm.jsonl', 'w') as mlm:
    for sent_natural in natural.readlines():
        natural_example = json.loads(sent_natural)
        sent_good = natural_example['sentence_good'][:-1].split()
        sent_bad = natural_example['sentence_bad'][:-1].split()
        for i, word in enumerate(sent_good):
            if word!=sent_bad[i]:
                output = ' '.join(sent_good[:i] + ['[MASK]'] + sent_good[i+1:])+'.'
                good_option = word
                bad_option = sent_bad[i]
                to_dump = {'sent': output, 'option_good': good_option, 'option_bad': bad_option}
                json.dump(to_dump, mlm)
                mlm.write('\n')




