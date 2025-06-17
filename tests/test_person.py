import os
import shutil
import personlib
import pytest

from datetime import date
from math import floor

def setup_module(module) -> None:
    # setup a test directory for each test module
    personlib.DB_DIR = "test_db"
    # os.makedirs(personlib.DB_DIR, exist_ok=True)

def teardown_module(module) -> None:
    # clean up after tests
    shutil.rmtree(personlib.DB_DIR)

def test_db_creation() -> None:
    p = personlib.Person("DataBaseInitIfEmpty")

    assert os.path.exists(personlib.DB_DIR)
