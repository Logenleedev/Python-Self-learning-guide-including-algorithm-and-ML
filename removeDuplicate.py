class Solution:
    def removeDuplicates(self,nums):
      result = []
      result.append(nums[0])
      for n in range(len(nums)):
        result_ref = False
        for x in range(n):
          if nums[x] == nums[n]:
            result_ref = False
          else:
            result_ref = True
        if result_ref:
          result.append(nums[n])
        else:
          continue

      return len(result)
