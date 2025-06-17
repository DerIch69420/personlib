import unittest

import personlib

import os
import shutil

class TestDatabase(unittest.TestCase):

    def test__db(self) -> None:

        p = personlib.Person("Placeholder") # create new person

        self.assertEqual(os.path.exists(personlib.DB_DIR), True)
        self.assertEqual(os.path.exists("db"), True)


if __name__ == "__main__":

    unittest.main()
