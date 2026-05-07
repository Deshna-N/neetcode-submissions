##dictionary cant have duplicate keys!
##need to return indices, so key is number and indice is value

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} ##create dictionary
        for i in range(len(nums)): ##need to know how to loop for indice
            diff = target - nums[i]
            if diff in seen:
                ##return 
                return [seen[diff], i]
            else:              
                seen[nums[i]] = i ##storing the key, then value




        