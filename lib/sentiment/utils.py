from torch import Tensor
import numpy as np

def tensor_to_numpy(tensor: Tensor) -> np.ndarray: 
    """Description. Convert tensor to numpy array."""

    if tensor.device.type == "cuda": 
        tensor = tensor.cpu()

    return tensor.detach().numpy()