# LeetCode #9 - Palindrome Number

## 📝 Problem Statement

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome number reads the same forward and backward.

### Examples

**Example 1**

Input:
```
121
```

Output:
```
true
```

---

**Example 2**

Input:
```
-121
```

Output:
```
false
```

Explanation:
A negative number cannot be a palindrome because of the minus sign.

---

**Example 3**

Input:
```
10
```

Output:
```
false
```

Explanation:
Reading from left to right is `10`, while from right to left it becomes `01`.

---

# 💡 Approach

Instead of converting the integer into a string, this solution compares the **first digit** and the **last digit** using mathematical operations.

### Step 1
If the number is negative, return `False`.

```python
if x < 0:
    return False
```

Negative numbers are never palindromes.

---

### Step 2
Find the divisor corresponding to the leftmost digit.

Example:

For

```
12321
```

The divisor becomes

```
10000
```

Code:

```python
div = 1

while x >= 10 * div:
    div *= 10
```

---

### Step 3
Compare the first digit and the last digit.

First digit:

```python
x // div
```

Last digit:

```python
x % 10
```

If they are different:

```python
return False
```

---

### Step 4
Remove the first and last digits.

```python
x = (x % div) // 10
```

Update divisor:

```python
div = div // 100
```

The divisor is divided by 100 because two digits are removed.

---

### Step 5
Repeat until all digits are checked.

If every pair matches:

```python
return True
```

---

# 🧠 Dry Run

Input

```
1221
```

Initial values

```
x = 1221
div = 1000
```

### First comparison

First digit

```
1221 // 1000 = 1
```

Last digit

```
1221 % 10 = 1
```

Match ✅

Remove them

```
x = (1221 % 1000) // 10
  = 221 // 10
  = 22

div = 1000 // 100
    = 10
```

---

### Second comparison

First digit

```
22 // 10 = 2
```

Last digit

```
22 % 10 = 2
```

Match ✅

Remove them

```
x = 0
```

Loop ends.

Return

```
True
```

---

# ⏱️ Complexity Analysis

**Time Complexity**

```
O(log10(n))
```

The algorithm processes one pair of digits during each iteration.

---

**Space Complexity**

```
O(1)
```

Only a few variables are used.

---

# ✅ Python Solution

```python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        div = 1

        while x >= 10 * div:
            div *= 10

        while x:
            if x // div != x % 10:
                return False

            x = (x % div) // 10
            div = div // 100

        return True
```

---

## 🚀 Key Learning

- Mathematical digit manipulation
- Integer division (`//`)
- Modulus operator (`%`)
- Finding the first digit using a divisor
- Comparing digits without converting the number to a string
- Constant space optimization

---

**Language:** Python 🐍

**Difficulty:** Easy

**LeetCode Problem:** #9 - Palindrome Number
