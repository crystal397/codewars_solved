# My first solution

def likes_old(names):
    counts_names = len(names)
    remains = counts_names - 2
    if counts_names == 0:
        return "no one likes this"
    elif counts_names == 1:
        return names[0] + " likes this"
    elif counts_names == 2:
        return names[0] + " and " + names[1] + " like this"
    elif counts_names == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(remains) + " others like this"


# For studying, I brought other clever solution

def likes_new(names):
    counts_names = len(names)
    if counts_names == 0:
        return "no one likes this"
    elif counts_names == 1:
        return f"{names[0]} likes this"
    elif counts_names == 2:
        return f"{names[0]} and {names[1]} like this"
    elif counts_names == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {counts_names - 2} others like this"
