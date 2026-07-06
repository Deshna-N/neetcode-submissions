## idea: for numbers, it just gets added into stack
## for +, get top number stored, pop it, then next top number and perform addition 
## then once done, add it into the tracking stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        output = 0

        for i in range(len(tokens)):
            if len(tokens) == 0:
                return 0
            elif len(tokens) == 1:
                return int(tokens[i])
            else: 
                if tokens[i] == '+':
                    top = stack[-1] ## last stored number
                    stack.pop()
                    output = int(stack[-1] + top)
                    stack.pop()
                    stack.append(output)
                elif tokens[i] == '-':
                    top = stack[-1]
                    stack.pop()
                    output = int(stack[-1] - top)
                    stack.pop()
                    stack.append(output)
                elif tokens[i] == '*':
                    top = stack[-1]
                    stack.pop()
                    output = int(stack[-1] * top)
                    stack.pop()
                    stack.append(output)
                elif tokens[i] == '/':
                    top = stack[-1]
                    stack.pop()
                    output = int(stack[-1] / top)
                    stack.pop()
                    stack.append(output)
                else: ## its a number
                    stack.append(int(tokens[i]))
        return output

## ex 1: stack = [1] -> stack = [1,2] -> top = 2 -> stack = [1], output = 2 + 1 = 3, tracking = [3]
## stack = [1,3,3] -> * sign so top = 3 -> stack = [1,3] -> output = 3 * 3 = 9, stack = [1,3,9]
## 