# create class

class Credentials:

    # database to store all user information
    profile_database = []

    """method to initialize profiles"""

    def __init__(self, account, profile_name, profile_password):
        
        self.account = account
        self.profile_name = profile_name
        self.profile_password = profile_password