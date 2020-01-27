import getpass
import time
import os
from userclass import Users
from credentialclass import Credentials
from passwordgenclass import PasswordGenerator


class PasswordLocker:
    def main():

        while True:

            print("Loading...")
            time.sleep(2)

            """Welcome messages"""
            os.system("clear")

            print("\nWELCOME TO PASSWORD-LOCKER!")
            print("A safe place for all your online profiles")

            print(
                "\nLogin if you already have a password-locker account. \nSign up if you wish to use password-locker."
            )

            print("")
            print("Main menu!")
            print("----------")
            print("1: Login \n2: SignUp \nx: Exit")

            """Begin"""

            # take user input
            begin = input("\nPasswordLocker>>> ")

            # condition if
            if begin == "1":

                print("Loading...")
                time.sleep(2)

                os.system("clear")

                print("\nWelcome back!")
                print("Enter your details to login...")

                user_name = input("\nuser_name>>> ")
                user_password = getpass.getpass(prompt="\nuser_password>>> ")

                file = open("userinfo.txt", "r")
                data = file.readline()

                file.close()

                if user_name in data and user_password in data:

                    print("Loading...")
                    time.sleep(2)

                    os.system("clear")

                    while True:

                        print(
                            "\nCreate profile for your online accounts. \nOr view already saved profiles."
                        )

                        print("")
                        print("Profile menu!")
                        print("-------------")
                        print("1: view profiles \n2: create new profile \nx: Exit")

                        answer = input("\nProfileManager>>> ")

                        if answer == "1":
                            print("\nFind your profiles? \ny: Yes \nn: No")

                            profile_find = input("\nprofile_find>>> ")

                            if profile_find == "y":

                                view_profile = Credentials.view_user_profile(
                                    profile_find
                                )
                                print("")
                                print(view_profile)

                            else:
                                pass

                            continue

                        elif answer == "2":

                            print(
                                "\nCreate a profile by answering the following questions: \nWhat account does this profile belong to? \nWhat is the username for this account? \nWhat is the password for this account?"
                            )

                            account = input("\naccount>>> ")
                            profile_name = input("\nprofile_name>>> ")

                            print(
                                "\nDo you want a generated password? \ny: Yes \nn: No"
                            )
                            answer = input("\nanswer>>> ")

                            # condition if
                            if answer == "y":
                                profile_password = PasswordGenerator.generate_password()

                                print(
                                    "\nYour generated password is: " + profile_password
                                )
                            elif answer == "n":
                                print("\nEnter a password for your new account.")
                                profile_password = getpass.getpass(
                                    prompt="\nprofile_password>>> "
                                )
                            else:
                                print("\nPlease enter valid options!")

                            new_cred = Credentials(
                                account, profile_name, profile_password
                            )
                            new_cred.save_user_profile()

                            continue

                        elif answer == "x":
                            break

                        else:
                            print("\nPlease enter valid menu options!")

                            continue

                else:
                    print("\nWrong credentials! Try again...")
                    continue

            elif begin == "2":

                print("Loading...")
                time.sleep(2)

                os.system("clear")

                print("\nDon't have an account yet?")
                print("Enter a username for your new account.")
                user_name = input("\nuser_name>>> ")

                print("\nDo you want a generated password? \ny: Yes \nn: No")
                answer = input("\nanswer>>> ")

                # condition if
                if answer == "y":
                    user_password = PasswordGenerator.generate_password()

                    print("\nYour generated password is: " + user_password)
                elif answer == "n":
                    print("\nEnter a password for your new account.")
                    user_password = getpass.getpass(prompt="\nuser_password>>> ")
                else:
                    print("\nPlease enter valid options!")

                new_user = Users(user_name, user_password)
                new_user.save_user_information()

                continue

            elif begin == "x":
                break

            else:
                print("\nPlease enter valid menu options!")

                continue


PasswordLocker.main()
