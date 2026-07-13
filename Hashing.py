# prestoring values into some data structure like list/dict/set and fetching it when required is called hashing. 

"""Print the frequency of m[i] in n 
n = [5,3,2,2,1,5,5,7,5,10]
m = 10,111,1,9,5,67,2]
all the numbers in n will be less than or equal to 10


"""
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

result = []
hash_list = [0] * (max(n) + 1)

for i in range(len(n)):
    hash_list[n[i]] += 1

for i in m:
    if i <= max(n):
        result.append(hash_list[i])
    else:
        result.append(0)

print(result)

#Method 2 using dict
hm = {}
num = len(n)
for i in range(0,num):
    hm[n[i]] = hm.get(n[i],0)+1
print(hm)



#Question 
"""Count Frequency of Elements
Given an array, count the frequency of each element.
Example:
Input: [1,2,2,3,1,4,2]
Output: {1:2, 2:3, 3:1, 4:1}"""

n = [1,2,2,3,1,4,2]
d = {}
for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
#Time Complexity: O(n) where n is the length of the input array. We iterate through the array once to count the frequencies.
#Space Complexity: O(n) in the worst case, if all elements in the array are unique, we would store each element in the frequency dictionary. However, if the range of possible values is limited (e.g., 1 to 100), the space complexity can be considered O(1) as we will at most store a fixed number of unique keys in the dictionary.

"""
Find Highest Frequency Element
Return the element with maximum frequency.
Input: [1,2,2,3,3,3,4]
Output: 3
"""

n = [1,2,2,3,3,3,4]
d1= {}
c = 0
b = None
for i in n:
    d1[i] = d1.get(i,0)+1
for k,v in d1.items():
    if v > c:
        c = v
        b = k
print(b)

#Time Complexity: O(n) where n is the length of the input array. We iterate through the array once to count the frequencies and then iterate through the dictionary to find the element with the maximum frequency.
#Space Complexity: O(n) in the worst case, if all elements in the array are unique, we would store each element in the frequency dictionary. However, if the range of possible values is limited (e.g., 1 to 100), the space complexity can be considered O(1) as we will at most store a fixed number of unique keys in the dictionary.


"""
Check if Two Strings are Anagrams
Input: "listen", "silent"
Output: True
"""
s1 = "listen"
s2 = "silent"
d = {}

if len(s1) != len(s2):
    print(False)
else:
    for i in s1:
        d[i] = d.get(i, 0) + 1

    flag = True
    for j in s2:
        if j not in d or d[j] == 0:
            flag = False
            break
        d[j] -= 1

    print(flag)
#Time Complexity: O(n) where n is the length of the input strings. We iterate through each string once to count the frequencies and check for anagrams.
#Space Complexity: O(n) in the worst case, if all characters in the strings are unique, we would store each character in the frequency dictionary. However, if the range of possible characters is limited (e.g., lowercase English letters), the space complexity can be considered O(1) as we will at most store a fixed number of unique keys in the dictionary.


"""
First Non-Repeating Character
Input: "aabbcde"
Output: 'c'
"""
s="aabbcde"
d = {}
for i in s:
    d[i] = d.get(i,0)+1
for k,v in d.items():
    if v == 1:
        print(k)
        break
#Time Complexity: O(n) where n is the length of the input string. We iterate through the string once to count the frequencies and then iterate through the dictionary to find the first non-repeating character.
#Space Complexity: O(n) in the worst case, if all characters in the string are unique, we would store each character in the frequency dictionary. However, if the range of possible characters is limited (e.g., lowercase English letters), the space complexity can be considered O(1) as we will at most store a fixed number of unique keys in the dictionary.

"""
Least Non-Repeating Character
Input: "aabbcde"
Output: 'c'
"""
# cook your dish here
s="aabbcde"
d = {}
for i in s:
    d[i] = d.get(i,0)+1
print(min((k for k,v in d.items() if v == 1)))
#Time Complexity: O(n) where n is the length of the input string. We iterate through the string once to count the frequencies and then iterate through the dictionary to find the least non-repeating character.
#Space Complexity: O(n) in the worst case, if all characters in the string are unique, we would store each character in the frequency dictionary. However, if the range of possible characters is limited (e.g., lowercase English letters), the space complexity can be considered O(1) as we will at most store a fixed number of unique keys in the dictionary.




"""Frequencies in a Limited Array
You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

Examples:

Input: arr[] = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.
Input: arr[] = [3, 3, 3, 3]
Output: [0, 0, 4, 0]
Explanation: We have: 1 occurring 0 times, 2 occurring 0 times, 3 occurring 4 times, and 4 occurring 0 times.
Input: arr[] = [1]
Output: [1]
Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()
"""

class Solution:
    def frequencyCount(self, arr):
        #  code here
        d= {}
        a = []
        for i in arr:
            d[i] = d.get(i,0)+1
        for j in range(1,len(arr)+1):
            a.append(d.get(j,0))
        return a
    

#Time complexity :o(n)
#Space complexity : o(n)

"""Find the Frequency
Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

Examples :

Input: arr = [1, 1, 1, 1, 1], x = 1
Output: 5
Explanation: Frequency of 1 is 5.
Input: arr = [1, 2, 3, 3, 2, 1], x=2
Output: 2
Explanation: Frequency of 2 is 2.
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105
1 <= x <= 105
"""

"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        d = {}
        for i in arr:
            d[i] = d.get(i,0)+1
        return d.get(x,0)
    
#Time complexity :o(n)
#Space complexity : o(n)

