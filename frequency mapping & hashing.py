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