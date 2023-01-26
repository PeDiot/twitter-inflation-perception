"""Description. 
Basic preprocessing transfomation to Twitter data. 
"""

from typing import Union
from datetime import datetime

from pandas.core.frame import DataFrame 

def _string_to_float(x: Union[float, int, str]) -> float: 
    """Description. 
    Convert int or string object to float."""

    if type(x) == float: 
        return x
    
    elif type(x) == int: 
        return float(x)

    elif type(x) == str: 
        x = x.lower()
        
        if "k" in x: 
            x = x.replace("k", "")
            if "." in x: 
                x = x.split(".") 
                mul = 10**max(0, 3 - len(x[-1]))
                x = "".join(x)
            else: 
                mul = 1000
            x = mul * float(x.replace(",", ""))
        else: 
            x = float(x.replace(",", ""))

        return x

    else: 
        raise ValueError("x must be of type float, int or str.")

def _to_datetime(x: str) -> datetime: 
    """Description. Convert string object to datetime."""
    if "T" not in x: 
        raise ValueError("T not in input.")
    
    return datetime.strptime(x.split("T")[0], "%Y-%m-%d") 

def clean_data(df: DataFrame) -> DataFrame: 
    """Description. Apply basic preprocessing steps to Twitter data."""

    df.columns = df.columns.str.lower()

    cols = ["timestamp", "embedded_text", "emojis", "retweets", "likes", "comments"]
    df = df.loc[:, cols]

    df = df.rename(columns={"embedded_text": "text"})
    df.loc[:, "text_emojis"] = df.loc[:, "text"] + " " + df.loc[:, "emojis"]

    num_cols = ["retweets", "likes", "comments"]

    for col in num_cols: 
        df[col] = df[col].apply(_string_to_float) 

    df["timestamp"] = df["timestamp"].apply(_to_datetime)

    return df.reset_index(drop=True)



    