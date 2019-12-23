
#    0  1  2  3  4  5  6  7  8  9  10 
A = [64,25,12,22,11,37,98,47,58,20,98]

'''
Selection Sort O(n^2)
'''
def SelectionSort(Array):
    for i in range(len(Array)):
        if (i != len(Array)-1): 
            for j in range(i+1,len(Array)):
                if Array[i]>Array[j]:
                    Array[i],Array[j] = Array[j],Array[i]
        else:
            return Array



            
'''
Bubble Sort O(n^2) min -> max
'''

def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

'''
Insertion Sort 
'''
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 


'''
Linear Search
'''

def linearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i+1
    return -1



'''
# Merge Sort

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)




'''


'''
Binary Search
'''

def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	while first<=last:
	    midpoint = (first + last)//2
	    if alist[midpoint] == item:
	        return midpoint
	    else:
	        if item < alist[midpoint]:
	            last = midpoint-1
	        else:
	            first = midpoint+1
    



	
# for i in range(len(A)):
#     print("%d" %A[i])
