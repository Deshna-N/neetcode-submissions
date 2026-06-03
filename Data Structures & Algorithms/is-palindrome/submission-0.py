## Ccould have two pointers, one starting at end other at beginning and if each element equals for two pointers then move them along
## iterate forward/backwards

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 ## at the end

        while left < right:
            if not s[left].isalnum(): ##left pointer at non alphanumeric
                left += 1
            elif not s[right].isalnum(): #right opointer at non alphanumeric
                right -= 1
            else:  
                ## now each compared letter is lower case

                if s[left].lower() != s[right].lower(): ### so stops palindrome
                    return False
                ### otherwise palindrome must continue so move pointers
                left += 1
                right -= 1
            
        ###loop has ended so palindrome is true
        return True
            





        