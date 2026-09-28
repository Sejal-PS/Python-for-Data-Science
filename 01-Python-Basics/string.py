# ============================================
# STRINGS IN PYTHON
# ============================================

# A string is a sequence of characters.
# Strings can be created using single or double quotes.

name = "Python"
course = 'Data Science'

print(name)
print(course)


# ============================================
# STRING INDEXING
# ============================================

text = "Python"

print(text[0])
print(text[1])
print(text[-1])


# ============================================
# STRING SLICING
# ============================================

print(text[0:3])
print(text[2:6])
print(text[:4])
print(text[2:])
print(text[::-1])


# ============================================
# STRING LENGTH
# ============================================

print(len(text))


# ============================================
# STRING METHODS
# ============================================

message = "  Python for Data Science  "

print(message.upper())
print(message.lower())
print(message.title())
print(message.strip())


# ============================================
# REPLACE
# ============================================

text = "I am learning Python"

new_text = text.replace("Python", "Data Science")

print(new_text)


# ============================================
# SPLIT
# ============================================

sentence = "Python is easy to learn"

words = sentence.split()

print(words)


# ============================================
# JOIN
# ============================================

words = ["Python", "for", "Data", "Science"]

sentence = " ".join(words)

print(sentence)


# ============================================
# STRING CHECKING
# ============================================

text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())


# ============================================
# STRING FORMATTING
# ============================================

name = "Sejal"
age = 22

print(f"My name is {name} and I am {age} years old.")


# ============================================
# ESCAPE CHARACTERS
# ============================================

print("Python\nData Science")
print("Python\tData Science")


# ============================================
# PRACTICAL EXAMPLE
# ============================================

student_name = "Sejal"
course_name = "Python for Data Science"

print(f"Student: {student_name}")
print(f"Course: {course_name}")


# ============================================
# PRACTICE
# ============================================

# 1. Create a string containing your name.
# 2. Print the first and last character.
# 3. Reverse a string using slicing.
# 4. Convert a string to uppercase.
# 5. Count the number of characters.
# 6. Split a sentence into words.
# 7. Join a list of words into a sentence.
