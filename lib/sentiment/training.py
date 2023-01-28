from transformers import CamembertForSequenceClassification, AdamW, get_linear_schedule_with_warmup

import torch 
from torch.utils.data import DataLoader
from torch.optim.lr_scheduler import LambdaLR

from typing import Tuple, List
import time 
from tqdm import tqdm 

from .model import backup_model

def init_scheduler(num_epochs: int, dataloader: DataLoader, optimizer: AdamW) -> LambdaLR: 
    """Description. 
    Initialize the scheduler which creates a schedule with a learning rate that decreases linearly towards 0."""

    num_steps = num_epochs * len(dataloader)
    scheduler = get_linear_schedule_with_warmup(optimizer, 
                                                num_warmup_steps = 0, 
                                                num_training_steps = num_steps)

    return scheduler
    
def check_convergence(
        model: CamembertForSequenceClassification, 
        path: str, 
        losses: List, 
        curr_loss: float, 
        consecutive_epochs_with_no_improve: int) -> int: 
    """Description. 
    Check whether current training loss is less than minimum loss over last epochs.
    
    Returns: update number of consecutive epochs with no improvements."""

    if min(losses) <= curr_loss: 
        consecutive_epochs_with_no_improve += 1
    else: 
        consecutive_epochs_with_no_improve = 0
        backup_model(model, path)

    return consecutive_epochs_with_no_improve

def train(
        model: CamembertForSequenceClassification, 
        dataloader: DataLoader, 
        device: torch.device, 
        optimizer: AdamW, 
        scheduler: LambdaLR, 
        epoch: int, num_epochs: int) -> Tuple: 
    """Description. Fine-tune camemBERT model over multiple batch for one training epoch.
    
    Attributes: 
        - model: camemBERT model 
        - dataloader: iterator of data batches 
        - device: device to store tensors
        - optimizer: algorithm to update model parameters
        - scheduler: linear scheduler for learning rate
        - epoch: running epoch
        - num_epochs: total number of epochs
        
    Returns: 
        - batch_losses: loss for each training batch 
        - training_times: list of training times per batch."""
    
    model.train()
    
    loop = tqdm(dataloader)
    loop.set_description(f"Training Epoch [{epoch + 1}/{num_epochs}]")

    t0 = time.time()
    training_times = []

    batch_losses = []

    for batch in loop:
      
        input_id = batch[0].to(device)
        attention_mask = batch[1].to(device)
        sentiment = batch[2].to(device)

        model.zero_grad()        

        output = model(
            input_id, 
            token_type_ids=None, 
            attention_mask=attention_mask, 
            labels=sentiment)
        
        loss = output.loss

        loss_value = loss.item()
        batch_losses.append(loss_value)

        loss.backward()

        # Clip the norm of the gradients to 1.0
        # This is to help prevent the "exploding gradients" problem.
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

        optimizer.step()

        # Update the learning rate.
        scheduler.step()

        training_time = time.time() - t0
        t0 = training_time 
        training_times.append(t0)

        loop.set_postfix(loss_train=round(loss_value, 2), training_time=round(t0, 2))

    return batch_losses, training_times