# Write your code here
import re


def starts_with_a(string):
    if re.match("a", string):
        return True
    return False