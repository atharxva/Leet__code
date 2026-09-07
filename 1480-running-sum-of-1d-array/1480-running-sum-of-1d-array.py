class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total+= nums[i]
            answer[i] = total
        return answer