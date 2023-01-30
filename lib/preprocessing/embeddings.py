"""Description. Transform text from tweets into embeddings. 

See Hugging Face for more details: https://huggingface.co/dangvantuan/sentence-camembert-large

Example: 
    
>>> from lib.preprocessing.embeddings import text_to_embeddings, load_transformer
>>> import pickle as pkl
>>> path = "./backup/data/"
>>> file_path = path+"tweets_preprocessed.pkl"
>>> with open(file_path, "rb") as f: tweets_preprocessed = pkl.load(f)
>>> tweets = tweets_preprocessed["cleaned"]
>>> model = load_transformer()
>>> embeddings = text_to_embeddings(model, tweets, file_path=path+"embeddings.npy")
Batches:   1%|▋                                                                            | 24/2902 [01:21<2:54:49,  3.64s/it]
"""

import numpy as np 
from typing import List, Optional
from sentence_transformers import SentenceTransformer

def load_transformer(model_name: str="all-MiniLM-L6-v2") -> SentenceTransformer:
    """Description. Load SentenceTransformer from Hugging Face.""" 

    model = SentenceTransformer(model_name)
    return model 

def text_to_embeddings(model: SentenceTransformer, sentences: List, file_path: Optional[str]=None) -> np.ndarray: 
    """Description. 
    Convert list of sentences into numerical numpy array and save as npy file."""

    embeddings = model.encode(sentences, show_progress_bar=True)

    if file_path: 
        if file_path.split(".")[-1] != "npy": 
            raise ValueError("file_path must be end by .npy.")

        with open(file_path, "wb") as f:
            np.save(f, embeddings)
    
    return embeddings

