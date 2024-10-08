def create_dictionary(keys, values):
    dictionary = {}
    for k,v in zip(keys, values):
        dictionary[k] = v
    return dictionary