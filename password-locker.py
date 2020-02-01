#!/usr/bin/env python3

# imports
import getpass
import time
import os
from userclass import Users
from credentialclass import Credentials
from passwordgenclass import PasswordGenerator

# class PasswordLocker
class PasswordLocker:

    # main app welcome function
    def welcome():

        print("\nLoading...")
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

    # main app login function
    def account_login():

        print("\nLoading...")
        time.sleep(2)

        os.system("clear")

        print("\nWelcome back!")
        print("Enter your details to login...")

        user_name = input("\nuser_name >>> ")
        user_password = getpass.getpass(
            prompt="\nuser_password >>> ")

        file = open("userinfo.txt", "r")
        data = file.readline()

        file.close()

        if user_name in data and user_password in data:

            PasswordLocker.profile_manager()

        else:

            print("\nWrong credentials! Try again...")

    # main app signin funcion
    def account_signin():

        print("\nLoading...")
        time.sleep(2)

        os.system("clear")

        print("\nDon't have an account yet?")
        print("Enter a username for your new account.")
        user_name = input("\nuser_name >>> ")

        print("\nDo you want a generated password? \ny: Yes \nn: No")
        answer = input("\nanswer? >>> ")

        # condition if
        if answer == "y":

            user_password = PasswordGenerator.generate_password()

            # print("\nYour generated password is: " + user_password)

        elif answer == "n":

            print("\nEnter a password for your new account.")
            user_password = input("\nuser_password >>> ")

        else:

            print("\nPlease enter valid options!")

        new_user = Users(user_name, user_password)
        new_user.save_user_information()

        print("your username: " + user_name + "\nYour password: " + user_password)

    # profile manager welcome function
    def profile_manager_welcome():

        print("\nLoading...")
        time.sleep(2)

        os.system("clear")

        print(
            "\nCreate profile for your online accounts. \nOr view already saved profiles."
        )

        print("")
        print("Profile menu!")
        print("-------------")
        print("1: create new profile \n2: view profiles \nx: Exit")

    # create profile function
    def create_profile():

        print(
            "\nCreate a profile by answering the following questions: \nWhat account does this profile belong to? \nWhat is the username for this account? \nWhat is the password for this account?"
        )

        account = input("\naccount >>> ")
        account_username = input("\naccount_username >>> ")

        print(
            "\nDo you want a generated password? \ny: Yes \nn: No"
        )
        answer = input("\nanswer? >>> ")

        # condition if
        if answer == "y":

            account_password = PasswordGenerator.generate_password()

        elif answer == "n":

            print(
                "\nEnter a password for your new account.")
            account_password = getpass.getpass(
                prompt="\n account_password >>> "
            )

        else:

            print("\nPlease enter valid options!")

        new_cred = Credentials(
            account, account_username, account_password
        )
        new_cred.save_user_profile()

        print("Profile for: " + "\n\naccount = " + account + "\n\nusername = " + account_username + "\n\npassword = " + account_password)

    # find profile function
    def find_profile():

        print("\nFind your profiles? \ny: Yes \nn: No")

        profile_find = input("\nfind_profile? >>> ")

        if profile_find == "y":

            view_profile = Credentials.view_user_profile(profile_find)

            print("")
            print("Your saved profiles: \n")
            print(view_profile)

        else:

            pass

    # profile manager main function
    def profile_manager():

        while True:

            PasswordLocker.profile_manager_welcome()

            answer = input("\nprofilemanager >>> ")

            if answer == "1":

                while True:

                    PasswordLocker.create_profile()

                    continue_browse = input("\ncontinue? | any key then hit 'Enter' >>> ")

                    if continue_browse == True:

                        break

                    break

            elif answer == "2":

                while True:

                    PasswordLocker.find_profile()

                    continue_browse = input("\ncontinue? | any key then hit 'Enter' >>> ")

                    if continue_browse == True:

                        break

                    break

            elif answer == "x":

                break

            else:

                print("\nPlease enter valid menu options!")

            continue

    # main app function
    def main():

        while True:

            PasswordLocker.welcome()

            # take user input
            begin = input("\npasswordlocker >>> ")

            # condition if
            if begin == "1":

                while True:

                    PasswordLocker.account_login()

                    continue_browse = input("\ncontinue? | any key then hit 'Enter' >>> ")

                    if continue_browse == True:

                        break

                    break

            elif begin == "2":

                while True:

                    PasswordLocker.account_signin()

                    continue_browse = input("\ncontinue? | any key then hit 'Enter' >>> ")

                    if continue_browse == True:

                        break

                    break

            elif begin == "x":

                break

            else:

                print("\nPlease enter valid menu options!")

            continue


# calling the main app function
PasswordLocker.main()
