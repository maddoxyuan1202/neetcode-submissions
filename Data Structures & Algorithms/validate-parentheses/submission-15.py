class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []
        if not s:
            return False

        for ch in s:
            if ch in matching:
                if stack and stack[-1] == matching[ch]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(ch)
        
        return True if not stack else False