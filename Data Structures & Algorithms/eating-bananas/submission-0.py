## piles has each number of banana at each spot
# h is how much time i got to consume bananana
# k is rate of eating  bananans per hour, can only eat k bananana each hour
## if pile has < k, finish the pile and whatever its got (can't consume from another)
# return min of K 

## def want left right pointers to track going through piles
## can use left right pointers to select best pile to choose to consume at certain hour??
### but now i think does that even matter what specific pile ate first mattering??
#### IF H == len(piles), then min integer K MUST equal len(piles)
## log in the complexity so prob want a mid so using binary search

### how to find k ????? 
# brute force option of starting k at 1 and then if doesnt work go to 2,3,4...

## thinking now instead that left right pointers hsould just be for selecting pile to eat

## first hint points out h >= len of piles
## if h == k, then this upper bound means k equals largest number in the array of piles
# lower bound is smallest number k found rn???

# second hint -> ceil(x/k) hour to finish a pile

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_k_rate = 1
        right_k_rate = max(piles)

        if h == len(piles): ## upper bound base case
            return right_k_rate

        while left_k_rate <= right_k_rate:
            mid_k_rate = (left_k_rate + right_k_rate) // 2
            total_hours = 0

            for i in piles:
                total_hours += (math.ceil(i / mid_k_rate))

            if total_hours > h: ## we passed our avail hrs so increment lower bound and move on
                left_k_rate = mid_k_rate + 1 ## def not our best answer coming from here
            else: ## total_hours is equal or less than h, we could make upper bound smaller 
                best_k = mid_k_rate
                right_k_rate = mid_k_rate - 1

                
                
        return best_k





## ex 1: piles = [1,4,3,2] and h = 9, left_k = 1, right_k = 4, mid_k = 2
# 


        