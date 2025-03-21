## Description

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

\# StringsData \# Structures \# Fundamentals

# Solutions
1. I solved the problem by **using Counter**.
2. But I found a more efficient and readable solution.

### 1. **Code Length:**
- **Original:** Long and complex
- **Recommended:** Short and concise
- **Simplified:** Very short and concise

### 2. **Performance (Speed):**
- **Original:** Slow (O(n) + O(26) = O(n), inefficient due to use of Counter)
- **Recommended:** Fast (O(n) efficient set operations)
- **Simplified:** Fastest (O(n) using set operations)

### 3. **Performance (Memory):**
- **Original:** O(n) (uses two Counter objects)
- **Recommended:** O(n) (uses two sets)
- **Simplified:** O(n) (uses one set)

### 4. **Readability:**
- **Original:** Intuitive but a bit complex
- **Recommended:** Simple and clear
- **Simplified:** Very simple and intuitive

### 5. **Disadvantages:**
- **Original:** Inefficient and requires handling of duplicates
- **Recommended:** Doesn’t handle duplicate characters or cases where order matters
- **Simplified:** Doesn’t handle special characters outside of the alphabet

### 6. **Suitability:**
- **Original:** Good for when detailed processing or handling duplicates is required
- **Recommended:** Suitable when speed and efficiency are important
- **Simplified:** Best for when speed and simplicity are key, and order or duplicates aren’t important

**compared the execution time** of my solution and the optimized solution using the performance measurement code.
![image](https://github.com/user-attachments/assets/9797fcb3-8011-44b3-b4bb-aeca614c1e1a)

Here’s an explanation of the functions and concepts used in the expression `set(string.ascii_lowercase).issubset(st.lower())`:

### 1. **`set()` Function:**
   - The `set()` function in Python is used to create a set object. A set is an unordered collection of unique elements. In this context, `set()` is used to convert a sequence (like a string) into a set, automatically removing any duplicate characters.
   - For example, if you call `set('apple')`, the result would be `{'a', 'p', 'l', 'e'}`, which is a set containing the unique characters from the word "apple."

### 2. **`string.ascii_lowercase`:**
   - `string.ascii_lowercase` is a constant in Python’s `string` module. It provides a string that contains all lowercase letters in the alphabet from 'a' to 'z'.
   - This can be useful when you need to reference all the lowercase letters in the alphabet. For example, `string.ascii_lowercase` is equal to the string `'abcdefghijklmnopqrstuvwxyz'`.

### 3. **`st.lower()`:**
   - The `lower()` method is a built-in string method in Python. It converts all uppercase characters in a string to lowercase.
   - For instance, `'Hello'.lower()` would return `'hello'`, which is the lowercase version of the original string.
   - In this case, `st.lower()` converts the input string `st` to all lowercase characters, ensuring that the check is case-insensitive.

### 4. **`issubset()` Method:**
   - The `issubset()` method is used with set objects in Python. It checks if all the elements of one set are contained in another set.
   - For example, `set('abc').issubset(set('abcdef'))` would return `True`, because all elements of the first set are also present in the second set.
   - In the given expression, `set(string.ascii_lowercase).issubset(st.lower())` checks if all the lowercase alphabet letters (`a` to `z`) are present in the input string `st`, after converting it to lowercase.

### Putting it all together:

The expression `set(string.ascii_lowercase).issubset(st.lower())` can be broken down as follows:
- `set(string.ascii_lowercase)` creates a set containing all lowercase letters from 'a' to 'z'.
- `st.lower()` converts the input string `st` to all lowercase characters.
- `issubset()` checks if all characters in the alphabet (from `string.ascii_lowercase`) are present in the string `st`.

If the input string `st` contains every letter of the alphabet at least once (ignoring case), `issubset()` will return `True`, indicating that the string is a **pangram** (a sentence that contains every letter of the alphabet). If any letter is missing, it will return `False`.

### Example:

```python
import string

def is_pangram(st):
    return set(string.ascii_lowercase).issubset(st.lower())

# Test cases
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello World"))  # False
```

In this case:
- The first sentence contains all 26 letters of the alphabet, so the function returns `True`.
- The second sentence does not contain all the letters, so the function returns `False`.
