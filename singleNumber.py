class Solution:
    def __init__(self, PracticeQuestion, source):
        self._PracticeQuestion = PracticeQuestion
        self._source = source

    @property
    def PracticeQuestion(self):
        return self._PracticeQuestion
    
    @PracticeQuestion.setter
    def PracticeQuestion(self, PracticeQuestion):
        self._PracticeQuestion = PracticeQuestion

    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, source):
        self._source = source

    def singleNumber(self, nums):
        no_duplicatearray = []
        for x in nums:
            if x not in no_duplicatearray:
                no_duplicatearray.append(x)
            else:
                no_duplicatearray.remove(x)
        return no_duplicatearray.pop()
    

a = Solution("Simple Number","Leetcode")

print(a.singleNumber([4,1,1,2,2]))