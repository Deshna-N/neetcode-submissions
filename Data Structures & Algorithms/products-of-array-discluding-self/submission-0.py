# could take everything and multiply each other, then divide by output[i] and then thats answer
# how to store? ->can have duplicates so no set
# dont know length so might wanna use a while loop?
# need to either store the curr i or smthing else... 
# prefix = [1, 1, 2, 8]
# suffix = [ 48, 24 , 6 , 1]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ###have the sub prefix product list put together
        prefix = [] 
        suffix = []
        tot = 1
        for n in nums:
            prefix.append(tot)
            tot = n * tot
        ## prefix fully stored now
        tot = 1
        for x in reversed(nums):
            suffix.append(tot)
            tot = x * tot
        suffix.reverse()
        ## now multiply both lists together and return as one!
        ## both would have same index numbers and all, if any negatives should work out itself
        final = []
        for i in range(len(prefix)):
            final.append(prefix[i] * suffix[i])
        return final

        


        