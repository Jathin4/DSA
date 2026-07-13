#Frequency map or dictonary in python is a data structure that stores the frequency of each element in a collection. It is implemented using a dictionary, where the keys are the unique elements and the values are their corresponding frequencies.


#Method 1: Using a for loop to iterate through the list and update the frequency map.
nums = [5,6,7,7,7,1,9,111,1,1,5,1,1]

class frequency_map:
    def __init__(self,nums, freq_map={}):
        self.nums = nums
        self.freq_map = freq_map

        for i in range(0,len(self.nums)):
            if self.nums[i] in self.freq_map:
                self.freq_map[self.nums[i]] += 1
            else:
                self.freq_map[self.nums[i]] = 1
        
    def get_freq(self,freq_map):
        return freq_map

obj = frequency_map(nums)
print(obj.get_freq (obj.freq_map))


""" 
time complexity: O(n) where n is the number of elements in the input list.
space complexity: O(k) where k is the number of unique elements in the input list, as we are storing the frequency of each unique element in the frequency map."""

#Method 2 
class freq_map:
    def __init__(self, nums,hash_map={}):
        self.nums = nums
        self.hash_map = hash_map
        for i in range(0,len(self.nums)):
            self.hash_map[self.nums[i]] = self.hash_map.get(self.nums[i],0) + 1
        def get_freq(self,hash_map):
            return hash_map
obj = freq_map(nums)
nums = [5,6,7,7,7,1,9,111,1,1,5,1,1]
print(obj.get_freq(obj.hash_map))

"""
self.hash_map.get(self.nums[i],0) is a method that retrieves the value associated with the key self.nums[i] from the hash_map. If the key does not exist in the hash_map, it returns 0 as the default value. This allows us to increment the frequency count for each element in the nums list without having to check if the key already exists in the hash_map.

.get : is used to retrieve the value associated with a specific key from a dictionary. It takes two arguments: the key you want to retrieve and an optional default value that is returned if the key is not found in the dictionary. If the key exists in the dictionary, it returns the corresponding value; otherwise, it returns the default value (or None if no default value is provided).

time complexity: O(1) for delete and update operations, O(n) for iterating through the input list to build the frequency map.
space complexity: O(k) where k is the number of unique elements in the input list, as we are storing the frequency of each unique element in the frequency map.
"""