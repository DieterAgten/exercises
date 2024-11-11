from util import *

def count_older_than(people, min_age):
    def is_older(person):
        return person.age >= min_age
    return count(people, is_older)