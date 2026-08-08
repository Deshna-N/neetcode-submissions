### "rotating" means shifitng all elements to right 1 indice
## if rotated n times, where len(nums) == n, then list stays as it was before rotating
## all unique numbers!!! -> set??
## want O(logn) time, using a mid pointer along with left and right
## brute force likely is just looking through array and returning the lowest number, updating after looking at each element so that would be O(n)

## list before was ascending, has already been rotated tho so idk where it started


## could just start left at 0 index, right at len(nums) - 1, mid = left + right // 2
## however idk if elmeent on right or left of mid can be greater or less than, gotta note for that
## but goal is having a smaller and smaller window to evaluate



## if nums[mid] > nums[right] then rotation point is between mid and right
## if nums[mid] < nums[right] then min is anywhere left to including mid

## cant think of any base cases to take care of 

## how to leave loop...when 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        track_min = 0

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            ###else: ## nums[mid] == nums[right]
                ###### then the min is right - 1 so return that
            ## believe when leaving while loop it means min was found
        return nums[left] ## could do nums[right] also both point same place atp tho



## run through an example:
## nums = [3,4,5,6,1,2]
## left at index 0, right at index 5, mid is 5 // 2 = 2 
## 5 is > 2 so left = 3 aka 6
## left at index 3, right at index 5, mid is 8 // 2 = 4
# 1 < 2 so right = index 4 aka (1)
# left still at index 3, right at index 4, mid is 7 // 2 = 3
# nums[mid] < nums[right] aka 6 < 1, so right = index 3 aka 

## numns = [4,5,0,1,2,3]
# left at index 0 (4), right at index 5 (3), mid is 5 // 2 = index 2 (0)
# 0 < 3 so right = index 2 (0)
# left at index 0 (4), right at index 2 (0), mid is 2 // 2 = index 1 (5)
# 5 > 0 so left = index 2 (0)
# now nums[right] and nums[left] are equal
        