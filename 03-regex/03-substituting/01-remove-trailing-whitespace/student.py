import re

def remove_trailing_whitespace(string):
    return re.sub(r'\s+$', '', string, flags = re.MULTILINE)

"""
\s = witruimte (spatie, tab, nieuwe regels)
+ = 1 of meerdere keren witruimte
$ = vanaf het einde string
flags = re.MULTILINE = Regex op het einde van elke regel ipv op het einde van de string
"""