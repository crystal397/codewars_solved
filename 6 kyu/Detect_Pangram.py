# Original method (Counter-based)
from collections import Counter
def is_pangram_old(st):
    all = Counter(string.ascii_lowercase) - Counter(st.lower())
    return False if any(v == 1 for v in all.values()) else True

# My recommended method (Set-based)
def is_pangram_new(st):
    st_set = set(st.lower())
    alphabet_set = set(string.ascii_lowercase)
    return alphabet_set <= st_set

# Simplified method (Another Set-based)
def is_pangram_simple(st):
    return set(string.ascii_lowercase).issubset(st.lower())
