import unittest

import personlib

import os
import shutil

class TestName(unittest.TestCase):

    def test_create_person(self) -> None:
        ''' test person creation '''

        p = personlib.Person("Creation") # create new person

        # check if file exists
        self.assertEqual(os.path.exists(os.path.join(personlib.DB_DIR,"creation.json")), True)

        # check if file does not exist
        self.assertNotEqual(os.path.exists(os.path.join(personlib.DB_DIR,
                                                        "notcreation.json")),
                            True)

    def test_get_name(self) -> None:
        ''' test name getter for person '''

        p = personlib.Person("NameGetter") # create new person

        self.assertEqual(p.name, "NameGetter")
        self.assertNotEqual(p.name, "NotNameGetter")

    def test_change_name(self) -> None:
        ''' test changing name of the person '''

        p = personlib.Person("NameChange") # create new person

        # check if name is right
        self.assertEqual(p.name, "NameChange")

        # check if file is right
        self.assertEqual(os.path.exists(os.path.join(personlib.DB_DIR,
                                                     "namechange.json")),
                         True)

        # change the name of the person
        p.name = "NameChangeDDD"

        # test if name got changed correctly
        self.assertNotEqual(p.name, "NameChange")
        self.assertEqual(p.name, "NameChangeDDD")
        self.assertNotEqual(p.name, "NameNotChanged")

        # test if the file was renamed correctly
        self.assertNotEqual(os.path.exists(os.path.join(personlib.DB_DIR,
                                                     "namechange.json")),
                         True)
        self.assertEqual(os.path.exists(os.path.join(personlib.DB_DIR,
                                                     "namechangeddd.json")),
                         True)
        self.assertNotEqual(os.path.exists(os.path.join(personlib.DB_DIR,
                                                     "namenotchanged.json")),
                         True)


if __name__ == "__main__":

    unittest.main()

