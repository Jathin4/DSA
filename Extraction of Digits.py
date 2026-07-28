class Extract:
    def extract_digit(self, n):
        while n > 0:
            print(n % 10)
            n //= 10

obj = Extract()
n = int(input("Enter the number: "))
obj.extract_digit(n)

# Time Complexity : O(d)
# Space Complexity: O(1)
# Explanation: The loop runs once for each digit of the number and uses only constant extra memory.


# 1. count no.of digits 
class digits():
    def count_digits(self,n):
        c = 0
        while n > 0:
            n //= 10
            c += 1
        return c
obj = digits()
n = int(input("enter no.of digits : "))
print(obj.count_digits(n))

# Time Complexity : O(d)
# Space Complexity: O(1)
# Explanation: The number is divided by 10 until it becomes 0, visiting each digit exactly once.

#2. Resever a number 
class reverse():
    def reverse_number(self,n):
        rev = 0
        while n > 0:
            l_d = n % 10
            rev = (rev*10)+l_d
            n //= 10
        return rev
obj = reverse()
n = int(input("enter the number: "))
print(obj.reverse_number(n))

# Time Complexity : O(d)
# Space Complexity: O(1)
# Explanation: Each digit is processed once to construct the reversed number.


#3. Armstrong number - a number equal to the sum of its own digits , each raised to the power of the total number of digits in the number 

class Armstrong:
    def armstrong_number(self, n):
        arm = 0
        l = len(str(n))
        num = n

        while num > 0:
            ld = num % 10
            arm += ld ** l
            num //= 10

        if arm == n:
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")


obj = Armstrong()
n = int(input("Enter the number: "))
obj.armstrong_number(n)

# Time Complexity : O(d)
# Space Complexity: O(1)
# Explanation: The algorithm visits every digit once and performs constant-time operations for each digit.


#4. print factors of a number 
#(i) with out sorting the list
from math import sqrt

class factor:
    def factor_number(self, n):
        r = []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                r.append(i)
                if n // i != i:
                    r.append(n // i)
        return r

obj = factor()
n = int(input("Enter the number: "))
print(obj.factor_number(n))

# Time Complexity : O(√n)
# Space Complexity: O(f)
# Explanation: Only numbers up to √n are checked, and all factors are stored in the list.


#(ii) with sorting the factors 
class factor:
    def factor_number(self, n):
        r = []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                r.append(i)
                if n // i != i:
                    r.append(n // i)
        r.sort()
        return r
obj = factor()
n = int(input("Enter the number: "))
print(obj.factor_number(n))

# Time Complexity : O(√n + f log f)
# Space Complexity: O(f)
# Explanation: Finding factors takes O(√n), and sorting the factor list takes O(f log f).



#or we have another way which is n//2

class factor:
    def factor_number(self,n):
        r = []
        for i in range(1,(n//2)+1):
            if n%i == 0:
                r.append(i)
        r.append(n)
        return r
obj = factor()
n = int(input("enter the number"))
print(obj.factor_number(n))

# Time Complexity : O(n)
# Space Complexity: O(f)
# Explanation: The algorithm checks every number from 1 to n/2 for divisibility and stores the factors.