# ============================================
# FILE HANDLING IN PYTHON
# ============================================

# Python provides built-in functions for
# creating, reading, writing, and modifying files.


# ============================================
# WRITING TO A FILE
# ============================================

with open("sample.txt", "w") as file:
    file.write("Python for Data Science\n")
    file.write("Learning Python file handling.")


# ============================================
# READING A FILE
# ============================================

with open("sample.txt", "r") as file:
    content = file.read()

print(content)


# ============================================
# READING LINE BY LINE
# ============================================

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())


# ============================================
# APPENDING TO A FILE
# ============================================

with open("sample.txt", "a") as file:
    file.write("\nLearning Data Science.")


# ============================================
# READ ALL LINES
# ============================================

with open("sample.txt", "r") as file:
    lines = file.readlines()

print(lines)


# ============================================
# FILE MODES
# ============================================

# "r"  -> Read
# "w"  -> Write
# "a"  -> Append
# "x"  -> Create


# ============================================
# CHECK WHETHER FILE EXISTS
# ============================================

import os

if os.path.exists("sample.txt"):
    print("File exists.")
else:
    print("File does not exist.")


# ============================================
# FILE INFORMATION
# ============================================

if os.path.exists("sample.txt"):
    print("File size:", os.path.getsize("sample.txt"), "bytes")


# ============================================
# DELETE A FILE
# ============================================

# Be careful when deleting files.

# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")


# ============================================
# PRACTICAL DATA SCIENCE EXAMPLE
# ============================================

data = [
    "Alice,85\n",
    "Bob,90\n",
    "Charlie,78\n"
]

with open("students.txt", "w") as file:
    file.writelines(data)


with open("students.txt", "r") as file:
    student_data = file.readlines()

print(student_data)


# ============================================
# PRACTICE
# ============================================

# 1. Create a text file.
# 2. Write five student names into the file.
# 3. Read the file.
# 4. Append another student.
# 5. Count the number of lines in the file.
# 6. Check whether a file exists.
