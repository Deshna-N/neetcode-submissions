## it is ascending order -> sorted
## ONE INDEXED NO ZERO 
## two pointers , index1 and 2 and index2 always bigger
## no base case of not a valid solution needed
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum = 0

        while left < right: 
            ##### so start comparing if u add up left and right
            #### if that sum is < target -> need left to move up 1
            ####if that sum is > target -> need right to move down 1
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            if sum < target:
                left += 1
            if sum == target:
                ## make indexes adjust to 1-index format
                right += 1
                left += 1
                return [left, right]





