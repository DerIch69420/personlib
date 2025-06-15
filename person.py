import json  # json handling
import os  # check if files already exist
from typing import Optional


class Person:
    def __init__(self, name: str) -> None:
        self._name: str = name  # name given with init
        self._age: Optional[int] = None

        # get filepath via name of person
        self._filepath: str = f"db/{self._name.lower()}.json"
        self._load_or_init()

    def _load_or_init(self) -> None:
        if os.path.exists(self._filepath):
            # get attributes of person from json file
            with open(self._filepath, "r") as file:
                data = json.load(file)
                self.age = data.get("age")
        else:
            self._save()

    def _save(self) -> None:
        # save the data about the person in a json file
        with open(self._filepath, "w") as file:
            json.dump({
                "name": self._name,
                "age": self._age,
            }, file, indent=4)

    def __str__(self) -> str:
        # print attributes of the person
        return (
            f"Name: {self._name}\n"
            f"Age: {self._age}\n"
        )

    @property
    def age(self) -> Optional[int]:
        return self._age

    @age.setter
    def age(self, value: Optional[int]) -> None:
        if value is None or (isinstance(value, int) and value >= 0):
            self._age = value
            self._save()
        else:
            raise ValueError("Age must be a non-negative integer or None")

    def change_name(self, new_name: str) -> None:
        if isinstance(new_name, str) and new_name.strip():
            # change name and also filepath
            old_filepath = self._filepath
            self._name = new_name
            self._filepath = f"db/{self._name.lower()}.json"
            if os.path.exists(old_filepath):
                os.rename(old_filepath, self._filepath)
            self._save()

    def have_birthday(self) -> None:
        if self._age is None:
            self._age = 1
        else:
            self._age += 1
        self._save()

