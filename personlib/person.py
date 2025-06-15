import json # storing and loading person data
import os # checking if dirs and files exist
from typing import Optional
import personlib  # to get global DB_DIR


class Person:
    # constructor
    def __init__(self, name: str) -> None:
        self._name: str = name # given by user

        # other data set to None
        # chagned by user or via loading json-file
        self._age: Optional[int] = None

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
                self.age = data.get("age")
        else:
            self._save() # create empty new person with given name

    def _save(self) -> None:
        with open(self._filepath, "w") as file:
            json.dump({
                "name": self._name,
                "age": self._age,
            }, file, indent=4)

    def __str__(self) -> str:
        ''' return all information about the person '''
        return f"Name: {self._name}\nAge: {self._age}\n"

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

    def change_name(self, new_name: str) -> None:
        ''' change the name of the person '''
        if isinstance(new_name, str) and new_name.strip():
            old_filepath = self._filepath
            self._name = new_name
            self._filepath = os.path.join(self._db_dir, f"{self._name.lower()}.json")
            if os.path.exists(old_filepath):
                os.rename(old_filepath, self._filepath)
            self._save()

