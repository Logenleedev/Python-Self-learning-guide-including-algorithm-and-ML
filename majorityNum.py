# Solution 1 Brute force 
# Time Complexity O(n^2)

# Solution 2 Sorting
# Time Complexity O(n)

# Solution 3 HashTable
# Time Complexity O(n)

class Solution1:
    def majorityElement(self, nums) -> int:
        MajorTime = len(nums)//2
        for elements in nums:
            count = 0
            for element in nums:
                if element == elements:
                    count += 1
                    if count > MajorTime:
                        return element 


class Solution2:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution3:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


