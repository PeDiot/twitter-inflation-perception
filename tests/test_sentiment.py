from lib.sentiment.utils import tensor_to_numpy, get_avg_training_losses
from lib.sentiment.training import check_convergence 

import torch 
import numpy as np 

import pytest

@pytest.fixture
def statistics(): 
    stats = [
        {
            "epoch": 0, 
            "train_batch_losses": [1., 2.], 
            "training_times": np.random.uniform(0, 1, 2), 
            "val_batch_scores": np.random.uniform(0, 1, 2)
        }, 
        {
            "epoch": 1, 
            "train_batch_losses": [.0, 1.], 
            "training_times": np.random.uniform(0, 1, 2), 
            "val_batch_scores": np.random.uniform(0, 1, 2)
        }
    ] 
    return stats 

def test_tensor_to_numpy(): 
    x = torch.tensor(data=[.3, 1., .2], device="cpu")
    y = tensor_to_numpy(x)

    assert type(y) == np.ndarray 
    assert y.shape == (3,)

def test_get_avg_training_losses(statistics): 
    avg_training_losses = get_avg_training_losses(statistics)
    expected = [1.5, .5] 

    assert avg_training_losses == expected

def test_check_convergence(): 
    consecutive_epochs_with_no_improve = 0
    losses = [.9, .8, .75]
    curr_loss = .8 

    consecutive_epochs_with_no_improve = check_convergence(losses, curr_loss, consecutive_epochs_with_no_improve) 
    assert consecutive_epochs_with_no_improve == 1 

    losses.append(curr_loss) 
    curr_loss = .6 
    consecutive_epochs_with_no_improve = check_convergence(losses, curr_loss, consecutive_epochs_with_no_improve) 
    assert consecutive_epochs_with_no_improve == 0



    