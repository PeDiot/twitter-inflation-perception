import os 
from typing import List 

def get_files(backup_dir: str) -> List: 
    """Description. Return list of files in folder."""

    return [f"{backup_dir}{f}" for f in os.listdir(backup_dir)]