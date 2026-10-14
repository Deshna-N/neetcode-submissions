## use a dict -> key = number, value = frequency
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        res = []
        for num in nums:
            if num not in mydict:
                mydict[num] = 0
            mydict[num] += 1
        ## stored all nums and their freq in mydict
        # need to find highest freq and use its key
        while k > 0:
            highest_freqs_key = max(mydict, key=mydict.get)
            mydict.pop(highest_freqs_key)
            res.append(highest_freqs_key)
            k -= 1
        return res