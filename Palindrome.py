class Solution:
    def __init__ (self, problemName, source):
        self._problemName = problemName
        self._source = source
    
    @property
    def problemName(self):
        return self._problemName
    
    @problemName.setter 
    def problemName (self,problemName):
        self._problemName = self.problemName

    @staticmethod
    def Palindrome(nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] != nums[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

s = Solution("Palindrom" , "Leetcode")
print(s.Palindrome("ada"))
