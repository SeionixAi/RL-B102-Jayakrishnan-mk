

# List comprehension

# # squares
# nums = [1, 2, 3, 4, 5]
# squares = [x**2 for x in nums];
# print(squares)

# # even
# nums = [10, 15, 20, 25, 30, 35, 40]
# evens = [x for x in nums if x%2 == 0];
# print(evens);

# # len
# words = ["apple", "banana", "kiwi", "grape", "orange"]
# lengthOfWord = [len(word) for word in words]
# print(lengthOfWord);

# # If the number is even, keep it as is.
# # If the number is odd, replace it with -1.
# nums = [2, 5, 8, 11, 14, 17]
# newNums = [num if num%2 == 0 else -1 for num in nums];
# print(newNums);

# # Create a new list containing only the numbers that:
# # are divisible by 2
# # and not divisible by 3
# nums = list(range(1, 31))
# newNumbers = [x for x in nums if x%2 == 0 and x%3 != 0]
# print(newNumbers);


# =================================================================

# Lambda fn


# square(5)
# squared = (lambda x: x * x)(5);
# print(squared);

# largest(10, 25)
# Write a lambda function that takes two numbers and returns the larger one.

# larger = (lambda x,y: x if x>y else y)
# print(larger(301,44));



# Sort the list by age (second element of each tuple) using the key parameter with a lambda function.

people = [
    ("John", 25),
    ("Alice", 20),
    ("Bob", 30),
    ("Emma", 22)
]

# o/p - [
#     ("Alice", 20),
#     ("Emma", 22),
#     ("John", 25),
#     ("Bob", 30)
# ]

people.sort(key=lambda person: person[1])
print(people);