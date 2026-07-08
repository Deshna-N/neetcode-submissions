## temperatures = [], and temperatures[i] is the daily temp of the ith day
## return result = [], where result[i] is # days AFTER ith day before a more warm temp appears later on
## if no day warmer appears after ith day, result[i] == 0 and return that
## planning:...
# need to keep track of index for sure, and compare the temp[i] vs future ones (use max())
# need result = [] to have the difference between indices stored
# using a stack??? -> logic-> 
## store initial i in stack, for next one check if temp[i] > stack's top
## if yes then diff = temp[i] - stack's top, and store diff into result
## if no then diff = 0 and store diff into result
## DO I NEED TO POP AT ANYTIME FOR STACK??
## -> when 30 < 38 and replace, then pop
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        diff = 0
        result = [0] * len(temperatures) ## list that stores diff between indices
        stack = [] ## store indices of numbers needing next warm
        
        for i in range(len(temperatures)):
            if not stack: ## if its empty
                stack.append(i)
            else:
                    while (len(stack) != 0) and (temperatures[i] > temperatures[stack[-1]]):
                        prev = stack[-1]
                        stack.pop()
                        result[prev] = i - prev
                    stack.append(i)
        return result




                    
            


### ex:
# i = 0, stack empty so stack = [0]
# i = 1, 38 > 30 so 
        