import json # storing and loading person data
import os # checking if dirs and files exist
from typing import Optional
from datetime import date # birth date of person

import personlib  # to get global DB_DIR


class Person:
    # constructor
    def __init__(self, name: str) -> None:
        self._name: str = name # given by user

        # other data set to None
        # chagned by user or via loading json-file
        self._age: Optional[int] = None
        self._birth_date: Optional[date] = None

        # get global DB_DIR
        self._db_dir = personlib.DB_DIR
        os.makedirs(self._db_dir, exist_ok=True) # create database dir

        self._filepath: str = os.path.join(self._db_dir, f"{self._name.lower()}.json")
        self._load_or_init() # load person data or create a new one

    def _load_or_init(self) -> None:
        if os.path.exists(self._filepath):
            with open(self._filepath, "r") as file:
                data = json.load(file)

                # set each variable except for "name"
                self._age = data.get("age")
                birth_date_str = data.get("birth_date")
                self._birth_date = date.fromisoformat(birth_date_str) if birth_date_str else None


        else:
            self._save() # create empty new person with given name

    def _save(self) -> None:
        with open(self._filepath, "w") as file:
            json.dump({
                "name": self._name,
                "age": self._age,
                "birth_date": self._birth_date.isoformat() if self._birth_date else None,
            }, file, indent=4)

    def __str__(self) -> str:
        ''' return all information about the person '''
        return (
            f"Name: {self._name}\n"
            f"Age: {self._age}\n"
            f"Birth Date: {self._birth_date}"
        )

    # name of person
    @property
    def name(self) -> Optional[str]:
        '''The name property.'''
        return self._name
    @name.setter
    def name(self, new_name: str) -> None:
        ''' change the name of the person '''
        if isinstance(new_name, str) and new_name.strip():
            old_filepath = self._filepath
            self._name = new_name
            self._filepath = os.path.join(self._db_dir, f"{self._name.lower()}.json")
            if os.path.exists(old_filepath):
                os.rename(old_filepath, self._filepath)
            self._save()

    # age of person
    @property
    def age(self) -> Optional[int]:
        ''' return the age of the person'''
        return self._age
    @age.setter
    def age(self, value: Optional[int]) -> None:
        ''' change the age of the person '''
        if value is None or (isinstance(value, int) and value >= 0):
            self._age = value
            self._save()
        else:
            raise ValueError("Age must be a non-negative integer or None")

    # birth date of person
    @property
    def birth_date(self):
        ''' return the birth date of the person '''
        return self._birth_date
    @birth_date.setter
    def birth_date(self, value: Optional[date]) -> None:
        ''' change the birth date of the person '''
        if value is None or isinstance(value, date):
            self._birth_date = value
            self._save()
        else:
            raise ValueError("Birth date must be of type date or None")

