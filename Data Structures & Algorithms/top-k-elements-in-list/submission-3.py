## use a dict -> key = number, value = frequency
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        mydict = {}
        res = []
        for i in range(len(nums) + 1):
            buckets.append([])
        for num in nums:
            if num not in mydict:
                mydict[num] = 0
            mydict[num] += 1
            ### now mydict got key = num, val = freq
        ## need to map mLydict's freq to = index in buckets, and store mydict's key there
        for num, f in mydict.items():
            buckets[f].append(num)

        i = len(buckets) - 1

        while i > 0:
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            i -= 1

        
            



        ## stored all nums and their freq in mydict
        # need to find highest freq and use its key
        while k > 0:
            highest_freqs_key = max(mydict, key=mydict.get)
            mydict.pop(highest_freqs_key)
            res.append(highest_freqs_key)
            k -= 1
        return res