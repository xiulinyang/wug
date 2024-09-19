
from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM
import torch
import torch.nn.functional as F

masked_lm_names = ["google-bert/bert-base-uncased","google-bert/bert-large-uncased", ]

# Approach One: Using Pipeline
for model_name in masked_lm_names:
    nlp = pipeline("fill-mask", model=model_name)
    result_pipeline = nlp(f"This is the best thing I've [MASK] in my life.", targets=['done', 'seen'])
    print(result_pipeline)