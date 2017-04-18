def data_type(n):
    if isinstance(n, str):
        return len(n)
    elif n == None:
        return "no value"
    elif isinstance(n, bool):
        return n
    elif isinstance(n, int):
        if n < 100:
            return "less than 100"
        elif n == 100:
            return "equal to 100"
        else:
            return "more than 100"
    elif isinstance(n, list):
        if len(n) >= 3:
            return n[2]
        else:
            return None
