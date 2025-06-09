# Write your code here
import re


def only_vowels(string):
    if re.fullmatch("[aeuioAEUIO]*", string):
        return True
    return False