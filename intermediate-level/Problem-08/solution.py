# Command-line Calculator

def calculator():
    command = input("Enter command (e.g., add 5 7): ").split()
    operation, num1, num2 = command[0], int(command[1]), int(command[2])
    
    if operation == "add":
        print(f"Result: {num1 + num2}")
    elif operation == "subtract":
        print(f"Result: {num1 - num2}")
    elif operation == "multiply":
        print(f"Result: {num1 * num2}")
    elif operation == "divide":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid command")

if __name__ == "__main__":
    calculator()