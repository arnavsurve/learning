class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
        
        return False
