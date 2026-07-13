""" basic syntax of extraction of digits using loops """
class ExtractionOfDigitsUsingLoops:
    def extract_digits(num):
        n = num
        r = 0
        while n >0:
            l = n %10
            print(l)
            n = n//10   
obj = ExtractionOfDigitsUsingLoops
obj.extract_digits(54123)

#1. Count the number of digits in a number
class CountDigits:
    def count_digits(num):
        n = num
        count = 0
        while n > 0:
            l = n % 10
            count += 1
            n = n // 10
        print(count)
obj = CountDigits
obj.count_digits(54123)

#2. reverse a number 
class ReverseNumber:
    def reverse_number(num):
        n = num
        rev = 0
        while n >0:
            l = n%10
            rev = rev*10 + l
            n = n//10
        print(rev)
obj = ReverseNumber
obj.reverse_number(54123)

#3. check if a number is Amstrong or not

class ArmstrongNumber:
    def is_armstrong(num):
        n = num
        s = 0
        while n >0:
            l = n%10
            s += l**3
            n = n//10
        if s == num:
            print("Armstrong")
        else:
            print("Not Armstrong")
obj = ArmstrongNumber
obj.is_armstrong(153)


