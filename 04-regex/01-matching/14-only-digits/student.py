# Write your code here
import re


def only_digits(string):
    if re.fullmatch("[0123456789]*", string):
        return True
    return False