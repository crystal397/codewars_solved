## Description

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

### Examples
```
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```
\# Mathematics \# Algorithms

# Solutions
1. I solved the problem using a **recursive function**.
2. But I found a smarter and simpler solution.
   This solution calculates the digital root **using the map function** without recursion. It repeatedly sums the digits of the number by converting it to a string, mapping each character to an integer, and summing them up. This process is repeated until the result is a single-digit number.
   
   The performance difference between the two solutions becomes more significant with larger numbers. The first solution uses recursion and converts the number to a string at each step, which takes more time. Especially with large numbers, more recursive calls and `str()` conversions occur, which affects performance.
    The second solution uses a loop and map to intuitively solve the problem, **resulting in lower memory usage and faster execution**.

I **compared the execution time** of my solution and the optimized solution using the performance measurement code.
<img width="794" alt="스크린샷 2025-02-24 오후 2 27 43" src="https://github.com/user-attachments/assets/683c7496-ed02-4cee-8e9a-46fa34a2ba4a" />
