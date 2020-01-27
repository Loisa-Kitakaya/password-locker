# create class
class Users(object):

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

        Users.user_database.clear(self)
