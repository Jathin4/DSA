from unittest import result

from sqlalchemy import union


class frequency_mapping:
    def freq_map(self,n):
        f = {}
        for i in range(0,len(n)):
            f[n[i]] = f.get(n[i],0)+1
        return f
obj = frequency_mapping()
n = [5,6,7,7,1,9,111,1,1,5,1,1]
print(obj.freq_map(n))

"""
Time Complexity: O(n) — because the loop runs n times, and dictionary get() and insertion are O(1) average case.
Space Complexity: O(k) — because the dictionary stores only the unique elements, where k = number of distinct elements; worst case O(n).
"""

#Questions 
#!.Check if an array is subset of another array
class question1:
    def ques1(self,a,b):
        h = set(a)
        for i in b:
            if i not in h:
                return False
        return True
obj = question1()
a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1] 
print(obj.ques1(a,b))

#2. Frequency of each character in a String using Hashing
class question2:
    def ques2(self,str):
        h = {}
        for i in range(len(str)):
            h[str[i]] = h.get(str[i],0)+1
        return h
obj = question2()
str = "geeksforgeeks"
print(obj.ques2(str))

#3. First non-repeating character in a String using Hashing
class question3:
    def ques3(self, s):
        h = {}

        
        for i in range(len(s)):
            h[s[i]] = h.get(s[i], 0) + 1

       
        for i in range(len(s)):
            if h[s[i]] == 1:
                return s[i]

        return "$"


obj = question3()
s = "geeksforgeeks"

print(obj.ques3(s))


#4. 1. Union with Duplicates
"""We are given two arrays a[] and b[] and the task is to find the union of both the arrays. Union of two arrays is an array having all distinct elements that are present in either array. The input arrays may contain duplicates.

Examples:

Input : a[] = {1, 2, 3, 2, 1}, b[] = {3, 2, 2, 3, 3, 2}
Output : {3, 2, 1}
Explanation: Each element in the output either belongs to array a or array b, and we need to print only one occurrence of such elements.

Input : a[] = {1, 2, 3}, b[] = {4, 5, 6}
Output : {1, 2, 3, 4, 5, 6}
Explanation: Each element in the output either belongs to array a or array b, and we need to print only one occurrence of such elements."""
class question4:
    def union(self, a, b):
        a.sort()
        b.sort()

        i = 0
        j = 0
        result = []

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1

            elif a[i] > b[j]:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j += 1

            else:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1

        # Remaining elements from a
        while i < len(a):
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        # Remaining elements from b
        while j < len(b):
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j += 1

        return result


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

obj = question4()
print(obj.union(a, b))


#5. Intersection of two arrays
class question5:
    def ques5(self, a, b):
        a.sort()
        b.sort()

        i = 0
        j = 0
        result = []

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                i += 1

            elif a[i] > b[j]:
                j += 1

            else:
                # Avoid duplicates
                if not result or result[-1] != a[i]:
                    result.append(a[i])

                i += 1
                j += 1

        return result


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

obj = question5()
print(obj.ques5(a, b))


#6. Missing Element in Range
"""
Given an array arr[] of integers and a range [low, high], find all the numbers within the range that are not present in the array. return the missing numbers in sorted order.

Examples:  

Input: arr[] = [10, 12, 11, 15], low = 10, high = 15
Output: [13, 14]
Explanation: Numbers 13 and 14 lie in the range [10, 15] but are not present in the array.

Input: arr[] = [1, 4, 11, 51, 15], low = 50, high = 55
Output: [50, 52, 53, 54, 55]
Explanation: Numbers 50, 52, 53, 54 and 55 lie in the range [50, 55] but are not present in the array."""

class question6:
    def ques6(self, l, h, a):

        s = []

        # Size of the range
        m = h - l + 1

        # Boolean array to mark present numbers
        present = [False] * m

        # Mark numbers that are present in the range
        for x in a:
            if l <= x <= h:
                present[x - l] = True

        # Find missing numbers
        for i in range(m):
            if not present[i]:
                s.append(l + i)

        return s


obj = question6()

l = 10
h = 15

a = [10, 12, 11, 15]

print(obj.ques6(l, h, a))