# class Extract:
#     def extract_digit(self, n):
#         while n > 0:
#             print(n % 10)
#             n //= 10

# obj = Extract()
# n = int(input("Enter the number: "))
# obj.extract_digit(n)


# # 1. count no.of digits 
# class digits():
#     def count_digits(self,n):
#         c = 0
#         while n > 0:
#             n //= 10
#             c += 1
#         return c
# obj = digits()
# n = int(input("enter no.of digits : "))
# print(obj.count_digits(n))

# #2. Resever a number 
# class reverse():
#     def reverse_number(self,n):
#         rev = 0
#         while n > 0:
#             l_d = n % 10
#             rev = (rev*10)+l_d
#             n //= 10
#         return rev
# obj = reverse()
# n = int(input("enter the number: "))
# print(obj.reverse_number(n))


# #3. Armstrong number - a number equal to the sum of its own digits , each raised to the power of the total number of digits in the number 

# class Armstrong:
#     def armstrong_number(self, n):
#         arm = 0
#         l = len(str(n))
#         num = n

#         while num > 0:
#             ld = num % 10
#             arm += ld ** l
#             num //= 10

#         if arm == n:
#             print("Armstrong Number")
#         else:
#             print("Not an Armstrong Number")


# obj = Armstrong()
# n = int(input("Enter the number: "))
# obj.armstrong_number(n)


#4. print factors of a number 
#(i) with out sorting the list
from math import sqrt

class Sorting:
    def sort_number(self, n):
        r = []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                r.append(i)
                if n // i != i:
                    r.append(n // i)
        return r

obj = Sorting()
n = int(input("Enter the number: "))
print(obj.sort_number(n))

