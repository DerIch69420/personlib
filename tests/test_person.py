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

def test_create_person() -> None:
    ''' test person creation '''
    p = personlib.Person("TestUser")

    assert os.path.exists(os.path.join(personlib.DB_DIR, "testuser.json"))

def test_name() -> None:
    ''' test name attributes and methods '''
    p = personlib.Person("OldName")
    p.name = "NewName"

    assert os.path.exists(os.path.join(personlib.DB_DIR, "newname.json"))
    assert not os.path.exists(os.path.join(personlib.DB_DIR, "oldname.json"))

    with pytest.raises(Exception) as excinfo:

        p1 = personlib.Person("User")
        p2 = personlib.Person("User1")
        p2.name = "User"
    assert str(excinfo.value) == "A person with this name already exists"  

    assert os.path.exists(os.path.join(personlib.DB_DIR, "user.json"))
    assert os.path.exists(os.path.join(personlib.DB_DIR, "user1.json"))

