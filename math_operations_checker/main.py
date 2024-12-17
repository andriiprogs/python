# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform mathematical operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Display results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Division: {division}")
