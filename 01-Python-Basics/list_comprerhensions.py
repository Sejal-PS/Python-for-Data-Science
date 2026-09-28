# ============================================
# LIST COMPREHENSIONS IN PYTHON
# ============================================

# List comprehension provides a short and
# readable way to create lists.


# ============================================
# BASIC LIST COMPREHENSION
# ============================================

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# ============================================
# LIST COMPREHENSION WITH CONDITION
# ============================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# ============================================
# ODD NUMBERS
# ============================================

odd_numbers = [
    number for number in numbers
    if number % 2 != 0
]

print(odd_numbers)


# ============================================
# STRING LIST
# ============================================

names = ["alice", "bob", "charlie"]

uppercase_names = [
    name.upper()
    for name in names
]

print(uppercase_names)


# ============================================
# LENGTH OF STRINGS
# ============================================

words = ["Python", "Data", "Science"]

word_lengths = [
    len(word)
    for word in words
]

print(word_lengths)


# ============================================
# IF-ELSE IN LIST COMPREHENSION
# ============================================

numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)


# ============================================
# NESTED LIST COMPREHENSION
# ============================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    value
    for row in matrix
    for value in row
]

print(flattened)


# ============================================
# DICTIONARY WITH LIST COMPREHENSION
# ============================================

numbers = [1, 2, 3, 4, 5]

square_dict = {
    number: number ** 2
    for number in numbers
}

print(square_dict)


# ============================================
# PRACTICAL DATA SCIENCE EXAMPLE
# ============================================

marks = [45, 78, 92, 56, 88, 34, 67]

passed_marks = [
    mark for mark in marks
    if mark >= 40
]

print(passed_marks)


# ============================================
# PRACTICE
# ============================================

# 1. Create a list of squares from 1 to 20.
# 2. Create a list containing only even numbers.
# 3. Convert a list of names to uppercase.
# 4. Find words with more than 5 characters.
# 5. Create a dictionary containing numbers and their cubes.
