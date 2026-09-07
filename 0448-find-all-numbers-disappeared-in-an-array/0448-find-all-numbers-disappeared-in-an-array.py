class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        missing = []
        for i in nums:
            count[i] = count.get(i , 0) + 1
        for i in range(1,len(nums)+1):
            if i not in count:
                missing.append(i)
        return missing