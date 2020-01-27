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

    """testing if user profile can be deleted"""

    def test_if_can_delete(self):

        # run test case
        self.new_profile.save_user_profile()
        self.new_profile.delete_user_profile()
        self.assertEqual(len(Credentials.profile_database), 0)

    """testing if can write user profile to text file"""

    def test_if_can_write_file(self):

        # run test case
        self.new_profile.save_user_profile()
        self.new_profile.write_user_profile_to_file()

        # open file
        file = open("userprofile.txt", "r")

        entry = file.readline()

        print(entry)

        # close file
        file.close()

    """testing if can read user profile from text file"""

    def test_if_can_read_file(self):

        # run test case
        self.new_profile.save_user_profile()
        self.new_profile.write_user_profile_to_file()

        # open file
        file = open("userprofile.txt", "r")

        entry = file.readline()
        word_in_entry = entry.split()

        for word in word_in_entry:

            if word == "twitter" or word == "loisaK" or word == "loisa123":

                return word
            else:

                break

        # close file
        file.close()

    """clean up after test"""

    def tearDown(self):

        # deleting our object instances
        Credentials.profile_database = []


if __name__ == "__main__":

    unittest.main()
