# My first solution

def narcissistic( value ):
    if value == sum(map(lambda x: int(x) ** len(str(value)), str(value))):
        return True
    else:
        return False


# For studying, I brought other clever solution

def narcissistic(value):
    digits = str(value)
    length = len(digits)
    return value == sum(int(digit) ** length for digit in digits)
