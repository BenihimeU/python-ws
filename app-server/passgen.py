import random
import string
import secrets
import uuid

# random string generator lowercases
# string.choice -- picks same member
def randomString(len=8, isLower=False):
    if (isLower):
        letters = string.ascii_lowercase
    else:
        letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(len))

# random string generator from phrase
def randomStringFromPhrase(len=8, isLower=False):
    #Need pass the phrase secret key
    letters = 'abcdefzyxwv'
    return ''.join(random.choice(letters) for i in range(len))

# random string generator
# string.sample -- picks unique member
def randomStringFromUnique(length=8, isLower=False):
    #Need pass the phrase secret key
    letters = string.ascii_letters
    return ''.join(random.sample(letters, length))

# random string generator
# string.sample -- picks unique member
def randomAlphaNumeric(length=8, isLower=False):
    #Need pass the phrase secret key
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# random secret generator not duplicate
# string.printable
def randomSecureString(length=8):
    #Need pass the phrase secret key
    return ''.join(secrets.choice(string.ascii_lowercase) for i in range(length))

#using secret library
print('secret library :', secrets.token_hex(32))

#using uuid library
print('secret library :', uuid.uuid4())
