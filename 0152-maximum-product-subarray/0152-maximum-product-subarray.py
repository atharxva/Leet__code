class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        max_product = nums[0]

        for i in range(1,len(nums)):
            x = nums[i]
            old_max = curr_max
            old_min = curr_min

            curr_max = max(x , x* old_max  , x *old_min)
            curr_min = min(x , x * old_max , x * old_min)

            max_product = max(curr_max , max_product)

        return max_product