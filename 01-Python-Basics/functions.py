# Python Functions


# -------------------------
# 1. Simple Function
# -------------------------

def greet():
    print("Hello, Welcome to Python!")


greet()


# -------------------------
# 2. Function with Parameter
# -------------------------

def greet_user(name):
    print("Hello", name)


greet_user("Sejal")
greet_user("Rahul")


# -------------------------
# 3. Function with Multiple Parameters
# -------------------------

def add_numbers(a, b):
    result = a + b
    print("Addition:", result)


add_numbers(10, 20)


# -------------------------
# 4. Function with Return
# -------------------------

def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# -------------------------
# 5. Default Parameter
# -------------------------

def greet_person(name="Student"):
    print("Hello", name)


greet_person()
greet_person("Sejal")


# -------------------------
# 6. Keyword Arguments
# -------------------------

def student_info(name, age, marks):
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)


student_info(
    name="Rahul",
    age=22,
    marks=85
)


# -------------------------
# 7. Data Science Example
# -------------------------

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)

    return average


marks = [80, 75, 90, 85, 70]

average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)




# # Conceptes covered 
Function
Parameter
Argument
Return value
Default parameter
Keyword argument
Function reuse

