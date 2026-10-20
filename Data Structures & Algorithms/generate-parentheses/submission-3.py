class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(numOpen:int, numClose:int):
            if numOpen == numClose == n:
                res.append(''.join(stack))

            if numOpen < n:
                stack.append('(')
                dfs(numOpen+1, numClose)
                stack.pop()

            if numClose < numOpen:
                stack.append(')')
                dfs(numOpen, numClose+1)
                stack.pop()

        dfs(0,0 )
        return res