from lib.utils import get_files, get_lexical_field
from lib.enums import BACKUP
import pytest

def test_get_files(mocker):
    backup_dir = f"../{BACKUP}"
    mock = mocker.patch("os.listdir", return_value=[])

    result = get_files(backup_dir)
    assert result == []  

    mock.assert_called_once_with(backup_dir)

def test_get_lexical_field(): 
    file_path = "../backup/tweets/econ_terms_2020-01-01_2020-12-31.csv"
    assert get_lexical_field(file_path) == "econ_terms" 

    with pytest.raises(ValueError): 
        get_lexical_field("../backup/tweets/economics_2020-01-01_2020-12-31.csv")