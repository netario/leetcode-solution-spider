# LeetCode Spider

a simple python script
input a set of problem links, spider will automatically scratch your accepted solutions and push to github

**input sample**

```
- Leetcode ¡¾125¡¿Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/description/

- Leetcode ¡¾235¡¿Lowest Common Ancestor of a Binary Search Tree (Easy)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

- Leetcode ¡¾236¡¿Lowest Common Ancestor of a Binary Tree (Medium)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
```

**output sample**

```
[cpp] leetcode 125 :
|SubmitTime 1 year, 8 months ago |RunTime 12 ms beats 18.38 % |Lines 15
https://github.com/netario/leetcode-solutions/blob/master/125_valid_palindrome.cpp
[cpp] leetcode 235 :
|SubmitTime 1 year, 8 months ago |RunTime 44 ms beats 4.18 % |Lines 17
https://github.com/netario/leetcode-solutions/blob/master/235_lowest_common_ancestor_of_a_binary_search_tree.cpp
[cpp] leetcode 236 :
|SubmitTime 46 minutes ago |RunTime 13 ms beats 61.58 % |Lines 18
https://github.com/netario/leetcode-solutions/blob/master/236_lowest_common_ancestor_of_a_binary_tree.cpp
```

### Test Environment
**Windows 7**

### Required Python Package
python -m pip install **selenium**
python -m pip install **gitpython**

### Useful Links
**How to connecting to github using SSH keys**
https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/