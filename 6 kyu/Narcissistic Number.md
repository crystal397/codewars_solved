## Description

A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

### Examples

For example, take 153 (3 digits), which is narcissistic:
```
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```
and 1652 (4 digits), which isn't:
```
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
```
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

\# Algorithms

# Solutions
1. I solved the problem using a **using the map function and lambda**.
2. But I found a more efficient and readable solution.
### 1. **Avoiding Repeated Function Calls:**
   - **Original solution:** In the original code, `len(str(value))` is called multiple times. The length of the number is calculated repeatedly for each digit inside the `map()` function and the `lambda` function. This is inefficient because the same length is being calculated multiple times, which increases the execution time slightly, especially for larger numbers.   
   - **Improved solution:** The improved version calculates `len(str(value))` just once and stores it in the `length` variable. This eliminates redundant calculations, making the code more efficient.

### 2. **List Comprehension vs. `map()` and `lambda`:**
   - **Original solution:** The original code uses `map()` along with `lambda`, which is functional and concise but can be less intuitive for some developers. While `map()` is an efficient tool for applying a function to each item in an iterable, it's not as optimized for performance as list comprehensions in Python.
   - **Improved solution:** The list comprehension approach is more Pythonic and is generally faster for this kind of task. List comprehensions are optimized for iterating over sequences and creating lists, and they tend to be faster and more readable compared to using `map()` with `lambda` for simple operations.

### 3. **Readability and Simplicity:**
   - **Original solution:** Using `map()` and `lambda` can be concise, but it might be harder to follow for someone unfamiliar with these functional programming tools. It requires the reader to understand the `lambda` function and how `map()` works, which may reduce readability.
   - **Improved solution:** List comprehensions are generally easier to understand at a glance. They provide a clear, one-liner solution to process each digit, making the code more readable and easier to maintain. This is especially important in team projects or when sharing code with others.

I **compared the execution time** of my solution and the optimized solution using the performance measurement code.
![image](https://github.com/user-attachments/assets/8abfa160-fd06-4de9-a678-fc01ee1748a5)
