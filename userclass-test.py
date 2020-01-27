import unittest
from userclass import Users


class TestForClassUsers(unittest.TestCase):

    """setting up our test"""

    def setUp(self):

        # creating an object instance of class users
        self.new_user = Users("Loisa", "loisa123")

    """testing if user profile can be saved"""

    def test_if_can_save(self):

        # run test case
        self.new_user.save_user_information()

        file = open("userinfo.txt", "r")
        data = file.readline()

        self.assertEqual(data, "Loisa-loisa123")

        file.close()

    """clean up after test"""

    def tearDown(self):

        # deleting our object instances
        Users.user_database = []


if __name__ == "__main__":

    unittest.main()
