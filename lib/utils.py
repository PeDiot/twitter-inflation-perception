import os 
from typing import List 

from lib.enums import CONFIG 
LEXICAL_FIELDS = [val["file_name"] for val in CONFIG.values()]

def get_files(backup_dir: str) -> List: 
    """Description. Return list of files in folder."""

    return [f"{backup_dir}{f}" for f in os.listdir(backup_dir)]

def get_lexical_field(file_path: str) -> str: 
    """Description. Extract lexical field from file path."""

    file_name = file_path.split("/")[-1]
    lexical_field = file_name.split("_")[0] 

    if lexical_field == "econ": 
        lexical_field = "econ_terms"

    if lexical_field not in LEXICAL_FIELDS: 
        raise ValueError(f"lexical_field must be in {LEXICAL_FIELDS}.")

    return lexical_field
