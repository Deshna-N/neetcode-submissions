## MUST run in logn time
# all integers are unique, so could use a set/dict??

#refreshed via google search on what binary search is


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1 

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: 
                high = mid -1
            else: 
                low = mid + 1
        return -1
        
        
        



        # for i in range(len(nums)): ## in order to get index 
        #     if nums[i] == target:
        #         return i
        #     ## otherwise it continues 
        # return -1



        