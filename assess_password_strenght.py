import string


def assess_password_strength(password):

    # define criteria for password strength
    length_criteria = 8  # minimum number of  characters in password

    # uppercase_criteria = 1  (minimum number of uppercase characters)
    # lowercase_minimum = 1 (minimum number of lowercase characters)
    # special_characters_minimum = 1 (minimum number of special characters)
    # number_criteria = 1 (minimum number of characters)

    # check password against criteria
    if len(password) < length_criteria:
        return "Weak Password: Password is too short"
    if not any(c.isupper() for c in password):
        return "Weak Password: no upper case character"
    if not any(c.islower() for c in password):
        return "Weak Password: no lower case character"
    if not any(c in string.punctuation for c in password):
        return "Weak Password: no special character"
    if not any(c.isdigit() for c in password):
        return "Weak Password: no number"

    # if all criteria are met password is strong
    return "All criteria met: Password is strong"


# get password from user
password = input("Enter Password to assess: ")

# assess password strength
strength = assess_password_strength(password)
print(strength, ":", password)
