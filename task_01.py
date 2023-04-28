import re

exception_str = ",. !;:"
alphavit = set("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")


def is_palindrome(input_data):
    if input_data is None:
        return False
    input_data = str(input_data)
    input_data = ''.join(filter(alphavit.__contains__, input_data)).lower()
    revere_str = input_data[::-1]
    if revere_str == input_data:
        return True
    else:
        return False



