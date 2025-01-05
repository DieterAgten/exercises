def fibonacci(nummer):
    if nummer <= 0:
        return 0
    elif nummer == 1:
        return 1
    else:
        return fibonacci(nummer-1) + fibonacci(nummer-2)