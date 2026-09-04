class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        for i in range(len(nums)+1):
            if i not in count:
                return i
    

        