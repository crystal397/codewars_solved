# My first solution

def unique_in_order_old(sequence):
    if not sequence:  # Handle empty sequences
        return []

    result = [sequence[0]]  # Start with the first element
    for i in sequence[1:]:  # Start iterating from the second element
        if result[-1] != i:
            result.append(i)

    return result


# For studying, I brought other clever solution

from itertools import groupby

def unique_in_order_new(sequence):
    return [key for key, _ in groupby(sequence)]
