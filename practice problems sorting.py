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

