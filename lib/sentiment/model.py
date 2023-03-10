from typing import Optional

import torch 
from transformers import CamembertForSequenceClassification

def backup_model(model: CamembertForSequenceClassification, path: str) -> CamembertForSequenceClassification: 
    """Description. Save model improvements at the end of each epoch."""

    torch.save(model.state_dict(), path)
    print(f"Model saved at {path}")

def load_model(model_path: Optional[str]=None, num_labels: int=2): 
    """Description. Load pre-trained camemBERT from local directory or from Hugging Face."""

    if model_path: 

        if model_path.split(".")[-1] != "pt": 
            raise ValueError("model_path must be a .pt file.")
        
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        
        if device.type == "cpu": 
            map_location = torch.device("cpu")
        else: 
            map_location = torch.device("cuda:0") 

        state_dict = torch.load(model_path, map_location=map_location)
        print("Loading trained model...")
        model = CamembertForSequenceClassification.from_pretrained("camembert-base", state_dict=state_dict)

    else: 
        model = CamembertForSequenceClassification.from_pretrained("camembert-base", num_labels=num_labels)

    return model