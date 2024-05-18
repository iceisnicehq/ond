
def calculate_expression(expression):
    """Takes a string as input, evaluates it as a Python expression, and prints the result."""
    try:
        result = eval(expression)
        print(f"The result is {result}")
    except Exception as e:
        print(f"Error: {e}")

print("Type 'no' to quit")
result = "yes"
while result!="no":
    result = input("Equation (or not): ")
    calculate_expression(result)
