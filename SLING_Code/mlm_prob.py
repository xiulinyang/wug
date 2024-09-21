
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM
import torch
import json
import torch.nn.functional as F
from glob import glob
masked_lm_names = ["google-bert/bert-base-uncased","google-bert/bert-large-uncased"]
all_paths = glob('/Users/xiulinyang/Desktop/TODO/wug/data_mlm/*.jsonl')

def prob(model, sent, options):
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForMaskedLM.from_pretrained(model)
    model.eval()  # Put the model in evaluation mode

    inputs = tokenizer(sent, return_tensors="pt")

    # Predict all tokens
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = outputs.logits

    # Apply softmax to get probabilities for the masked token
    mask_token_index = (inputs['input_ids'] == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
    softmax_probs = F.softmax(predictions[0, mask_token_index, :], dim=-1).squeeze()

    done_id = tokenizer.convert_tokens_to_ids(options[1])
    seen_id = tokenizer.convert_tokens_to_ids(options[2])

    return softmax_probs[done_id].item(), softmax_probs[seen_id].item()


with open('result.txt', 'w') as result:

    for model_name in masked_lm_names:
        nlp = pipeline("fill-mask", model=model_name)
        for p in all_paths:
            for exp in open(p).readlines():
                json_dic = json.loads(exp)
                result_pipeline = nlp(json_dic['sent'], targets=[json_dic['option_good'], json_dic['option_bad']])
                print(result_pipeline)