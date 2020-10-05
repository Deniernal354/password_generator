# == START OF PROGRAM DETAILS == #
###
#   NAME: PASSWORD GENERATOR
#   SHORT_DISC: Write a programme, which generates a random password for the user.
#   Ask the user how long they want their password to be, and how many letters and numbers they want in their password.
#   Have a mix of upper and lowercase letters, as well as numbers and symbols.
#   The password should be a minimum of 6 characters long.
#   PARAMS: stringLength - INT EX: 6 | chars - METHOD EX: string.ascii_letters
#   LIBRARIES/DEPENDENCIES: string and secrets
###
# == END OF PROGRAM DETAILS == #

# == VALIDATION ==
#   - Length isn't less than 6 characters >==> DONE
# == VALIDATION ==

import string, secrets, random

length_of_password = int(input("How long is the password? "))
letterCount = int(input("How many letters? "))  # Max is 52
numberCount = int(input("How many numbers? "))  # Max is 52

while (length_of_password - letterCount - numberCount) or (length_of_password - numberCount - letterCount) != 0:
    print("Invalid input, letter or number count is invalid!")
    letterCount = int(input("How many letters? "))  # Max is 52
    numberCount = int(input("How many numbers? "))  # Max is 52

chars = random.sample(string.ascii_letters, letterCount) + random.sample(string.digits, numberCount) + random.sample(
    string.punctuation, length_of_password)

while length_of_password < 6:
    print("Invalid input, password length too short!")
    lenOfPass = int(input("How long is the password? "))


def password_generator(string_length=length_of_password):
    return ''.join(secrets.choice(chars) for _ in range(string_length))


print(f"Your random password: {password_generator()}")
