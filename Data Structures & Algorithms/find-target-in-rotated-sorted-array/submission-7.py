## cases to note for :
# 1. if target is not present in array, then gotta return -1
# 2. when left == right, gotta check if that number is target else return -1

## when nums[mid] < nums[right], means the right half is sorted since its ascend
## when nums[mid] > nums[right], means left half is sorted one and right has pivot

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right: 
            mid = (left + right) // 2
            if nums[mid] != target:
                if nums[mid] < nums[right]: ## right half sorted
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else: # target is not in right sorted half then
                         right = mid - 1
                elif nums[mid] > nums[right]: ## left half sorted, right has pivot
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else: ## target not in sorted left half
                        left = mid + 1
                ### otherwise left == right then so target is at that?
            else: ## mid == target
                return mid
        ## at this point, left and right point to same number
        if nums[left] == target:
            return left
        
        else: ## target not in the array nums
            return -1

## example 1: nums = [3,4,5,6,1,2] and target = 1
## left = index 0 (3), right = index 5 (2), mid = 5 // 2 = index 2 (5)
# 5 != 1 so then -> 5 > 2 so left = index 3 (6)
# left = index 3 (6), right = index 5 (2), mid = 8 // 2 = index 4 (1)
# 1 == 1!!!!! so return mid aka index 4


## ex 2: nums=[1,3], target=3
# left = index 0 (1), right = index 1 (3), mid = 1 // 2 = index 0 (1)
# mid != target so -> 1 < 3 so right = mid aka index 0 (1) aka we leave while loop now
## so nums[left] is 1 and 1 != 3 so return -1












