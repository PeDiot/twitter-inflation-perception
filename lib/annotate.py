"""Description. 
Helpful function for tweet annotation."""

from pandas.core.frame import DataFrame
from pandas.core.series import Series
from typing import Tuple, List

import numpy as np 

def extract_random_tweets(df: DataFrame, prop: float=.011) -> Tuple:
    """Description. Extract random tweets from Twitter dataset.
    
    Attributes: 
        - df: original dataset 
        - prop: proportion of random tweets to select
        
    Returns: 
        - indices of selected tweets
        - selected tweets"""
    
    if "lexical_field" not in df.columns: 
        raise ValueError("lexical_field not in columns.")

    if "text" not in df.columns:
        raise ValueError("text not in columns.")
    
    def _select_samples(x: Series) -> Series:
        n = x.shape[0]
        return x.sample(n=int(n * prop), replace=False)

    grouped = df.groupby("lexical_field",as_index=False)
    sampled_df = grouped.apply(_select_samples).reset_index(level=0, drop=True)
    
    idxs = sampled_df.index.to_list()
    tweets = sampled_df["text"].to_list()

    return idxs, tweets

def add_labels(df: DataFrame, idxs: List, labels: List) -> DataFrame:
    """Description. Add 'Label' column to Twitter datasets.""" 

    labelled_df = df.copy()    
    mask = labelled_df.index.isin(idxs)
    labelled_df.loc[mask, "label"] = labels

    return labelled_df