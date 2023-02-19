import math
def calculator():
    while True:
        # Get the user's input
        user_input = input("Enter a mathematical expression (e.g. 2 + 3) or type exit to exit: ")
        
        # Exit the calculator if the user types 'exit'
        # Say value of pi if the user types pi
        if user_input == 'exit':
            break
        if user_input == 'pi':
            print(math.pi)

        # Use try-except block to handle errors
        try:
            # Evaluate the expression and print the result
            result = eval(user_input)
            print(result)
        except:
            # Print an error message if the input is invalid
            print("Invalid input, please try again.")    
calculator()
