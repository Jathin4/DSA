#Basic syntac
def greet():
    print("jathin")
greet()

# if we want multiple print 
c = 0
def greet(c):
    if c == 3:
        return 
    print("jathin")
    greet(c+1)
greet(c)
# this us head recursion means first job is printed then the function is called

c = 1

def greet(c):
    if c > 4:
        return

    print("jathin",c)
    greet(c + 1)

greet(c)

# this is tail recursion means frist function is called till the function exist , after that o/p is printed

# Questions on Recursion 
# 1. Print x , N times
# head recursion
def greet(x,n):
    if n == 0:
        return 
    print(x)
    greet(x,n-1)
greet("jathin",4)

#tail recursion
def greet(x,n):
    if n == 0:
        return
    greet(x,n-1)
    print(x)
greet("jathin",4)

# 2. Print 0 to n
# head recursion
def greet(i,n):
    if i >n :
        return
    print(i)
    greet(i+1,n)
greet(0,10)
    
# tail recursion
def greet(i,n):
    if i >n:
        return
    greet(i+1,n)
    print(n-i)
greet(0,10)

# 3. Print N to 0
def greet(n):
    if n < 0:
        return 
    print(n)
    greet(n-1)
greet(10)


def greet(n):
    if n < 0:
        return
    greet(n-1)
    print(n)
greet(10)


# Parameterized recursion
# 1. print sum of 1 to n
def greet(s,i,n):
    if i > n:
        return s
    return greet(s+i, i+1, n)
print(greet(0,1,10))

#Functional recursion
def greet(n):
    if n ==1:
        return 1
    return n + greet(n-1)
print(greet(10))

#1. factorial of a number
def greet(n):
    if n == 1:
        return 1
    return n* greet(n-1)
print(greet(5))



# Reverse an array using recursion
# basic syntax
def greet(n,l,r):
    if l >= r :
        return
    n[l],n[r] = n[r],n[l]
    return greet(n,l+1,r-1)
n = [5,4,3,2,1]
greet(n,0,len(n)-1)
print(n)

#1. palindrome or not 
def greet(s,l,r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
s = "MOM"
print(greet(s,0,len(s)-1))

# 2.Fibonacci series

def greet(n):
    if n == 0 or n == 1:
        return 1
    return greet(n-1)+greet(n-2)
print(greet(5))
    


a = int(input("enter first number"))
b = int(input("enter 2nd number"))
avg = (a+b)/2
print(avg)

