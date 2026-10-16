class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stack = []
        if len(s)<=1:
            return False      

        for ch in s:
            if ch in ['[', '(', '{']:
                stack.append(ch)
            else:
                if stack and stack[-1] == matching[ch]:
                    stack.pop()
                else:
                    return False
           
        
        return not len(stack)