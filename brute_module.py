import itertools
import string
import time
from validation_module import LENGTH
from security_module import verify_password

DIGITS = string.digits
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
SYMBOLS = "!§$%&?-_#*+/<>="


def show_menu():
    print("=== Brute Force Demo (6 Zeichen) ===")
    print("1: Nur Zahlen")
    print("2: 4 Zahlen + 2 kleine Buchstaben")
    print("3: 4 kleine Buchstaben + 2 Zahlen")
    print("4: 4 Zahlen + 1 Groß + 1 Klein")
    print("5: Mind. Zahl, klein, groß, Symbol")
    return int(input("Auswahl: "))


def show_mode_menu():
    print("\nModus wählen:")
    print("1: Plaintext Vergleich")
    print("2: Realistisch (SHA-256 + Salt)")
    return int(input("Modus: "))


# Regelchecks
def rule_option_2(pw):
    return sum(c.isdigit() for c in pw) == 4 and sum(c.islower() for c in pw) == 2

def rule_option_3(pw):
    return sum(c.islower() for c in pw) == 4 and sum(c.isdigit() for c in pw) == 2

def rule_option_4(pw):
    return (sum(c.isdigit() for c in pw) == 4 and
            sum(c.isupper() for c in pw) == 1 and
            sum(c.islower() for c in pw) == 1)

def rule_option_5(pw):
    return (any(c.isdigit() for c in pw) and
            any(c.islower() for c in pw) and
            any(c.isupper() for c in pw) and
            any(c in SYMBOLS for c in pw))


def get_charset_and_rule(option):
    if option == 1:
        return DIGITS, None
    elif option == 2:
        return DIGITS + LOWER, rule_option_2
    elif option == 3:
        return DIGITS + LOWER, rule_option_3
    elif option == 4:
        return DIGITS + LOWER + UPPER, rule_option_4
    elif option == 5:
        return DIGITS + LOWER + UPPER + SYMBOLS, rule_option_5
    else:
        return None, None


# Gesamtanzahl Kombinationen (für %)
def estimate_total(charset):
    return len(charset) ** LENGTH


def brute_force_plain(target, charset, rule=None):
    total = estimate_total(charset)
    start = time.time()
    attempts = 0

    for combo in itertools.product(charset, repeat=LENGTH):
        guess = ''.join(combo)
        attempts += 1

        if rule and not rule(guess):
            continue

        if attempts % 50000 == 0:
            elapsed = time.time() - start
            speed = attempts / elapsed if elapsed > 0 else 0
            percent = (attempts / total) * 100
            print(f"\r{percent:.2f}% | {speed:.0f} Versuche/s", end="")

        if guess == target:
            duration = time.time() - start
            print()
            return attempts, duration

    return attempts, None


def brute_force_hash(target_hash, salt, charset, rule=None):
    total = estimate_total(charset)
    start = time.time()
    attempts = 0

    for combo in itertools.product(charset, repeat=LENGTH):
        guess = ''.join(combo)
        attempts += 1

        if rule and not rule(guess):
            continue

        if attempts % 50000 == 0:
            elapsed = time.time() - start
            speed = attempts / elapsed if elapsed > 0 else 0
            percent = (attempts / total) * 100
            print(f"\r{percent:.2f}% | {speed:.0f} Versuche/s", end="")

        if verify_password(guess, salt, target_hash):
            duration = time.time() - start
            print()
            return attempts, duration

    return attempts, None