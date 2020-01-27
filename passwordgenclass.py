# make imports
import secrets
import string

# create class
class PasswordGenerator:

    """method to generate random password"""

    def generate_password(self):

        # variable to hold default initial password
        default = ""

        needs = string.ascii_letters + string.digits

        new_password = default.join(secrets.choice(needs) for length in range(10))
