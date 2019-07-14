# Method 1

class Solution:
    def moveZeros(self, nums):
        count = 0
        for n in range(len(nums)):
            el = nums[n]
            if el != 0:
                nums[n], nums[count] = nums[count], nums[n]
                count += 1
        return nums
a = Solution()
print(a.moveZeros([0,1,0,3,12]))

# Method 2

class Solution(object):
    def moveZeroes(self, nums):
        append_times=nums.count(0)
        for i in range(append_times):
            nums.remove(0) #  Delete the front zero
            nums.append(0) # append it at the end of nums, the times of the addition and substraction shall be equal