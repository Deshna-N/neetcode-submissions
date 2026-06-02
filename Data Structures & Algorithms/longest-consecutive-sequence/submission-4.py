# could use a set maybe, no repeats, but does not check for consecutive...
# could make a set and check if each i > i - 1 but still not consecutive...

# could add each element in nums to a set
# then could track curr_num as i - 1, and then if i = curr_num + 1 continue 
# if false then stop and output so need an output incrementing by 1
# ~~~~~~~~
# ok instead i could check if a certain number is in the set!
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        curr_length = 1
        final_length = 1
        

        for x in nums: #O(n)
            s.add(x)
        # no duplicates added, so ex 1: s = [2,20,4,10,3,5]

        curr_num = 0
        next_num = 0
        prev_num = 0

        if nums == []:
                curr_length = 0
                return curr_length

        for i in s:
            ### need base case of if first number, then next num is increment of that?
            ## answer: check if there is a predecessor!
            if (i - 1) in s:
                continue 
            else:
                ## i is start of sequence          
                next_num = i + 1
                while (next_num in s):
                    next_num = next_num + 1
                    curr_length += 1
                    if curr_length > final_length:
                        final_length = curr_length
                else:
                    curr_length = 1

            # so we have now gone through all of s, and tried to find consecutive sequence
        return final_length

## case 1: s = [2,20,4,10,3,5]
# curr_num = 0, next_num = 1
# at base case, 
            



            
            
            


        
        
        
        


        