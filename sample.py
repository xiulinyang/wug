
from wuggy import WuggyGenerator
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM

model2 = 'openai-community/gpt2'
tokenizer = AutoTokenizer.from_pretrained(model2)

g = WuggyGenerator()
g.load("orthographic_english")
with open('/Users/xiulinyang/Desktop/TODO/wug/verbs.txt', 'r') as verb:
    for v in verb.readlines():

        standard = False
        while not standard:
            for w in g.generate_classic([v],ncandidates_per_sequence=1):
                if w[-1]!='s':
                    correct_verb = w+'s'
                    wrong_verb = w

                    single_correct = 'He '+correct_verb+'.'
                    single_wrong = 'He '+wrong_verb +'.'

                    plural_correct = 'They ' + wrong_verb+'.'
                    plural_wrong = 'They ' + correct_verb+'.'

                    single_natural_correct = 'He '+v+'s.'
                    single_natural_wrong = 'He ' +v+'.'
                    print(tokenizer.tokenize(single_wrong))
                    # if len(tokenizer.tokenize(single_correct))



