class Solution:

  def canJump(self, nums: list[int]) -> bool:
    reach = 0

    for i in range(len(nums)):
      # 1. If we can't even reach index i, we're stuck
      if i > reach:
        return False

      # 2. Update the furthest index we can reach
      if i + nums[i] > reach:
        reach = i + nums[i]

      # 3. If we can reach or overshoot the last index, we won!
      if reach >= len(nums) - 1:
        return True

    return True