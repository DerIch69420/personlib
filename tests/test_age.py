import unittest

import personlib
from datetime import date
from math import floor

class TestAge(unittest.TestCase):

    def test_birth_date_none(self) -> None:
        ''' test setting date of birth to None on creation '''

        p = personlib.Person("BirthDateNone") # create new person

        self.assertEqual(p.age, None) # check if no birth date is set
 
    def test_birth_date_change(self) -> None:
        ''' test date of birth change '''

        p = personlib.Person("BirthDateChange") # create new person

        p.birth_date = date(2010, 7, 24) # change birth date of person

        self.assertEqual(p.birth_date, date(2010, 7, 24))
        self.assertNotEqual(p.birth_date, date(2010, 6, 10))

    def test_age(self) -> None:
        ''' test getting age of person '''

        p = personlib.Person("Age") # create new Person
        p.birth_date = date(2010, 12, 24) # change birth date of person
        today = date.today() # get today's date
        # calculate age of person
        age: int = floor((today - date(2010, 12, 24)).days / 365)

        # check if calculated age and the one from the person are equal
        self.assertEqual(p.age, age)
        self.assertNotEqual(p.age, age -1)

    def test_age_none(self) -> None:
        ''' test getting age equal to None if birth date not set '''

        p = personlib.Person("AgeNone") # create new person
        
        # don't set birth date so age getter will return None
        self.assertEqual(p.age, None)

if __name__ == "__main__":
    unittest.main()
