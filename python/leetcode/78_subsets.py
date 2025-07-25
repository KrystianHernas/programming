class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, end, tmp):
            ans.append(tmp.copy())
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        backtrack(0, len(nums), [])
        return ans

