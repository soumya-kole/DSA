---
difficulty: Medium
tags:
    - Array
    - Hash Table
    - String
    - Sorting
---

# [1152. Analyze User Website Visit Pattern 🔒](https://leetcode.com/problems/analyze-user-website-visit-pattern)

## Description

You are given two string arrays `username` and `website` and an integer array `timestamp`, all of the same length `n`, where `username[i]` is the username, `website[i]` is the website visited, and `timestamp[i]` is the timestamp of the visit.

A **pattern** is a list of three websites (not necessarily distinct).

- For example, `["home", "away", "love"]`, `["leetcode", "love", "leetcode"]`, and `["luffy", "luffy", "luffy"]` are all patterns.

The **score** of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

- For example, if the pattern is `["home", "away", "love"]`, the score is the number of users `x` such that `x` visited `"home"` then later visited `"away"` and then visited `"love"`, all by following the order of patterns.
- Similarly, if the pattern is `["leetcode", "love", "leetcode"]`, the score is the number of users `x` such that `x` visited `"leetcode"` then visited `"love"` and then visited `"leetcode"` again, all by following the order of patterns.

Return the pattern with the largest score. If there is a tie, return the lexicographically smallest pattern.

### Example 1:

```
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
```

### Example 2:

```
Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
Output: ["a","b","a"]
```

### Constraints:

- `3 <= username.length <= 50`
- `1 <= username[i].length <= 10`
- `timestamp.length == username.length`
- `website.length == username.length`
- `1 <= website[i].length <= 10`
- `username[i]` and `website[i]` consist of lowercase English letters.
- `0 <= timestamp[i] <= 10^9`
- It is guaranteed that there is at least one user who visited at least three websites.
- All the tuples `[username[i], timestamp[i], website[i]]` are unique.
