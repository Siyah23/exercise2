num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("enter an operation(+, -, *, /): ")
if operation == "+":
  result = num1 + num2
elif operation =="-":
  result = num1 - num2
elif operation =="*":
  result = num1 * num2
elif operation =="/":
  if num2 != 0:
    result = num1 / num2
  else:
    result = "error: cannot divide by zero."
else:
  result = "invalid operation."
print("result", result)