## valid when every open is closed by same type -> track in pairs
# if closing gotta aklready be open

## wanna use a stack

## possible char: '(', ')', '[', ']', '{', '}'

## latest opened bracket must close first


class Solution:
    def isValid(self, s: str) -> bool:
        track = [] ## stack 
        for i in s: ## so while its not empty
            if i == '(' or i == '[' or i == '{':
                track.append(i) ## each opening paranthesis regardless of type
            elif i == ')' or i == ']' or i == '}':
                if len(track) == 0:
                    return False
                top_check = track[-1]

                if top_check != '(' and i == ')':
                    return False
                elif top_check != '[' and i == ']':
                    return False
                elif top_check != '{' and i == '}':
                    return False
                else: ## there is an open correct bracket
                    track.pop()
        if not track: ## checks if empty
            return True
        else:
            return False
                






        