def sum(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply (x, y):
    return x*y

def divide(x, y):
    if y == 0:
        raise ValueError("0val nem oszthatsz")
    return x / y