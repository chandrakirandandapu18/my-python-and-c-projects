numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print(squares)
#--------------------------------------------------------------------------------
word = "python"

vowels = [ch for ch in word if ch in "aeiou"]

print(vowels)
#--------------------------------------------------------------------------------
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = {x for x in numbers}

print(unique)
#--------------------------------------------------------------------------------
square = {x: x**2 for x in range(1, 6)}

print(square)
#--------------------------------------------------------------------------------
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

for row in table:
    print(row)