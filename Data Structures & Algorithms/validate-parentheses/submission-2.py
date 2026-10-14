class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack.pop() != matching[ch]:
                    return False

        
        return len(stack) == 0