# LeetCode #11 - Container With Most Water

## 📝 Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `iᵗʰ` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that can store the maximum amount of water.

Return the maximum amount of water the container can store.

---

## 📌 Example

### Example 1

**Input**

```
height = [1,8,6,2,5,4,8,3,7]
```

**Output**

```
49
```

**Explanation**

The maximum water is formed between heights `8` and `7`.

---

## 💡 Intuition

The amount of water depends on:

- The shorter of the two heights.
- The distance between them.

Formula:

```
Area = Width × Minimum Height
```

Checking every possible pair would take **O(n²)** time.

Instead, we use the **Two Pointers** technique.

---

## 🔍 Approach

### Step 1

Initialize two pointers.

```python
l = 0
r = len(height) - 1
```

- `l` starts from the left.
- `r` starts from the right.

---

### Step 2

Calculate the current area.

```python
area = (r - l) * min(height[l], height[r])
```

Update the maximum area.

```python
res = max(res, area)
```

---

### Step 3

Move the pointer with the smaller height.

```python
if height[l] < height[r]:
    l += 1
else:
    r -= 1
```

Why?

The shorter line limits the amount of water.

Moving the taller line cannot increase the height of the container, so we only move the shorter one hoping to find a taller line.

---

### Step 4

Repeat until the pointers meet.

Return the maximum area found.

---

## 🧠 Dry Run

Input

```
height = [1,8,6,2,5,4,8,3,7]
```

Initially

```
l = 0
r = 8
```

Area

```
width = 8
height = min(1,7)

Area = 8 × 1 = 8
```

Maximum

```
res = 8
```

Move left pointer.

```
l = 1
```

Now

```
height[1] = 8
height[8] = 7
```

Area

```
width = 7
height = 7

Area = 49
```

Maximum

```
res = 49
```

Continue moving pointers.

No larger area is found.

Answer

```
49
```

---

## ⏱️ Complexity Analysis

### Time Complexity

```
O(n)
```

Each pointer moves at most once across the array.

---

### Space Complexity

```
O(1)
```

Only a few variables are used.

---

## 🐍 Python Solution

```python
class Solution(object):
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
```

---

## 🎯 Key Learnings

- Two Pointers Technique
- Greedy Pointer Movement
- Optimizing from O(n²) to O(n)
- Calculating Area Using Width × Height
- Constant Space Optimization

---

## 📚 Concepts Used

- Arrays
- Two Pointers
- Greedy Algorithm

---

**Difficulty:** Medium

**Language:** Python 🐍

**LeetCode Problem:** #11 - Container With Most Water
