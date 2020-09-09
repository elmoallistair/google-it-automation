#!/usr/bin/env python3

def validate_user(username, minlen):
    if type(username) != str:
        raise TypeError("username must be a string")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    # Username can't begin with a number
    if username[0].isnumeric():
        return False
    return True