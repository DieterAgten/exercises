import re

def remove_repeated_words(string):
    return re.sub(r'(\b[a-zA-Z]+\b)( \1)+', r'\1', string)

"""
\b = woordgrens
(...) zet woord in een groep (1 of meerdere letters)
( \1) = Herhaald het woord, voorafgegaan door een spatie
r'\1' = De dubbele woorden worden vervangen door 1 woord, voorafgegaan door een spatie
"""