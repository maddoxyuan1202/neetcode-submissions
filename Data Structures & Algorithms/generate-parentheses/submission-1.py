class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(openNum, closeNum):
            if openNum == closeNum == n:
                res.append("".join(stack))

            if openNum < n:
                stack.append('(')
                dfs(openNum + 1, closeNum)
                stack.pop()

            if closeNum < openNum:
                stack.append(')')
                dfs(openNum, closeNum + 1)
                stack.pop()

            return 

        dfs(0, 0)
        return res