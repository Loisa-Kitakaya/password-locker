# create test for class PasswordGenerator

# imports
import unittest
from passwordgenclass import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    def test_password_generator(self):

        self.profile_password = PasswordGenerator.generate_password()

        print(self.profile_password)


if __name__ == "__main__":
    unittest.main()
