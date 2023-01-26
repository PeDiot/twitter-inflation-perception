from lib.utils import get_files
from lib.enums import BACKUP
import pytest

def test_get_files(mocker):
    backup_dir = f"../{BACKUP}"
    mock = mocker.patch("os.listdir", return_value=[])

    result = get_files(backup_dir)
    assert result == []  

    mock.assert_called_once_with(backup_dir)