import os
import shutil
import personlib


def setup_module(module):
    # setup a test directory for each test module
    personlib.DB_DIR = "test_db"
    os.makedirs(personlib.DB_DIR, exist_ok=True)


def teardown_module(module):
    # clean up after tests
    shutil.rmtree(personlib.DB_DIR)


def test_create_person_and_set_age():
    p = personlib.Person("TestUser")
    p.age = 25

    assert p.age == 25
    assert os.path.exists(os.path.join(personlib.DB_DIR, "testuser.json"))


def test_change_name():
    p = personlib.Person("OldName")
    p.age = 20
    p.change_name("NewName")

    assert os.path.exists(os.path.join(personlib.DB_DIR, "newname.json"))
    assert not os.path.exists(os.path.join(personlib.DB_DIR, "oldname.json"))

