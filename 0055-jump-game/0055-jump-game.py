class Solution:

  def canJump(self, nums: list[int]) -> bool:
    reach = 0

    for i in range(len(nums)):

      if i > reach:
        return False


      if i + nums[i] > reach:
        reach = i + nums[i]


      if reach >= len(nums) - 1:
        return True

    return True
