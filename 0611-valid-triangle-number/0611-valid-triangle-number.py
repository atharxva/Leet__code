class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
      nums.sort()
      triplet =0 
      for r in range(len(nums)-1,-1,-1):
        l = 0
        i = r - 1

        while l < i:
          if nums[l] + nums[i] > nums[r]:
            triplet+=i-l
            i-=1
          else:
            l+=1
      return triplet