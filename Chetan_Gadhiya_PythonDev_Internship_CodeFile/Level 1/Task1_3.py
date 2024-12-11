# Email Valodator
import re


def email_validator(email):

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_regex, email):
        print("Entered Address is valid Email Address.")
    else:
        print("Entered Address is Invalid Email Address.")


emailEnter = input("Enter an Email Address : ")
email_validator(emailEnter)
