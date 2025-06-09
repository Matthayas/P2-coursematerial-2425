# Write your code here
import re


def is_valid_password(string):
    if re.fullmatch(r"(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[+\-*/.@])(?!.*(.)\1\1)(?!.*(.).*\2.*\2.*\2).{12,}", string):
        return True
    return False