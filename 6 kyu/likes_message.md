## Description

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
### Examples
```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```
Note: For 4 or more names, the number in "and 2 others" simply increases.

\# Strings \# Fundamentals

# Solutions
1. I solved the problem using a **using the map function and lambda**.
2. But I found a more efficient and readable solution.
### 1. **String Formatting (f-strings) vs. Concatenation:**
   - **Original solution:** The original solution uses string concatenation with the + operator to build the final result. This can be inefficient because each concatenation creates a new string object, which can be slower, especially for large numbers of names.
   - **Improved solution:** The improved solution uses f-strings (formatted string literals), which are more efficient and easier to read. They are evaluated at runtime and are generally faster than string concatenation, as they don't require creating new string objects for each operation.

### 2. **Avoiding Unnecessary Variables:**
   - **Original solution:** In the original solution, you calculate the remains variable to handle the case where there are more than two names. This requires an additional variable (remains) and extra lines of code.
   - **Improved solution:** The improved solution directly uses counts_names - 2 in the formatted string, avoiding the need for an extra variable. This reduces the complexity and keeps the code shorter and cleaner.

I **compared the execution time** of my solution and the optimized solution using the performance measurement code.
![스크린샷 2025-03-19 101352](https://github.com/user-attachments/assets/b7d4dabc-d3c1-4f20-991f-c7079817db7d)
