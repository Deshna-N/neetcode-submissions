## monotonic queue can remove from back and front
# for incoming number, compare to most recetly added to back 
## if smaller, dequeue from back, then all numbers infront of new added num
## will be greater than it, so we have a descending group of nums


## create monotonic queue (deque)
## For each new R
## compare to most recent added number in dequeue
## 1. if R > number, remove number and repeat 2. otherwise add R
## if front index outside window, remove front 
## k elements processed, than add number in front of dequeue to final output

from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        output = []

        ## create dequeue, guessig for now
        qu = deque()

        for R in range(len(nums)): ## R is an index now, gotta use index to store
                while qu and nums[R] > nums[qu[-1]]:## last character in deque, but gotta compare the number tho not the number in the deque which is just the index
                    qu.pop()
                qu.append(R)

                if qu[0] < (R - k) + 1: ## so window length still valid
                    qu.popleft()
                if R >= k - 1: 
                    output.append(nums[qu[0]])
        return output

            
            
            






        