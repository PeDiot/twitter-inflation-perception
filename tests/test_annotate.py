from lib.annotate import add_labels

import pandas as pd
import pytest

@pytest.fixture
def data(): 
    """Description. Create small dataset to test functions."""

    d = {
        "timestamp": ["2020-10-06", "2020-01-01", "2021-06-28"], 
        "text": ["hello poor world", "inflation is a hot topic right now", "let's use chat gpt to make some money"], 
        "emojis": ["😊", float("nan"), "🚀"], 
        "retweets": [202., 90., 1.], 
        "likes": [5., 19., 900.], 
        "comments": [21., 1., 0.], 
        "lexical_field": ["cheap", "econ_terms", "prices"], 
        "text_emojis": ["hello poor world 😊", "inflation is a hot topic right now", "let's use chat gpt to make some money 🚀"]
    }

    return pd.DataFrame(d)


def test_add_labels(data): 
    indices = data.index.values.tolist()
    labels = ["not_about_prices", "inflation", "other"]
    new_data = add_labels(data, indices, labels)

    assert new_data["label"].values.tolist() == labels 