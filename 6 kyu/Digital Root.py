# My first solution

def digital_root(n: int) -> int:
    # If the result has more than one digit
    if len(str(n)) == 1:
        return n
    else:  
        total: int = 0
        # Convert the number to a string. 
        n = str(n)
        # Extract each character.
        for i in n:
            # Convert each character back to a number and sum them up.
            total += int(i)

        # If the result has more than one digit, recursively call the function.
        if len(str(total)) >= 2:
            return digital_root(total)
        else:
            return total


# For studying, I brought other clever solution

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
