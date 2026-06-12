class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## values not sorted 
        ## a + b + c = 0
        ## or b + a = -c
        ## can have a b pointer and c pointer, and target is a that could change?
        ## two_sums = left + right
        ## target = 0 - two_sums
        ## if target in nums: -> store [left, right, target] in final list 

        ##at end, return the final list

        left = 0 ## a 
        right = 0 ## b 
        target = 0 ## c , where 0 minus two_sums = target or c
        two_sums = 0 ## when b and a are added together 
        final = [] ## returning at end 
        
        nums = sorted(nums)
        for i in range(len(nums)):  ## gonna increase

        ## duplicates skip, didnt get myself
            if i > 0 and nums[i] == nums[i - 1]:
                continue ## skip
                
            left = i + 1 ## a 
            right = len(nums) - 1
            target = -(nums[i]) ## target is the curr first number in the array, the neg.
                ## now gotta see if b + a equal -c, so if left + right = target 
            while left < right: 
                two_sums = nums[left] + nums[right]
                if two_sums == target: ### then found a triplet
                    final.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif two_sums > target: ## need a smaller num, so make right go down
                    right -= 1
                elif two_sums < target:
                    left += 1                     
        return final

        ## ex: nums = [-1,0,1,2,-1,-4] , i in range of 6
        #two_sums = -1 + -4, target = 1, -5 < 1 so left + 1 (0), r (-4)
        ## for i = 2, two_sum = -4 , target = 0, -4 < 0 so left + 1 (1), r (-4)
        # for i = 3, two_sum = -3, target = -1, -3 < -1 so left + 1 (2) , r (-4)
        # for i = 4, two_sum = -2, target = 2, -2 < 2 so left + 1 (-1) , r (-4)

            



