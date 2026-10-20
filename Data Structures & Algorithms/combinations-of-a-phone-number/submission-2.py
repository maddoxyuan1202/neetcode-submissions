class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        matching={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        path = []
        if not digits:
            return []

        def dfs(start:int, count:int):
            if count == len(digits):
                res.append(''.join(path.copy()))
                return
            for i in range(start, len(digits)):
                for j in range(0, len(matching[digits[i]])):
                    path.append(matching[digits[i]][j])
                    dfs(i+1, count+1)
                    path.pop()
        dfs(0,0)
        return res
