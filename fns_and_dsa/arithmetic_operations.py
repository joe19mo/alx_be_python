

def perform_operation(num1: float, num2: float, operation: str):
    """"
    Perform a basic arithmetic operation.

    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float or str: The result of the operation, or an error message for invalid inputs
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        case _:
            return "Error: Unsupported operation"
