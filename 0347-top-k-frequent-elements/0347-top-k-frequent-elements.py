class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        for num in nums:
          if num in dic:
            dic[num]+=1
          else:
            dic[num] = 1
        sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        ans = []

        for num in list(sorted_dic.keys())[:k]:
            ans.append(num)

        return ans
