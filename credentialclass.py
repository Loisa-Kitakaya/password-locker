import re


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

        file = open("userprofiles.txt", "a+")

        file.write(" | ")
        file.write(
            self.account
            + " - "
            + self.account
            + " username: "
            + self.profile_name
            + " - "
            + self.account
            + " password: "
            + self.profile_password
        )
        file.write(" | ")

        file.close()

    """method to view user information"""

    def view_user_profile(self):

        file = open("userprofiles.txt", "r")
        data = file.readline()

        file.close()

        return data

    """method to view user profiles based on account"""

    def view_user_profile_on_account(self, account_name):

        self.account_name = account_name

        try:
            file = open("userprofiles.txt", "r")
            data = file.read()

            for search in data.split():

                if self.account_name in search:

                    return search

            file.close()

        except FileNotFoundError:
            show = "No such file or directory!"
            return show

        else:
            show = "No such file or directory!"
            return show
