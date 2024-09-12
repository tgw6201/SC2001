import random
import time

maxArrSize = 10000
sValue = 25
randomNumRange = 5000

mergeSortKeyComparision = 0
insertionSortKeyComparision = 0
hybridSortKeyComparision = 0

def merge_sort(arr):
    global mergeSortKeyComparision  # Declare the global variable
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    global mergeSortKeyComparision  # Declare the global variable
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        mergeSortKeyComparision += 1  # Increment comparison count
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

def insertionSort(arr):
    global insertionSortKeyComparision  # Declare the global variable
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            insertionSortKeyComparision += 1  # Increment comparison count
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def hybridSort(arr, s):
    if len(arr) <= s:
        return hybridInsertionSort(arr)
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = hybridSort(left_half, s)
    right_half = hybridSort(right_half, s)
    
    return hybridMergeSort(left_half, right_half)

def hybridInsertionSort(arr):
    global hybridSortKeyComparision  # Declare the global variable
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            hybridSortKeyComparision += 1  # Increment comparison count
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def hybridMergeSort(left, right):
    global hybridSortKeyComparision  # Declare the global variable
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        hybridSortKeyComparision += 1  # Increment comparison count
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged


## Part B generating input data
## Size referes to the max size of array, n refers to the range of numbers, and duplicate refers to whether the array can have duplicates
def initialize_array(size, n, duplicate):
    if(duplicate):
        return [random.randint(1, n) for _ in range(size)]
    else:
        return random.sample(range(1, size+1), size)

## Part C.i
def fixedS_VS_arraySize(sValue,maxRange,pwr10=7,dupe=True):
    global hybridSortKeyComparision
    
    for i in range(3,pwr10+1):
        hybridSortKeyComparision = 0
        if(dupe):
            arr = initialize_array(10**i,maxRange,dupe)
        else:
            arr = initialize_array(10**i,maxRange,dupe)
        start = time.time()
        hybridSort(arr,sValue)
        end = time.time()
        print("ArraySize: ",10**i," Key Comparisons: ",hybridSortKeyComparision, " Time Taken: ",end-start)
        
## Part C.ii
def fixedArraySize_VS_sValue(startingS,endingS,stepS,size,maxRandArr,dupe=True):
    global hybridSortKeyComparision
    
    for i in range(startingS,endingS+1,stepS):
        hybridSortKeyComparision = 0
        if(dupe):
            arr = initialize_array(size,maxRandArr,dupe)
        else:
            arr = initialize_array(size,maxRandArr,dupe)
        start = time.time()
        hybridSort(arr,i)
        end = time.time()
        print("S Value: ",i," Key Comparisons: ",hybridSortKeyComparision, " Time Taken: ",end-start)

## Part C.iii
def differentSValuesVSDifferentArraySize(startingS,endingS,stepS,arrMaxRange,pwr10=5,dupe=True):
    global hybridSortKeyComparision
    
    for i in range(startingS,endingS+1,stepS):
        for j in range(3,pwr10+1):
            hybridSortKeyComparision = 0
            if(dupe):
                arr = initialize_array(10**j,arrMaxRange,dupe)
            else:
                arr = initialize_array(10**j,arrMaxRange,dupe)
            start = time.time()
            hybridSort(arr,i)
            end = time.time()
            print("S Value: ",i," ArraySize: ",10**j," Key Comparisons: ",hybridSortKeyComparision, " Time Taken: ",end-start)
        print("\n")
        

## Part D
def hybridVsMerge(size, maxRange, sValue, dupe):
    global mergeSortKeyComparision, hybridSortKeyComparision
    
    hybridSortKeyComparision = 0
    mergeSortKeyComparision = 0
    
    if(dupe):
        arr = initialize_array(size,maxRange,dupe)
    else:
        arr = initialize_array(size,maxRange,dupe)
    
    start = time.time()
    hybridSort(arr,sValue)
    end = time.time()
    print("Hybrid Sort Key Comparisons: ",hybridSortKeyComparision, " Time Taken: ",end-start)
    
    start = time.time()
    merge_sort(arr)
    end = time.time()
    print("Merge Sort Key Comparisons: ",mergeSortKeyComparision, " Time Taken: ",end-start)


## To run part C.i
fixedS_VS_arraySize(15,randomNumRange,7,True)

## To run part C.ii
##fixedArraySize_VS_sValue(1,50,1,10000,50,True)

## To run part C.iii
##differentSValuesVSDifferentArraySize(1,50,1,randomNumRange,5,True)

## To run part D
##hybridVsMerge(100000, randomNumRange, 10, True)
