# Calculator
from art import logo
# Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  if n2 > n1 :
    return n2 - n1
  elif n1 > n2 :
    return n1 - n2
  else:
    return 0

# Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply, 
  "/": divide
}
# function = operations["*"]
# function(2,3)

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  should_continue = True
  
  while should_continue:
    operation_chice = input("Pic an operation: ")
    num2 = float(input("What's the next number?: "))
    function = operations[operation_chice]
    result = function(num1, num2)
    
    print(f"{num1} {operation_chice} {num2} = {result}" )

    run = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation, or type 'exit' to exit from calculating: ")
    if run == "y":
      num1 = result
    elif run == "n":
      should_continue = False
      calculator()
    else:
      should_continue = False
    
calculator()
