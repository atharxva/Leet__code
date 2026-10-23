class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      
      dic = {}

      for num in jewels:
        if num in dic:
          dic[num]+=1
        else:
          dic[num] = 1

      count = 0

      for stone in stones:
        if stone in dic:
          count+=1
      
      return count