

def solve(a):
    if isinstance(a, (int, float)) != True:
        return 
    else:
        result = []
        result.append(a)
        while a != 1:
            if a > 1:
                if (a%2 == 0):
                    a = a/2
                    result.append(a)
                else:
                    a = 3*a + 1
                    result.append(a)
        
        return result
print(solve("3"))

    