## MUST run in logn time
# all integers are unique, so could use a set/dict??


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)): ## in order to get index 
            if nums[i] == target:
                return i
            ## otherwise it continues 
        return -1



        