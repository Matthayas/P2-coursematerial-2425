# Write your code here
import re


def is_valid_email_address(string):
    if re.fullmatch(r"[a-z\d.]*@(student\.)?ucll\.be", string):
        return True
    return False