from transformers.models.camembert.modeling_camembert import CamembertForSequenceClassification

import torch 
from torch.utils.data import DataLoader
from torch import Tensor

from sklearn.metrics import balanced_accuracy_score
from tqdm import tqdm

from typing import Tuple, List 

from .utils import tensor_to_numpy

def predict(
        input_ids: Tensor, 
        attention_mask: Tensor, 
        model: CamembertForSequenceClassification, 
        eval_mode: bool=True) -> Tuple:
    """Description. 
    Run camemBERT given tokenized texts and attentions mask and return predictions. 
    
    Attributes: 
        - input_ids: tensors obtained from converting texts into embeddins
        - attention_mask: indicates to the model which tokens should be attended to
        - model: camemBERT model
        - eval_mode: indicates whether torch.no_grad() and model.eval() has been already called
        
    Returns: 
        - predicted_labels: sentiments outputed by camBERT
        - scores: probabilities for each label"""

    if eval_mode: 
        output = model(input_ids, attention_mask=attention_mask)
        scores = torch.softmax(output.logits, dim=1)
        predicted_labels = torch.argmax(output.logits, dim=1)
    
    else: 
        with torch.no_grad():
            model.eval()

            output = model(input_ids, attention_mask=attention_mask)
            scores = torch.softmax(output.logits, dim=1)
            predicted_labels = torch.argmax(output.logits, dim=1)
        
    return predicted_labels, scores

def evaluate(model: CamembertForSequenceClassification, dataloader: DataLoader, device: torch.device) -> List:
    """Description. Evaluate model on unseen batches and return balanced accuracy scores per batch.""" 

    accuracy_scores = [] 
    loop = tqdm(dataloader) 
    loop.set_description("Validation in progress")

    with torch.no_grad():
        model.eval()

        for batch in dataloader: 
            
            input_id = batch[0].to(device)
            attention_mask = batch[1].to(device)
            sentiment = batch[2]

            predicted_labels, _ = predict(input_id, attention_mask, model)
            predicted_labels = tensor_to_numpy(predicted_labels)

            bacc = balanced_accuracy_score(sentiment, predicted_labels)
            accuracy_scores.append(bacc)

            loop.set_postfix(balanced_accuracy_score=round(bacc, 2))
    
    return accuracy_scores