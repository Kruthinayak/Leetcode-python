# LeetCode #1 - Two Sum

## 📝 Problem

Find the indices of two numbers in an array whose sum is equal to the given target.

---

## 💻 Python Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i

        return
```

---

## 🚀 Approach

This solution uses a **Dictionary (Hash Map)** to store the numbers that have already been visited along with their indices.

For every number in the array:

1. Calculate the difference between the target and the current number.
2. Check whether the difference already exists in the dictionary.
3. If it exists, return the index stored in the dictionary and the current index.
4. Otherwise, store the current number and its index in the dictionary.
5. Continue until the pair is found.

This approach avoids using nested loops and solves the problem efficiently in a single traversal.

---

## 🔍 Code Explanation

### Step 1: Create an Empty Dictionary

```python
prevMap = {}
```

A dictionary is created to store:

- **Key** → Number
- **Value** → Index

Example:

```text
{
    2: 0,
    7: 1
}
```

---

### Step 2: Traverse the Array

```python
for i, n in enumerate(nums):
```

`enumerate()` returns both the index and the value.

Example:

```python
nums = [2,7,11,15]
```

| Index | Number |
|------:|-------:|
| 0 | 2 |
| 1 | 7 |
| 2 | 11 |
| 3 | 15 |

---

### Step 3: Find the Required Difference

```python
diff = target - n
```

The difference represents the number required to reach the target.

Example:

```text
Target = 9
Current Number = 2

Difference = 9 - 2 = 7
```

---

### Step 4: Check if the Difference Exists

```python
if diff in prevMap:
```

If the difference is already present in the dictionary, the solution has been found.

```python
return [prevMap[diff], i]
```

The first index comes from the dictionary, and the second is the current index.

---

### Step 5: Store the Current Number

```python
prevMap[n] = i
```

If the required number is not found, store the current number and its index.

Example after first iteration:

```text
{
    2: 0
}
```

After second iteration:

```text
{
    2: 0,
    7: 1
}
```

---

## 🧪 Dry Run

### Input

```text
nums = [2,7,11,15]
target = 9
```

### Iteration 1

```text
Current Number = 2

Difference = 7

Dictionary = {}

7 is not found.

Store:
{
    2:0
}
```

---

### Iteration 2

```text
Current Number = 7

Difference = 2

Dictionary

{
    2:0
}

2 is found ✅
```

Return

```text
[0,1]
```

---

## ⏱️ Time Complexity

```text
O(n)
```

Only one traversal of the array is required.

---

## 💾 Space Complexity

```text
O(n)
```

The dictionary stores previously visited numbers.

---

## 📚 Concepts Used

- Arrays
- Dictionary (Hash Map)
- One-pass Traversal

---

⭐ This solution is part of my LeetCode learning journey.
