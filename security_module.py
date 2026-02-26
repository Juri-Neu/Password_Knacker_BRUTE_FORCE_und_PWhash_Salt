import hashlib
import os


def generate_salt(length=16):
    return os.urandom(length)


def hash_password(password, salt):
    data = salt + password.encode()
    return hashlib.sha256(data).hexdigest()


def verify_password(guess, salt, target_hash):
    guess_hash = hash_password(guess, salt)
    return guess_hash == target_hash