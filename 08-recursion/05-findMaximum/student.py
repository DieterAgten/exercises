def findMaximum(list):
    if len(list) == 0:
        raise IndexError("List is leeg")
    elif len(list) == 1:
        return list[0]
    else:
        max_of_rest = findMaximum(list[1:])
        return list[0] if list[0] > max_of_rest else max_of_rest