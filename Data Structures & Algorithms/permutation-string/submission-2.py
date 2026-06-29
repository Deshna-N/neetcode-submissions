## could use a dictionary for key to track letter, value to track frequency
## CONFUSION, once i find that for example c is infact in check.keys() what to do?
## should i decrement the frequency of letters from check and then after iterating do smthing?

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        check1 = {}
        check2 = {}

        if len(s1) > len(s2):
            return False

        while left < len(s1):
            if s1[left] not in check1:
                check1[s1[left]] = 0
            check1[s1[left]] += 1
            left += 1
            ## check 1 built
        left = 0
        right = len(s1) - 1 #reset

        while left <= right:
            if s2[left] not in check2:
                check2[s2[left]] = 0
            check2[s2[left]] += 1
            left += 1
            ## check 2 built
        left = 0
        right = len(s1) - 1 # reset

        if check1 == check2: ## for the first iteration if it happens to end up being true
            return True

        while right < len(s2) - 1: ## - 1 is so window can exist, left shouldnt be highets num
            ## get rid of the left letter
            check2[s2[left]] -= 1
            if check2[s2[left]] == 0:
                del check2[s2[left]]

            left += 1
            right += 1

            ## adding in new right letter after iteration
            if s2[right] not in check2:
                check2[s2[right]] = 0
            check2[s2[right]] += 1

            if check1 == check2:
                return True
        return False

        




            