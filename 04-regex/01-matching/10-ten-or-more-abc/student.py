# Write your code here
import re


def ten_or_more_abc(string):
    if re.fullmatch("(abc){10,}", string):
        return True
    return False
