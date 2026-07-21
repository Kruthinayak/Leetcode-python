# LeetCode #17 - Letter Combinations of a Phone Number

## 📝 Problem Statement

Given a string containing digits from **2-9** inclusive, return all possible letter combinations that the number could represent.

The mapping of digits to letters is the same as on a telephone keypad.

Return the answer in **any order**.

---

## 📌 Example

### Example 1

**Input**

```
digits = "23"
```

**Output**

```
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

### Example 2

**Input**

```
digits = ""
```

**Output**

```
[]
```

---

### Example 3

**Input**

```
digits = "2"
```

**Output**

```
["a","b","c"]
```

---

## 💡 Intuition

Each digit can represent multiple letters.

For example,

```
2 → abc
3 → def
```

If the input is

```
23
```

we need every possible combination:

```
a + d
a + e
a + f

b + d
b + e
b + f

c + d
c + e
c + f
```

This is a classic **Backtracking** problem because we try every possible choice, move to the next digit, and continue building the string until a complete combination is formed.

---

## 🔍 Approach

### Step 1

Create a dictionary to store the digit-to-letter mapping.

```python
digitToChar = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
```

---

### Step 2

Create a Backtracking function.

```python
backtrack(i, curStr)
```

where

- `i` → current digit index
- `curStr` → current combination being built

---

### Step 3

Base Case

If the length of the current string becomes equal to the number of digits,

```python
if len(curStr) == len(digits):
```

store the completed combination.

```python
res.append(curStr)
```

---

### Step 4

Loop through every letter corresponding to the current digit.

```python
for c in digitToChar[digits[i]]:
```

Recursively move to the next digit.

```python
backtrack(i + 1, curStr + c)
```

Eventually, every possible combination is explored.

---

## 🌳 Recursion Tree

For

```
digits = "23"
```

```
                ""
               / | \
             a  b  c
            /|\ /|\ /|\
           d e f d e f d e f
```

Generated combinations:

```
ad
ae
af
bd
be
bf
cd
ce
cf
```

---

## 🧠 Dry Run

Input

```
digits = "23"
```

Start

```
backtrack(0, "")
```

Choose

```
a
```

Current String

```
"a"
```

Move to next digit

Choose

```
d
```

Current String

```
"ad"
```

Length equals number of digits.

Store

```
["ad"]
```

Go back.

Choose

```
e
```

Store

```
["ad","ae"]
```

Continue until

```
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

## ⏱️ Complexity Analysis

### Time Complexity

```
O(4^n × n)
```

where `n` is the number of digits.

Each digit has at most **4 possible letters** (digit 7 and 9), and creating each combination takes up to `n` characters.

---

### Space Complexity

```
O(n)
```

The recursion stack grows up to the length of the input.

(The output list itself is not counted in auxiliary space.)

---

## 🐍 Python Solution

```python
class Solution(object):
    def letterCombinations(self, digits):
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res
```

---

## 🎯 Key Learnings

- Backtracking
- Recursion
- Tree Traversal
- Depth-First Search (DFS)
- Building combinations recursively
- Dictionary (Hash Map)

---

## 📚 Concepts Used

- Backtracking
- Recursion
- DFS
- Hash Map
- Strings

---

## 🚀 Interview Tip

This problem is one of the most common **Backtracking** interview questions. Understanding this pattern makes it much easier to solve similar problems such as:

- Subsets
- Combination Sum
- Permutations
- Generate Parentheses
- N-Queens
- Word Search

Mastering this problem builds a strong foundation for recursive problem-solving.

---

**Difficulty:** Medium

**Language:** Python 🐍

**LeetCode Problem:** #17 - Letter Combinations of a Phone Number
