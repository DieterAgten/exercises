def countX(text):
    if not text:
        return 0
    else:
        first_is_x =1 if text[0] == "x" else 0
    return first_is_x + countX(text[1:])