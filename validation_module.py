import string

DIGITS = string.digits
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
SYMBOLS = "!§$%&?-_#*+/<>="

LENGTH = 6


def validate_password(pw, option):
    if len(pw) != LENGTH:
        return False

    if option == 1:
        return pw.isdigit()

    elif option == 2:
        return (sum(c.isdigit() for c in pw) == 4 and
                sum(c.islower() for c in pw) == 2 and
                pw.isalnum())

    elif option == 3:
        return (sum(c.islower() for c in pw) == 4 and
                sum(c.isdigit() for c in pw) == 2 and
                pw.isalnum())

    elif option == 4:
        return (sum(c.isdigit() for c in pw) == 4 and
                sum(c.isupper() for c in pw) == 1 and
                sum(c.islower() for c in pw) == 1)

    elif option == 5:
        allowed = DIGITS + LOWER + UPPER + SYMBOLS
        if not all(c in allowed for c in pw):
            return False
        return (any(c.isdigit() for c in pw) and
                any(c.islower() for c in pw) and
                any(c.isupper() for c in pw) and
                any(c in SYMBOLS for c in pw))

    return False