def Twosum(num, target):
    length = len(num)
    answer = []
    for i in range(length-1):
        for j in range(i+1, length):
            sum = num[i] + num[j]
            if sum == target:
                answer.append(i)
                answer.append(j)
                break
    return answer


print(Twosum([1, 4, 6, 7], 8))