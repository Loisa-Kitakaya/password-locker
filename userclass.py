# create class
class Users:

    # database to store all user information
    user_database = []

    """method to initialize users"""

    def __init__(self, user_name, user_password):

        self.user_name = user_name
        self.user_password = user_password

    """method to save user information"""

    def save_user_information(self):

        Users.user_database.append(self)

    """method to delete user information"""

    def delete_user_information(self):

        Users.user_database.remove(self)

    """method to write list to a textfile"""

    def write_user_info_to_file(self):

        # opening the file
        file = open("userinfo.txt", "w")

        file.write(str(Users.user_database))

        # closing the file
        file.close()

    """method to read list from a text file"""

    def read_user_info_from_file(self):

        # opening the file
        file = open("userinfo.txt", "r")

        file.readline()

        # closing the file
        file.close()
