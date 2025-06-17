import json # storing and loading person data
import os # checking if dirs and files exist
from typing import Optional
from datetime import date, timedelta # birth date and age of person
from math import floor # convert days to years (age of person)

import personlib # to get global DB_DIR and JSON_INDENT

class Person:
    # constructor
    def __init__(self, name: str) -> None:
        self._name: str = name # given by user

        # other data set to None
        # chagned by user or via loading json-file
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
                birth_date_str = data.get("birth_date")
                self._birth_date = date.fromisoformat(birth_date_str) if birth_date_str else None

        else:
            self._save() # create empty new person with given name

    def _save(self) -> None:
        with open(self._filepath, "w") as file:
            json.dump({
                "name": self._name,
                "birth_date": self._birth_date.isoformat() if self._birth_date else None,
            }, file, indent=personlib.JSON_INDENT)

    def __str__(self) -> str:
        ''' return all information about the person '''
        return (
            f"Name: {self._name}\n"
            f"Birth Date: {self._birth_date}"
        )

    # name of person
    @property
    def name(self) -> Optional[str]:
        '''The name property.'''
        return self._name
    @name.setter
    def name(self, new_name: str) -> None: # return value is the exit code
        ''' change the name of the person '''

        if isinstance(new_name, str) and new_name.strip():
            old_filepath: str = self._filepath # save current filepath
            # create new file path with new name of person
            # don't save it yet in person object
            # because other person with same name/file already exists
            new_filepath: str = os.path.join(self._db_dir, f"{new_name.lower()}.json")

            if os.path.exists(new_filepath):
                # if the new filepath already exists
                # don't update the name and don't rename file
                raise Exception("A person with this name already exists")

            if os.path.exists(old_filepath):
                # update filepath for person
                self._name = new_name
                self._filepath = new_filepath

                # rename the old file to the new one
                # if no other already exists
                os.rename(old_filepath, new_filepath)

            # save the new name into the json file
            self._save()

        else:
            # if new name is not parsed as string
            raise ValueError("Name must be parsed as type string")

    # age of person
    @property
    def age(self) -> Optional[int]:
        ''' return the age of the person'''
        if self._birth_date == None:
            return None
        else:
            today: date = date.today() # get current date

            # substract birthdate from todays date
            # result is days since birth date
            # stored as datetime.timedelta
            age_days: timedelta = today - self._birth_date 

            # convert datetime.timedelta to integer representing days since birth date
            age: int = age_days.days

            # divide by 365 and use math.floor to get age of person
            age: int = floor(age / 365) 

            return age

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

