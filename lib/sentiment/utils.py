from torch import Tensor
import numpy as np

from typing import List, Dict 

def tensor_to_numpy(tensor: Tensor) -> np.ndarray: 
    """Description. Convert tensor to numpy array."""

    if tensor.device.type == "cuda": 
        tensor = tensor.cpu()

    return tensor.detach().numpy()

def results_to_dict(epoch: int, train_batch_losses: List, training_times: List, val_batch_scores: List) -> Dict: 
    """Description. Convert training/validation results to dictionnary for one epoch."""

    return {
        "epoch": epoch, 
        "train_batch_losses": train_batch_losses, 
        "training_times": training_times, 
        "val_batch_scores": val_batch_scores
    }

def get_avg_training_losses(statistics: List) -> List: 
    """Description. Compute average training loss for each epoch."""

    return [np.mean(stat["train_batch_losses"]) for stat in statistics]