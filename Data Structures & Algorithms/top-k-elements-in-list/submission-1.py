##could use sort() to evaluate the array so key is sorted, and value is 
#returned list of most frequent?
#use a dictionary possibly for frequency counting
#or key could be actual number since it cant repeat, and value is frequency?
#and so after iterating through list, i need to evaluate for k = whatever, which values are from biggest to smallest that whatever
# so for k = 2, i look at the values or could sort them? to be biggest to smallest and take the first k values and then return the numeric
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1 ##value now is a frequency +1 
            else:
                seen[i] = 1 ####so starting with a count of 1
        change = sorted(seen.items(), key=lambda x: x[1], reverse=True) #sorted big to small of all values (frequencies)
        
        answer = []

        for x in change[:k]:
            answer.append(x[0])

        return answer


        
        
        

        