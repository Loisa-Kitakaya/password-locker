
import unittest
from credentialclass import Credentials

class TestForClassUsers(unittest.TestCase):

    """setting up our test"""

    def setUp(self):

        # creating an object instance of class users
        self.new_profile = Credentials("twitter", "loisaK", "loisa123")

    """testing if user profile can be saved"""

    def test_if_can_save(self):

        # run test case
        self.new_profile.save_user_profile("twitter", "loisaK", "loisa123")

        file = open("userprofiles.txt", "r")
        data = file.readline()

        self.assertEqual(data, "twitter-loisaK-loisa123\n")

        file.close()

    """testing to find user profile by account"""

    def test_if_can_find_profile(self):

        self.new_profile.save_user_profile("twitter", "loisaK", "loisa123")
        self.account_name = "twitter"
        file = open("userprofiles.txt", "r")
        data = file.read()

        self.assertTrue(data)

        file.close()

    """clean up after test"""

    def tearDown(self):

        # deleting our object instances
        Credentials.profile_database = []

if __name__ == "__main__":

    unittest.main()
