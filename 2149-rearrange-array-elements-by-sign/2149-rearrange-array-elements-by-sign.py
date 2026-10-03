class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        neg = []
        pos = []

        for i in range(len(nums)):
            if(nums[i] < 0):
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        
        for i in range(len(nums)):
            if(i % 2 == 0):
                nums[i] = pos[i//2]
            else:
                nums[i] = neg[i//2]

        return nums