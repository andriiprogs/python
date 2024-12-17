# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic and advanced mathematical operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    division = num1 / num2
    modulo = num1 % num2
    floor_division = num1 // num2
else:
    division = "undefined (cannot divide by zero)"
    modulo = "undefined (cannot divide by zero)"
    floor_division = "undefined (cannot divide by zero)"

power = num1 ** num2  # num1 raised to the power of num2

# Display results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Division: {division}")
print(f"Modulo: {modulo}")
print(f"Floor Division: {floor_division}")
print(f"Power: {power}")
