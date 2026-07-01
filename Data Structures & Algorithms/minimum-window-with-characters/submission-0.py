class Solution:

    def isValid(self, need, window) -> bool:
        for c in need:
            if window.get(c, 0) < need[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        L = 0

        best = ""
        length = float("inf")

        ## add all letters and their freq of t into need
        for x in t:
            if x not in need:
                need[x] = 0
            need[x] += 1


        ## 
        for R in range(len(s)):
            ##  expanding window by adding in letter at R till window valid
            if s[R] not in window:
                window[s[R]] = 0
            window[s[R]] += 1

            ## 
            while self.isValid(need, window): ##valid, wanna try toshrink 
                if (R - L + 1) < length:
                    length = R - L + 1
                    best = s[L:R + 1]
                window[s[L]] -= 1
                L += 1 ## remove left by 1 
        return best
                ## now it should go back to checking this if statement
            ## if here, then now window isn't valid anymore, must keep expanding right 

        
