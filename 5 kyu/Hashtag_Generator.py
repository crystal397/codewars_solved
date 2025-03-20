# My first solution

def generate_hashtag_old(s):
    splitS = s.split()
    splitS = [i.capitalize() for i in splitS]
    joinS = ''.join(splitS)
    lenS = len(joinS)
    if not lenS or lenS >= 140:
        return False
    else:
        return '#' + joinS


# For studying, I brought other clever solution

def generate_hashtag_new(s):
    # Strip leading/trailing spaces and handle edge case where string is empty
    stripped_s = s.strip()

    # If string is empty after stripping or too long, return False
    if not stripped_s or len(stripped_s) + 1 > 140:
        return False

    # Capitalize each word and join them into a single string, with '#' at the start
    return '#' + ''.join(word.capitalize() for word in stripped_s.split())
