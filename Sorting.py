#A process of arranging elements of a collection into a specific order, such as numerical, alphabetical or chronological

#1. selection sort
class sel_sort():
    def selection(self,nums):
        n = len(nums)
        for i in range(0,n):
            min_ind = i
            for j in range(i+1,n):
                if nums[j]< nums[min_ind]:
                    min_ind = j
            nums[i],nums[min_ind] = nums[min_ind], nums[i]
        return nums

obj = sel_sort()
nums = [5,7,8,4,1,6,9,2]
print(obj.selection(nums))


print("//////////////---------------------////////////")

class sel_sort():
    def selection(self,nums):
        n = len(nums)
        for i in range(0,n):
            max_ind = i
            for j in range(i+1,n):
                if nums[j] > nums[max_ind]:
                    max_ind = j
            nums[i],nums[max_ind] = nums[max_ind], nums[i]
        return nums

obj = sel_sort()
nums = [5,7,8,4,1,6,9,2]
print(obj.selection(nums))

"""
time complexity : o(n^2)
space complexity : o(1)
"""

#2. bubble sort
class bubble():
    def bubble_sort(self,nums):
        n = len(nums)
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if nums[j] > nums[j+1]:                              #Ascending order
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums
obj = bubble()
nums = [5,8,1,6,9,2,4]
print(obj.bubble_sort(nums))


print("///////////////////////------------------------------------////////////////////")

class bubble():
    def bubble_sort(self,nums):
        n = len(nums)
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if nums[j] < nums[j+1]:                              #Descending order
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums
obj = bubble()
nums = [5,8,1,6,9,2,4]
print(obj.bubble_sort(nums))


"""
Time complexity : o(n^2)
space complexity : o(1)
"""



#Inserction sort
class insertion():
    def insertion_sort(self,nums):
        n = len(nums)
        for i in range(1,n):
            key = nums[i]
            j = i-1
            while j >= 0 and nums[j] > key :     #Ascending order
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums
obj = insertion()
nums = [3,5,6,4,8,9,10,7,1]
print(obj.insertion_sort(nums))



print("///////////////--------------------/////////////////////")

class Insertion:
    def insertion_sort(self, nums):
        n = len(nums)

        for i in range(1, n):
            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] < key:    #Descending order
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key

        return nums

obj = Insertion()
nums = [3, 5, 6, 4, 8, 9, 10, 7, 1]
print(obj.insertion_sort(nums))



# merge sort

class merge_sort():

    def merge_array(self,left, right):
        n = len(left)
        m = len(right)

        r = []
        i, j = 0, 0

        while i < n and j < m:
            if left[i] <= right[j]:
                r.append(left[i])
                i += 1
            else:
                r.append(right[j])
                j += 1

        while i < n:
            r.append(left[i])
            i += 1

        while j < m:
            r.append(right[j])
            j += 1

        return r

    def merge_sort(self,nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left_arr = nums[:mid]
        right_arr = nums[mid:]

        left = self.merge_sort(left_arr)
        right = self.merge_sort(right_arr)

        return self.merge_array(left, right)

obj = merge_sort()
nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]
print(obj.merge_sort(nums))

"""
Time Complexity

T(n)=2T(n/2)+n

Time Complexity: O(n log n)
Space Complexity: O(n) (for the temporary merged arrays)
"""


"""
Why merge_sort.merge_sort(left_arr)?

Your method is defined without self:

def merge_sort(nums):
Since there is no self, it is not an instance method.

Therefore, it must be called using the class name:

merge_sort.merge_sort(left_arr)
Why merge_sort.merge_sort(nums) in the output?
merge_sort() belongs to the class merge_sort.
No object is being used.

So you call it directly through the class:

print(merge_sort.merge_sort(nums))
Why didn't we create obj = merge_sort()?
Creating an object is useful when methods use self.
Your methods do not have self.
Therefore, an object is unnecessary.
What happens if we create an object?
obj = merge_sort()
obj.merge_sort(nums)

Python internally does:

merge_sort.merge_sort(obj, nums)

But your method accepts only one argument:

def merge_sort(nums):

So Python raises:

TypeError: merge_sort() takes 1 positional argument but 2 were given
When should we create an object?

Use an object when methods are defined like this:

class MergeSort:
    def merge_sort(self, nums):
        ...

Then:

obj = MergeSort()
obj.merge_sort(nums)

works because self receives obj.

Simple Rule

No self → Call using class name

MergeSort.merge_sort(nums)

With self → Create object and call using object

obj = MergeSort()
obj.merge_sort(nums)

"""
#quick sort
class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            p_index = self.partition(arr, low, high)

            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1

            while j >= low + 1 and arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j


arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]

obj = Solution()
obj.quickSort(arr, 0, len(arr) - 1)

print("Sorted array =", arr)

"""
Time Complexity
Best and Average Case: O(nlog⁡n). When the pivot divides the array into subarrays of nearly equal size, you get more balanced splits.
Worst Case: O(n2). If the pivot is consistently chosen poorly (for example, the smallest or largest element in each partition), each partition results in extremely unbalanced subarrays.
Space Complexity
Quick Sort is generally considered an in-place sort since it rearranges the array in-place.
Space complexity is O(log⁡n) for the recursion call stack in the best/average case. In the worst case, it can go up to O(n) because of the depth of the recursion tree.
"""