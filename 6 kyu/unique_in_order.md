## Description

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

### For example:
```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
```
\# Algorithms \# Fundamentals

# Solutions
1. I solved the problem using a **using manual iteration and condition checking**.
2. But I found a more efficient and readable solution.
### 1. **Using Manual Iteration vs. Using `groupby` for Grouping Consecutive Duplicates:**
- **Original solution:** The original solution manually iterates through the sequence, starting from the second element and checking whether the current element is different from the last one in the `result` list. If it is different, it appends the element to the result. This works but requires more manual logic and can be less efficient for large sequences.
- **Improved solution:** The improved solution uses Python’s `itertools.groupby()` function, which groups consecutive duplicate elements in the sequence automatically. This simplifies the code and improves its readability and efficiency by abstracting away the manual iteration logic.

### 2. **Manual Checking for Duplicates vs. Using `groupby`:**
- **Original solution:** In the original solution, you manually check if the current element (`i`) is the same as the last element in the result list (`result[-1]`). If they are the same, you skip appending it, and if they are different, you append it to the result. This involves additional conditionals and comparisons, which can be less efficient, especially with large lists.
- **Improved solution:** The improved solution leverages `groupby()`, which inherently handles the grouping of consecutive duplicates and eliminates the need for manual comparisons. This reduces both the amount of code and the complexity, making the solution cleaner and more efficient.

### 3. **Manual List Slicing vs. Using Efficient Iteration:**
- **Original solution:** The original solution uses list slicing (`sequence[1:]`) in order to skip the first element and start iterating from the second one. This creates a new list in memory for every slice, which can be inefficient in terms of both time and space.
- **Improved solution:** The improved solution directly iterates over the sequence without any slicing, making it more memory-efficient and reducing unnecessary copying of the sequence.

### 4. **Handling Empty Lists Manually vs. Simplified Approach:**
- **Original solution:** The original solution explicitly checks for an empty sequence using `if not sequence`, and if the sequence is empty, it returns an empty list. This is a straightforward and valid way of handling the case but introduces an extra conditional check.
- **Improved solution:** The improved solution uses `groupby()` directly, which handles the empty list case by returning an empty list when no groups are found. This removes the need for an explicit empty sequence check and keeps the code more streamlined.

### 5. **Iterating Over Entire Sequence vs. Efficient Grouping:**
- **Original solution:** The original solution iterates over the entire sequence and adds elements to a new list only if they are different from the last element in the result. This results in additional iterations and checks, which could slow down the function for larger sequences.
- **Improved solution:** The improved solution uses `groupby()`, which groups consecutive identical elements together. This is more efficient because it only processes each group once, without repeatedly comparing individual elements, making the code faster for long sequences.

**compared the execution time** of my solution and the optimized solution using the performance measurement code.
![스크린샷 2025-03-19 111029](https://github.com/user-attachments/assets/a0347b70-981a-4cf8-be37-60ae08526f1d)

### Sure! Let's break down the code `[key for key, _ in groupby(sequence)]` step by step:

### What is `groupby`?

The `groupby` function comes from Python’s `itertools` module. It groups consecutive, identical elements from an iterable (like a list) into groups. 

- **Example:**
  ```python
  from itertools import groupby
  sequence = [1, 1, 2, 2, 2, 3, 3, 4]
  result = groupby(sequence)
  for key, group in result:
      print(key, list(group))
  ```

  Output:
  ```
  1 [1, 1]
  2 [2, 2, 2]
  3 [3, 3]
  4 [4]
  ```

In this example:
- The `groupby` function groups consecutive 1s together, consecutive 2s together, and so on. It returns an iterator of `(key, group)` pairs.
- `key` is the value of the group (in this case, the number itself like `1`, `2`, etc.).
- `group` is an iterator that gives all elements in that group.

### Breaking down `[key for key, _ in groupby(sequence)]`

1. **List comprehension:**
   The code `[key for key, _ in groupby(sequence)]` is a **list comprehension**. List comprehensions are a concise way to generate lists in Python. They combine a `for` loop with an expression to create new lists.

2. **What is happening in the loop?**
   - `groupby(sequence)` returns a sequence of pairs `(key, group)`:
     - `key`: The value that is being grouped.
     - `_`: This represents the group (the actual consecutive elements). We don’t need the group itself, only the key (because we just want the distinct elements), so we use `_` to ignore it.
   
   - The list comprehension goes through each `(key, group)` returned by `groupby(sequence)` and extracts just the `key` (the value of each group), creating a list of all distinct values in the order they appear in the sequence.

3. **Why use `_`?**
   - In Python, `_` is a conventional way to indicate that you don’t care about a variable’s value. In this case, we don’t need the actual grouped values, only the unique "key" (the value) for each group.

4. **Final result:**
   The result of `[key for key, _ in groupby(sequence)]` is a list of the distinct elements of `sequence`, but only the first occurrence of each consecutive group. 

   - For example:
     ```python
     from itertools import groupby
     sequence = [1, 1, 2, 2, 2, 3, 3, 4]
     result = [key for key, _ in groupby(sequence)]
     print(result)
     ```

     Output:
     ```
     [1, 2, 3, 4]
     ```

     The `groupby` groups consecutive duplicate values, and the list comprehension picks the first element of each group, resulting in `[1, 2, 3, 4]`.

### Why is `groupby` useful here?
`groupby` is especially useful when you want to remove consecutive duplicates from a sequence. Without `groupby`, you'd have to manually iterate and compare each element with the previous one, which would be more complex and inefficient. With `groupby`, it automatically groups consecutive duplicates, allowing us to extract only the distinct elements in a concise and efficient way.

