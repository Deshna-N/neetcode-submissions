class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ##use a set because sets cannot have duplicates!
        seen = set()
        for i in nums:
            if i in seen: ##already in the set
                return True
            else:
                seen.add(i)
        return False
        