class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 1
        ## two pointers
        left = 0
        right = 0
        check = set()
        max_length = 0

        if s == "": ## empty set
            max_length = 0

        while right < len(s): ## so pointers never go over length of full string
            ## each iteration
            while s[right] in check: ### found a duplicate, string breaks
                check.remove(s[left])
                left += 1
            check.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
            
### ex 1: curr is z(l 0), next is x(r 1), maxlength = 1 currlength = 1 [z] 
## z added to check, and z in check so curr is x (l 1), next is y (r 2), maxlength is = 2, currlength = 2 [zx]
## x added to check, x in check so curr is y (l 2), next is z (r 3), maxlength is 3, currlength is 3 [zxy]
## z is not added to check, z not in check so string breaks so curr is z (l 3), next is x (r 4), maxlength is 3, currlength is 1

