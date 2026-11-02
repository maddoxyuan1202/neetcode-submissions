class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(nums: List[int], target: int):
            l, r = 0, len(nums)-1
            while (l <= r):
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        result_1 = binary_search(nums[:pivot], target)

        if result_1 != -1:
            return result_1

        result_2 = binary_search(nums[pivot:], target)

        if result_2 != -1:
            return result_2 + pivot

        return -1
        
