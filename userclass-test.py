# create test for class Users

# imports
import unittest
from userclass import Users

# create unittest subclass


class TestForClassUsers(unittest.TestCase):

    """setting up our test"""

    def setUp(self):

        # creating an object instance of class users
        self.new_user = Users("Loisa", "loisa123")

    """testing if user profile can be saved"""

    def test_if_can_save(self):

        # run test case
        self.new_user.save_user_information()
        self.assertEqual(len(Users.user_database), 1)

    """testing if user profile can be deleted"""

    def test_if_can_delete(self):

        # run test case
        self.new_user.save_user_information()
        self.new_user.delete_user_information()
        self.assertEqual(len(Users.user_database), 0)

    """clean up after test"""

    def tearDown(self):

        # deleting our object instances
        Users.user_database = []


if __name__ == "__main__":

    unittest.main()
