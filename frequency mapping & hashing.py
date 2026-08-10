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


class question2:
    def ques2(self,str):
        h = {}
        for i in range(len(str)):
            h[str[i]] = h.get(str[i],0)+1
        return h
obj = question2()
str = "geeksforgeeks"
print(obj.ques2(str))