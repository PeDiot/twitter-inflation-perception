from typing import (
    List, 
    Optional, 
    Tuple, 
)

import torch 

from transformers import CamembertTokenizer

def load_tokenizer() -> CamembertTokenizer: 
    return CamembertTokenizer.from_pretrained("camembert-base", do_lower_case=True)

def preprocess(tweets: List, tokenizer: CamembertTokenizer, sentiments: Optional[List]=None) -> Tuple:
    """Description.
    Preprocess raw tweets and optional sentiments.

    Attributes:
        - tweets (array-like): list of tweets as strings 
        - tokenizer: camemBERT tokenizer to encode strings       
        - sentiments: optional list of sentiments (1 if positive, 0 else)
    
    Returns
        - inputs_ids: tensors obtained from converting tweets into numbers
        - attention_masks: tensors indicating which tokens should be attended to
        - sentiments (optional)"""

    encoded_batch = tokenizer.batch_encode_plus(tweets,
                                                add_special_tokens=False,
                                                pad_to_max_length=True,
                                                return_attention_mask=True,
                                                return_tensors="pt")
    if sentiments:
        sentiments = torch.tensor(sentiments)
        return encoded_batch["input_ids"], encoded_batch["attention_mask"], sentiments

    return encoded_batch["input_ids"], encoded_batch["attention_mask"]

def train_val_split(tweets: List, sentiments: List, train_prop: float) -> Tuple: 
    """Description. 
    Split tweets and sentiment arrays into training and validation arrays."""

    if len(sentiments) != len(tweets): 
        raise ValueError("sentiments and tweets must have equal lengths.")
    
    n = len(sentiments)
    split_border = int(n * train_prop) 

    tweets_train, tweets_validation = tweets[:split_border], tweets[split_border:]
    sentiments_train, sentiments_validation = sentiments[:split_border], sentiments[split_border:]

    return (
        tweets_train, tweets_validation, 
        sentiments_train, sentiments_validation
    )