                                            # ARRAY INTERVIEW QUESTIONS #



# Problem 1 : Given an array containing n distinct numbers taken from 0 to n, find the missing number.

def missing_no (arr):
    n = len(arr)

    sum_of_expected = (n * (n + 1)) / 2
    actual_sum = sum(arr)
    missing_no = sum_of_expected - actual_sum
    return missing_no

arr1 = [1,2,4,5,0]
missing_number = missing_no(arr1)
print('The missing number from array is', int(missing_number))



# Problem 2 :  Find all the elements that appear twice in an array.
def findDuplicates(arr):
    duplicates = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

arr1 = [3,5,2,4,9,2,4,5,2,0,1,0,2,7,3]

dup = findDuplicates(arr1)
print('Duplicate element:',dup)



# Problem 3 : Determine if there are any duplicates in the array.
def hasDuplicate(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return True
            
    return False

arr1 = [0,2,3,1,7,0,8]
result = hasDuplicate(arr1)
if result:
    print("The array has duplicates")
else:
    print('The array does not have duplicates')



# Problem 4 : Remove duplicates from an array and return the new length.
def removing_dup(arr):
    n = len(arr)
    final_arr = []

    for i in range(n):
        if arr[i] not in final_arr:
                final_arr.append(arr[i])
    
    for i in range(len(final_arr)):
        arr = final_arr

    return(len(arr))

arr1 = [2,5,2,7,1,4,2,2,2,1,5,6]
result = removing_dup(arr1)
print('The length after removing duplicate elements (if any)', result)



# Problem 5 : Remove duplicates from a sorted array in-place and return the new length.
def remove_dup(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return n
    j = 0
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1
        
    arr[j] = arr[n-1]       # Copy the last element (unique or not) to the end
    return j+1              # Return the new length of the modified array

arr1 = [1,2,3,4,5]
result = remove_dup(arr1)
print('Length of modified array after removing duplicates is', result)