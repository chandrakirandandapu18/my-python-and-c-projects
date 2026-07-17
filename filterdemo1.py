numbers = [10, 15, 20, 23, 30, 41, 50]

even = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even)
#----------------------------------------------------------------------------------------------------------------
names = ["Alice", "Bob", "Anil", "David", "Arjun", "Charlie"]

result = list(filter(lambda name: name.startswith("A"), names))

print(result)
#-----------------------------------------------------------------------------------------------------------------
marks = [90, 25, 67, 34, 45, 18, 80, 35]

passed = list(filter(lambda x: x >= 35, marks))

print("Passed students:", passed)
#---------------------------------------------------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 4, 5, 8, 11, 13, 15, 17, 20]

primes = list(filter(is_prime, numbers))

print("Prime numbers:", primes)