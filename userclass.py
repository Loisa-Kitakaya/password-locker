class Users:

    user_database = []

    """method to initialize users"""

    def __init__(self, user_name, user_password):

        self.user_name = user_name
        self.user_password = user_password

    """method to save user information"""

    def save_user_information(self):

        file = open("userinfo.txt", "w+")
        file.write(self.user_name + "-" + self.user_password)
        file.close()

    """method to view user information"""

    def view_user_information(self):

        file = open("userinfo.txt", "r")
        data = file.readline()

        file.close()

        return data

