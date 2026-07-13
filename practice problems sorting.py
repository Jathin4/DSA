#1. Maximum Perimeter Triangle from array
"""
Given an array arr[] of positive integers. Find out the maximum perimeter of the triangle from the array.

Note: Return -1, if it is not possible to construct a triangle.

Examples:

Input: arr[] = [6, 1, 6, 5, 8, 4]
Output: 20
Explanation: Triangle formed by  8,6 & 6 has perimeter 20, which is the max possible.

Input: arr[] = [7, 55, 20, 1, 4, 33, 12]
Output:  -1
Explanation: The triangle is not possible because the condition: the sum of two sides should be greater than third is not fulfilled here
"""
#native approach --- ignore this one , here i have wrote the code as all the possible triangles 
class perimeter:
    def per_triangle(self, arr):
        n = len(arr)
        b = []

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if (arr[i] + arr[j] > arr[k] and
                        arr[j] + arr[k] > arr[i] and
                        arr[k] + arr[i] > arr[j]):

                        b.append([arr[i], arr[j], arr[k]])

        return b

obj = perimeter()
arr = [6, 1, 6, 5, 8, 4]

print(obj.per_triangle(arr))

#optimal solution ---- correct code according to question 
class perimeter:
    def p_t(self,a):
        a.sort(reverse=True)
        n = len(a)
        for i in range(n-2):
            if a[i] < a[i+1]+a[i+2]:
                return a[i]+a[i+1]+a[i+2]
        return -1
obj = perimeter()
a= [6, 1, 6, 5, 8, 4]
print("the perimeter of triangle is : ",obj.p_t(a))




#2.Maximize array sum after K negations
"""
Given an array of size n and an integer k. We must modify array k number of times. In each modification, we can replace any array element arr[i] by -arr[i]. The task is to perform this operation in such a way that after k operations, the sum of the array is maximum.

Examples : 

Input : arr[] = [-2, 0, 5, -1, 2], k = 4
Output: 10
Explanation:
1. Replace (-2) by -(-2), array becomes [2, 0, 5, -1, 2]
2. Replace (-1) by -(-1), array becomes [2, 0, 5, 1, 2]
3. Replace (0) by -(0), array becomes [2, 0, 5, 1, 2]
4. Replace (0) by -(0), array becomes [2, 0, 5, 1, 2]

Input : arr[] = [9, 8, 8, 5], k = 3
Output: 20
Explanation: Negate 5 three times. Array will become [9, 8, 8, -5]. 
"""

def maximizeSum(arr, k):
    n = len(arr)
    
    # Sort the array 
    arr.sort()
    
    # Use k to convert negative integers 
    # into positive integers.
    i = 0
    while i < n and k > 0 and arr[i] <= 0:
        arr[i] *= -1
        k -= 1
        i += 1
    
    # If k > 1, we can repeatedly negate 
    # the same value even times, so its 
    # value will remain the same.
    k = k % 2
    
    # Calculate sum of array.
    total_sum = sum(arr)
    
    if k == 0:
        return total_sum
    
    # If k == 1, we have to negate the
    # minimum value.
    minIndex = min(arr)
    
    return total_sum - 2 * minIndex

arr = [-2, 0, 5, -1, 2]
k = 4
print(maximizeSum(arr, k))


#3.Sum of minimum absolute differences in an array
"""
Given an array of n distinct integers. The task is to find the sum of minimum absolute difference of each array element. For an element arr[i] present at index i in the array, its minimum absolute difference is calculated as: 

Min absolute difference (arr[i]) = min(abs(arr[i] - arr[j])), where 0 <= j < n and j != i and abs is the absolute value. 
Examples: 

Input : arr = [4, 1, 5]
Output : 5
Explanation: Sum of minimum absolute differences is |4-5| + |1-4| + |5-4| = 1 + 3 + 1 = 5

Input : arr = [5, 10, 1, 4, 8, 7]
Output : 9
Explanation: Sum of minimum absolute differences is 
|5-4| + |10-8| + |1-4| + |4-5| + |8-7| + |7-8| = 1 + 2 + 3 + 1 + 1 + 1 = 9

Input : arr = [12, 10, 15, 22, 21, 20, 1, 8, 9]
Output : 18
"""

def minSumDiff(arr):
    n = len(arr)
    
    # Sort the array
    arr.sort()
    
    sum = 0
    
    # For first element, the closest 
    # is the second element
    sum += arr[1] - arr[0]
    
    # For last element, the closest 
    # is the second-last element
    sum += arr[n-1] - arr[n-2]
    
    # For middle elements, check both 
    # left and right neighbors
    for i in range(1, n-1):
        leftDiff = arr[i] - arr[i-1]
        rightDiff = arr[i+1] - arr[i]
        
        # Add the minimum of left 
        # and right differences
        sum += min(leftDiff, rightDiff)
    
    return sum


arr = [4, 1, 5]
print(minSumDiff(arr))

#4.Sort an array in wave form
"""
Given a sorted array arr[] of integers (in ascending order), rearrange the elements in-place to form a wave-like array.
An array is said to be in wave form if it satisfies the following pattern: arr[0] ≥ arr[1] ≤ arr[2] ≥ arr[3] ≤ arr[4] ≥ ...
In other words, every even-indexed element should be greater than or equal to its adjacent odd-indexed elements (if they exist).

Note: The given array is sorted in ascending order, and modify the given array in-place without returning a new array.

Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

Input: arr[] = [2, 4, 7, 8, 9, 10]
Output: [4, 2, 8, 7, 10, 9]
Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.
"""
def sortInWave(arr):
    
    n = len(arr)
   
    # swap adjacent elements
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]


arr = [1, 2, 3, 4, 5]
sortInWave(arr)
for i in range(0,len(arr)):
    print (arr[i],end=" ")


# 5.Chocolate Distribution Problem

"""Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

Each student gets exactly one packet.
The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.
Examples:

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3 
Output: 2 
Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, that is 2. 

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 5 
Output: 7
Explanation: If we distribute chocolate packets {3, 2, 4, 9, 7}, we will get the minimum difference, that is 9 - 2 = 7."""

def findMinDiff(arr, m):
    n = len(arr)

    # Sort the given packets
    arr.sort()

    minDiff = float('inf')

    for i in range(n - m + 1):

        # calculate difference of current window
        diff = arr[i + m - 1] - arr[i]

        # if current difference is smaller
        # then update the minimum difference
        if diff < minDiff:
            minDiff = diff

    return minDiff


arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(findMinDiff(arr, m))


#6.Pair with the given difference

"""

Given an unsorted array and an integer x, the task is to find if there exists a pair of elements in the array whose absolute difference is x. 

Examples: 

Input: arr[] = [5, 20, 3, 2, 50, 80], x = 78
Output: true
Explanation: The pair is {2, 80}.

Input: arr[] = [90, 70, 20, 80, 50], x = 45
Output: false
Explanation: No such pair exists."""

# Python program to find a pair with the given difference

def findPair(arr, x):
    n = len(arr)
    
    # Sort the array.
    arr.sort()
    
    j = 1
    
    for i in range(n):
        
        # Increment j till difference is 
        # less than x.
        while j < n and arr[j] - arr[i] < x:
            j += 1
        
        # If difference is x
        if j < n and i != j and arr[j] - arr[i] == x:
            return True
    
    return False

arr = [5, 20, 3, 2, 50, 80]
x = 78
if findPair(arr, x):
    print("true")
else:
    print("false")