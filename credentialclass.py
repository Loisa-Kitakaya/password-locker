# create class


class Credentials:

    # database to store all user information
    profile_database = []

    """method to initialize profiles"""

    def __init__(self, account, profile_name, profile_password):

        self.account = account
        self.profile_name = profile_name
        self.profile_password = profile_password

    """method to save user information"""

    def save_user_profile(self):

        Credentials.profile_database.append(self)

    """method to delete user information"""

    def delete_user_profile(self):

        Credentials.profile_database.remove(self)

    """method to write list to a textfile"""

    def write_user_profile_to_file(self):

        # opening the file
        file = open("userprofile.txt", "w")

        file.write(str(Credentials.profile_database))

        # closing the file
        file.close()

    """method to read list from a text file"""

    def read_user_profile_from_file(self):

        # opening the file
        file = open("userprofile.txt", "r")

        file.readline()

        # closing the file
        file.close()
