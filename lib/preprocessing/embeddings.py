"""Description. Transform text from tweets into embeddings. 

See here for more details: https://www.sbert.net/
"""

import numpy as np 
from typing import List, Optional
from sentence_transformers import SentenceTransformer, util

def text_to_embeddings(sentences: List, file_path: Optional[str]=None) -> np.ndarray: 
    """Description. 
    Convert list of sentences into numerical numpy array and save as npy file.
    
    Example: 
    
    >>> from lib.preprocessing.embeddings import text_to_embeddings
    >>> import pickle as pkl
    >>> path = "./backup/data/"
    >>> file_path = path+"tweets_preprocessed.pkl"
    >>> with open(file_path, "rb") as f: tweets_preprocessed = pkl.load(f )
    >>> tweets = tweets_preprocessed["cleaned"]
    >>> embeddings = text_to_embeddings(tweets, file_path=path+"embeddings.npy")
    Batches:   1%|▋                                                                            | 24/2902 [01:21<2:54:49,  3.64s/it]"""

    if file_path.split(".")[-1] != "npy": 
        raise ValueError("file_path must be end by .npy.")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(sentences, show_progress_bar=True)

    with open(file_path, "wb") as f:
        np.save(f, embeddings)
    
    return embeddings

