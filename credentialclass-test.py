# create test for class Users

# imports
import unittest
from credentialclass import Credentials

# create unittest subclass


class TestForClassUsers(unittest.TestCase):

    """setting up our test"""

    def setUp(self):

        # creating an object instance of class users
        self.new_profile = Credentials("twitter", "loisaK", "loisa123")

    """testing if user profile can be saved"""

    def test_if_can_save(self):

        # run test case
        self.new_profile.save_user_profile()
        self.assertEqual(len(Credentials.profile_database), 1)

    """clean up after test"""

    def tearDown(self):

        # deleting our object instances
        Credentials.profile_database = []


if __name__ == "__main__":

    unittest.main()
