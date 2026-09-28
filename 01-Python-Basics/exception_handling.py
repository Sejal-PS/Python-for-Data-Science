# ============================================
# EXCEPTION HANDLING IN PYTHON
# ============================================

# Exception handling allows us to handle
# runtime errors without stopping the program.


# ============================================
# BASIC TRY-EXCEPT
# ============================================

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Please enter a valid number.")


# ============================================
# DIVISION BY ZERO
# ============================================

try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================
# MULTIPLE EXCEPTIONS
# ============================================

try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print(result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# ============================================
# ELSE
# ============================================

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)


# ============================================
# FINALLY
# ============================================

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")


# ============================================
# RAISING AN EXCEPTION
# ============================================

age = 15

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

except ValueError as error:
    print(error)


# ============================================
# PRACTICAL EXAMPLE
# ============================================

def calculate_average(total, count):
    try:
        return total / count

    except ZeroDivisionError:
        return "Cannot calculate average because count is zero."


print(calculate_average(500, 10))
print(calculate_average(500, 0))


# ============================================
# PRACTICE
# ============================================

# 1. Handle invalid integer input.
# 2. Handle division by zero.
# 3. Create a function that safely converts
#    user input into a number.
# 4. Create a program that handles invalid
#    list indexes.
# 5. Use try, except, else, and finally.
