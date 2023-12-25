print("Welcome to Your Simple Calculator!")     # Welcome message

                                                  
num1 =float(input("Enter the first number: "))        # Input from the user
num2 = float(input("Enter the second number: "))      # Input from the user

                                         
print("Choose an operation:")                   # Display operation choices
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

                                                                                   
choice = input("Enter the number corresponding to your choice: ")         # Input operation choice  


if choice in ('1', '2', '3', '4'):         # Perform calculation based on user's choice
    if choice == '1':
        result = num1 + num2
        operation = "addition"
    elif choice == '2':
        result = num1 - num2
        operation = "subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "multiplication"
    elif choice == '4':
            result = num1 / num2
            operation = "division"
        
   
    print(f"The result of {num1} {operation} {num2} is: {result}")     # Display the result

else:
    print("Invalid input. Please enter a valid choice (1, 2, 3, or 4).")
