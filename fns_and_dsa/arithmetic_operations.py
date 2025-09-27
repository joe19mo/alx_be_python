

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation.

    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide' (case-insensitive)

    Returns:
        float or str: The numeric result of the operation, or a string error message
                      for division-by-zero or unsupported operations.
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"
