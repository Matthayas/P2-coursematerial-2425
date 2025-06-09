# Write your code here
import re


def is_valid_time(string):
    if re.fullmatch("\d\d:\d\d:\d\d(\.\d\d\d)?", string):
        return True
    return False