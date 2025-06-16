import os
import shutil
import personlib

from datetime import date


def setup_module(module):
    # setup a test directory for each test module
    personlib.DB_DIR = "test_db"
    os.makedirs(personlib.DB_DIR, exist_ok=True)


def teardown_module(module):
    # clean up after tests
    shutil.rmtree(personlib.DB_DIR)


def test_create_person():
    ''' test person creation '''
    p = personlib.Person("TestUser")

    assert os.path.exists(os.path.join(personlib.DB_DIR, "testuser.json"))

def test_age():
    ''' test age attributes and methods '''
    p = personlib.Person("AgeTest")
    p.age = 25
    assert p.age == 25

    p1 = personlib.Person("AgeNone")
    assert p1.age == None

def test_name():
    ''' test name attributes and methods '''
    p = personlib.Person("OldName")
    p.age = 20
    p.name = "NewName"

    assert os.path.exists(os.path.join(personlib.DB_DIR, "newname.json"))
    assert not os.path.exists(os.path.join(personlib.DB_DIR, "oldname.json"))

def test_birth_date():
    ''' test birth date attributes and methods '''
    p = personlib.Person("BirthDateTest")
    p._birth_date = date(2010, 6, 16)
    assert p.birth_date == date(2010, 6, 16)

    p1 = personlib.Person("BirthDateNone")
    assert p1.birth_date == None
