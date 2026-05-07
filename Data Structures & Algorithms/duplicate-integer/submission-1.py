class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        tracking = 0
        if len(s) < len(nums): ##that means a duplicate was removed
            return True
        else:
            return False