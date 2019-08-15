def PowerOfFour(num):
   if num == 1:
       return True
   elif num%2 != 0:
       return PowerOfFour(num//4)
   else:
       return False
print(PowerOfFour(3))
