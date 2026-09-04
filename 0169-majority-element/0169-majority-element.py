class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        threshold = len(nums) // 2
        
        for num, count in counts.items():
            if count > threshold:
                return num