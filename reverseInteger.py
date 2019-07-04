'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        strNum = str(x)
        if strNum[0] == "-":
            negativestrNum = strNum[1:]
            reversenumstr = '-'+negativestrNum[::-1]
            reversenumstrInt = int(reversenumstr)
            if reversenumstrInt < -2**31 or reversenumstrInt > 2**31-1:
                return 0
            else:
                return reversenumstrInt
        else:
            reversenumstr = strNum[::-1]
            reversenum = int(reversenumstr)
            if reversenum < -2**31 or reversenum > 2**31 -1:
                return 0
            else:
                return reversenum