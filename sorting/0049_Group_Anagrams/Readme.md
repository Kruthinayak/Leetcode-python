# LeetCode #49 - Group Anagrams

## 📝 Problem Statement

Given an array of strings `strs`, group the anagrams together.

You can return the answer in **any order**.

An **anagram** is a word formed by rearranging the letters of another word using all the original letters exactly once.

---

## 📌 Example

### Example 1

**Input**

```
strs = ["eat","tea","tan","ate","nat","bat"]
```

**Output**

```
[
  ["bat"],
  ["nat","tan"],
  ["ate","eat","tea"]
]
```

---

### Example 2

**Input**

```
strs = [""]
```

**Output**

```
[[""]]
```

---

### Example 3

**Input**

```
strs = ["a"]
```

**Output**

```
[["a"]]
```

---

## 💡 Intuition

Two strings are anagrams if they contain the **same characters**.

If we sort the characters of every string, all anagrams will produce the same sorted string.

Example:

```
eat → aet
tea → aet
ate → aet
```

Since all three produce the same sorted string, they belong to the same group.

---

## 🔍 Approach

### Step 1

Create a hash map to store groups of anagrams.

```python
groups = defaultdict(list)
```

---

### Step 2

Traverse every string in the input array.

```python
for s in strs:
```

---

### Step 3

Sort the characters of the string.

```python
key = "".join(sorted(s))
```

The sorted string becomes the unique key.

Example:

```
eat → aet
tea → aet
ate → aet
```

---

### Step 4

Store the original string in the corresponding group.

```python
groups[key].append(s)
```

---

### Step 5

Return all grouped anagrams.

```python
return list(groups.values())
```

---

## 🧠 Dry Run

Input

```
["eat","tea","tan","ate","nat","bat"]
```

Processing:

```
eat → aet
```

Dictionary

```
{
"aet": ["eat"]
}
```

Next

```
tea → aet
```

Dictionary

```
{
"aet": ["eat","tea"]
}
```

Next

```
ate → aet
```

Dictionary

```
{
"aet": ["eat","tea","ate"]
}
```

Next

```
tan → ant
nat → ant
```

Dictionary

```
{
"aet": ["eat","tea","ate"],
"ant": ["tan","nat"]
}
```

Next

```
bat → abt
```

Final Output

```
[
["eat","tea","ate"],
["tan","nat"],
["bat"]
]
```

---

## ⏱️ Complexity Analysis

### Time Complexity

```
O(n × k log k)
```

where:

- `n` = number of strings
- `k` = average length of each string

Sorting each string takes `O(k log k)`.

---

### Space Complexity

```
O(n × k)
```

Extra space is used for storing grouped anagrams.

---

## 🐍 Python Solution

```python
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())
```

---

## 🎯 Key Learnings

- Sorting Strings
- Hash Map (Dictionary)
- Grouping Similar Data
- String Manipulation
- Efficient Data Organization

---

## 📚 Concepts Used

- Sorting
- Hash Map
- Strings

---

## 🚀 Interview Tip

There are two common approaches for this problem:

### 1️⃣ Sorting Approach

- Sort every string.
- Use the sorted string as the dictionary key.
- Time Complexity: **O(n × k log k)**

### 2️⃣ Character Frequency Approach

- Count the frequency of each character.
- Use the frequency array as the key.
- Time Complexity: **O(n × k)**

The frequency-count approach is more optimized, but the sorting approach is easier to understand and is widely accepted in coding interviews.

---

**Difficulty:** Medium

**Language:** Python 🐍

**LeetCode Problem:** #49 - Group Anagrams
