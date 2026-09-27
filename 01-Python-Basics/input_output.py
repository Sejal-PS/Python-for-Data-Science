# Python Input and Output


# 1. Output using print()


name = "Sejal"
age = 26

print("Name:", name)
print("Age:", age)



# 2. Taking input from user


name = input("Enter your name: ")

print("Hello", name)



# 3. Input is string by default


age = input("Enter your age: ")

print("Age:", age)
print("Data Type:", type(age))



# 4. Converting input to integer


age = int(input("Enter your age: "))

print("Age:", age)
print("Data Type:", type(age))


# 5. Converting input to float

salary = float(input("Enter your salary: "))

print("Salary:", salary)
print("Data Type:", type(salary))



# 6. Data Science Example


customer_name = input("Enter customer name: ")
customer_age = int(input("Enter customer age: "))
purchase_amount = float(input("Enter purchase amount: "))

print("\nCustomer Information")
print("Name:", customer_name)
print("Age:", customer_age)
print("Purchase Amount:", purchase_amount)
