class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # przechowywanie odpowiedzi
        ans = []

        def backtrack(start):
            # warunek wyjściowy
            if start == len(nums):
                ans.append(nums[:])
                return

            for num in range(start, len(nums)):
                # zamieniamy
                temp = nums[start]
                nums[start] = nums[num]
                nums[num] = temp

                # print('b', num, start)
                backtrack(start + 1)
                temp = nums[start]
                nums[start] = nums[num]
                nums[num] = temp

                # print('a', num, start)
        backtrack(0)
        return ans
