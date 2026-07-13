#brute force method 
def printFactors(n):
    print("The factors of", n, "are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
num = 12
printFactors(num)

"""
Time complexity: O(n) : The loop runs from 1 to n, so the time complexity is O(n).
Space complexity: O(1) : We are using a constant amount of space to store the factors, so the space complexity is O(1).
"""

#better method
def printFactors(n):
    print("The factors of", n, "are:")
    for i in range(1, int(n//2) + 1):
        if n % i == 0:
            print(i)
    print(n)
n = 12
printFactors(n)
"""
Time complexity: O(n/2) : The loop runs from 1 to n/2, so the time complexity is O(n/2), which simplifies to O(n).
Space complexity: O(1) : We are using a constant amount of space to store the factors, so the space complexity is O(1).
"""

#optimal method
class PrintFactors:
    def Factors(n):
        print("The factors of", n, "are:")
        a = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                a.append(i)
                if i != n // i:
                    a.append(n // i)

        a.sort()
        return a


n = 12
print(PrintFactors.Factors(n))
"""
Time complexity: O(sqrt(n)) : The loop runs from 1 to sqrt(n), so the time complexity is O(sqrt(n)).
Space complexity: O(k) : We are using a list to store the factors, where k is the number of factors. In the worst case, when n is a perfect square, there can be at most 2*sqrt(n) factors, so the space complexity is O(sqrt(n))."""