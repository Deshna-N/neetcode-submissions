#need to store frequencies of each letter? so using a dict for each char->count
#but output needs to be a returning full list of the substrings...
#NEED to use sorted() so that i can compare if that output is same as other string
#but sorted() returns a list which isnt great for a key, so use "".join(...)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} #key of sorted, value of returning list
        for i in strs:
            change = sorted(i)  ##change is the key to store in dict
            change = "".join(change)
            if change not in seen:
                seen[change] = [i]
            else: ##it is in seen thus it is an anagram to add onto the list
                seen[change].append(i)
        return list(seen.values())
        