https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1130/

# contains duplicate

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
        
        return False
```

# single number

use **XOR** operator
1. $a \oplus a = 0$ (any number XORed itself is 0)
2. $a \oplus 0 = a$ (any number XORed with 0 is itself)
3. XOR is commutative and associative, meaning the order in which you apply the XOR operations does not matter

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_num = 0
        for i in nums:
            unique_num ^= i
            
        return unique_num
```

## why it works

given the array `[4, 1, 2, 1, 2]`, the operations would be $4 \oplus (1 \oplus 1) \oplus (2 \oplus 2)$
- since pairs cancel out to 0, the XOR operation on all elements will ultimately return the unique number
