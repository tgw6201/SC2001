import random
import time
import matplotlib.pyplot as plt
import math     #math for log2

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
    array_sizes = []
    key_comparisons = []
    times_taken = []
    
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
        array_sizes.append(10**i)
        key_comparisons.append(hybridSortKeyComparision)
        times_taken.append(end - start)
    
    # Visualization
    plt.figure()
    
    plt.subplot(1, 2, 1)
    plt.plot(array_sizes, key_comparisons, marker='o')
    plt.xscale('log')
    plt.xlabel('Array Size')
    plt.ylabel('Key Comparisons')
    plt.title(f'Hybrid Sort Key Comparisons for S = {sValue}')
    
    plt.subplot(1, 2, 2)
    plt.plot(array_sizes, times_taken, marker='o')
    plt.xscale('log')
    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title(f'Hybrid Sort Time Taken for S = {sValue}')
    
    plt.tight_layout()
    plt.show()
        
## Part C.ii
def fixedArraySize_VS_sValue(startingS,endingS,stepS,size,maxRandArr,dupe=True):
    global hybridSortKeyComparision
    s_values = []
    key_comparisons = []
    times_taken = []
    
    if(dupe):
            arr = initialize_array(size,maxRandArr,dupe) ##Enable this to fix the array values to allow comparison of S values' impact only. In theory, should make merging always the same
    else:
            arr = initialize_array(size,maxRandArr,dupe)

    for i in range(startingS,endingS+1,stepS):
        hybridSortKeyComparision = 0
        ##if(dupe):
        ##    arr = initialize_array(size,maxRandArr,dupe) ##what if we move this out of the for loop? we fix the N and n values by doing so we may have a better comparison
        ##else:
        ##    arr = initialize_array(size,maxRandArr,dupe)
        if (i==0): continue
        else:
            start = time.time()
            hybridSort(arr,i)
            end = time.time()
            print("S Value: ",i," Key Comparisons: ",hybridSortKeyComparision, " Time Taken: ",end-start)
            s_values.append(i)
            key_comparisons.append(hybridSortKeyComparision)
            times_taken.append(end - start)
    
    # Visualization
    plt.figure()
    
    plt.subplot(1, 2, 1)
    plt.plot(s_values, key_comparisons, marker='o')
    plt.yscale('log')
    plt.xlabel('S Value')
    plt.ylabel('Key Comparisons')
    plt.title(f'Hybrid Sort Key Comparisons for Array Size = {size}')
    
    plt.subplot(1, 2, 2)
    plt.plot(s_values, times_taken, marker='o')
    plt.xlabel('S Value')
    plt.ylabel('Time Taken (seconds)')
    plt.title(f'Hybrid Sort Time Taken for Array Size = {size}')
    
    plt.tight_layout()
    plt.show()

## Part C.iii
def differentSValuesVSDifferentArraySize(startingS,endingS,stepS,arrMaxRange,pwr10=5,dupe=True):
    global hybridSortKeyComparision
    
    optimal_S = startingS
    min_comparisons = float('inf')  # Initialize minimum comparisons to a high value
    
    for i in range(startingS,endingS+1,stepS):
        total_comparisons = 0
        total_time = 0
        
        # Iterate through array sizes
        for j in range(3,pwr10+1):
            hybridSortKeyComparision = 0
            if(dupe):
                arr = initialize_array(10**j,arrMaxRange,dupe)
            else:
                arr = initialize_array(10**j,arrMaxRange,dupe)
            start = time.time()
            hybridSort(arr,i)
            end = time.time()
            
            total_comparisons += hybridSortKeyComparision
            total_time += (end - start)
            
            # Print the intermediate results
            print("S Value: ",i," ArraySize: ",10**j," Key Comparisons: ",hybridSortKeyComparision, " Time Taken: ",end-start)
        print("\n")
        
        # Check if current S value gives the least comparisons
        if total_comparisons < min_comparisons:
            min_comparisons = total_comparisons
            optimal_S = i
        
        print(f"Total Comparisons for S={i}: {total_comparisons}, Total Time: {total_time}")
        print("\n")
    
    print(f"Optimal S Value: {optimal_S} with {min_comparisons} key comparisons")
    return optimal_S
        

## Part D
def hybridVsMerge(size, maxRange, sValue, dupe):
    global mergeSortKeyComparision, hybridSortKeyComparision
    
    hybridSortKeyComparision = 0
    mergeSortKeyComparision = 0
    
    if(dupe):
        arr = initialize_array(size,maxRange,dupe)
    else:
        arr = initialize_array(size,maxRange,dupe)
    
    # Hybrid Sort
    start = time.time()
    hybridSort(arr,sValue)
    #end = time.time()
    #print("Hybrid Sort Key Comparisons: ",hybridSortKeyComparision, " Time Taken: ",end-start)
    hybrid_time = time.time() - start
    hybrid_key_comparisons = hybridSortKeyComparision
    
    # Merge Sort
    start = time.time()
    merge_sort(arr)
    end = time.time()
    print("Merge Sort Key Comparisons: ",mergeSortKeyComparision, " Time Taken: ", end-start)
    merge_time = time.time() - start
    merge_key_comparisons = mergeSortKeyComparision
    
    # Visualization
    algorithms = ['Hybrid Sort', 'Merge Sort']
    key_comparisons = [hybrid_key_comparisons, merge_key_comparisons]
    times_taken = [hybrid_time, merge_time]
    
    plt.figure()
    
    plt.subplot(1, 2, 1)
    bars = plt.bar(algorithms, key_comparisons, color=['blue', 'orange'])
    plt.yscale('log')
    plt.ylabel('Key Comparisons')
    plt.title(f'Comparison of Hybrid and Merge Sort (Array Size = {size})')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.0f}', ha='center', va='bottom')
    
    plt.subplot(1, 2, 2)
    bars = plt.bar(algorithms, times_taken, color=['blue', 'orange'])
    plt.ylabel('Time Taken (seconds)')
    plt.title(f'Comparison of Hybrid and Merge Sort (Array Size = {size})')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.4f}', ha='center', va='bottom')
    
    
    plt.tight_layout()
    plt.show()


## To run part C.i
#fixedS_VS_arraySize(10,randomNumRange,7,True)

## To run part C.ii
##fixedArraySize_VS_sValue(0,180,1,10000,10000,False)

## To run part C.iii
##differentSValuesVSDifferentArraySize(1,5,1,randomNumRange,3,True)

## To run part D
#hybridVsMerge(10000000, randomNumRange, 10, True)

