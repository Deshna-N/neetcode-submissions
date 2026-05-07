class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        first = {}
        second = {}

        for char in s:
            if char in first:
                first[char] += 1
            else:
                first[char] = 1
        
        for x in t:
            if x in second:
                second[x] += 1
            else:
                second[x] = 1
        
        if first == second:
            return True
        else:
            return False




