from src.utils import is_numeric

def sum(*args):
    """do summation"""
    result = 0
    for num in args:
        if is_numeric(num):
            result += num
        else:
            return None
    return result


def sub(*args):
    """do subtraction"""
    result = args[0]
    if not is_numeric(result):
        return None
    for num in args[1:]:
        if is_numeric(num):
            result -= num
        else:
            return None
    return result


def multiply(*args):
    """do multiplication
"""
    result = args[0]
    if not is_numeric(result):
        return None
    for num in args[1:]:
        if is_numeric(num):
            result *= num
        else:
            return None
    return result


def divide(*args):
    """do division"""
    result = args[0]
    if not is_numeric(result):
        return None
    for num in args[1:]:
        if is_numeric(num):
            result /= num
        else:
            return None
    return result
    

if __name__ == "__main__":
    print(sum(1, 2, 3))
    print(sub(1, 2, 3))
    print(multiply(1, 2, 3))
    print(divide(1, 2, 3))
