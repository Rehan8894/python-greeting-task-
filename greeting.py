# Basic Mathematical Operations Program

# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Error: Cannot divide by zero"

# Display results
print("\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")


#Task 2

def main():
    # Taking user input for first and last name
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    # Validating input
    if not first_name or not last_name:
        print("Error: First name and last name cannot be empty.")
        return

    # Creating full name
    full_name = first_name + " " + last_name

    # Printing personalized greeting
    print(f"Hello, {full_name}! Welcome!")

# Run the main function
if __name__ == "__main__":
    main()