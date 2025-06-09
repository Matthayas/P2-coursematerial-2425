# Write your code here
import re


def remove_trailing_whitespace(string):
    new_string = re.sub(r"\s+$", "", string, flags=re.MULTILINE)
    return new_string
