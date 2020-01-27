import secrets
import string


class PasswordGenerator:

    """method to generate random password"""

    def generate_password():

        # variable to hold default initial password
        default = ""

        needs = string.ascii_letters + string.digits

        new_password = default.join(secrets.choice(needs) for length in range(10))

        return new_password
