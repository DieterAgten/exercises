import re

def is_valid_password(string):
    positiveregex = [
        r".{12,}",
        r"[a-z]",
        r"[A-Z]",
        r"[0-9]",
        r"[-+/.*@]",
    ]

    negativeregex = [
        r"(.)\1{2}",
        r"(.)(.*\1){3}",
    ]

    for regex in positiveregex:
        if not re.search(regex, string):
            return False
    
    for regex in negativeregex:
        if re.search(regex, string):
            return False
    
    return True