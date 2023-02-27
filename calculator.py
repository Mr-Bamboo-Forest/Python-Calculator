import math
def calculator():
    while True:
        # Get the user's input
        user_input = input("Enter a type of maths (math, log, cos, sin, tan) or type exit to exit: ")
        
        # Exit the calculator if the user types 'exit'
        # Say value of pi if the user types pi
        if user_input == 'exit':
            break
        if user_input == 'pi':
            print(math.pi)
        if user_input == 'math':
            # Use try-except block to handle errors
            try:
                # Evaluate the expression and print the result
                result = eval(user_input)
                print(result)
            except:
                # Print an error message if the input is invalid
                print("Invalid input, please try again.")
        if user_input == 'log':
            user_input_log = input("Enter x of log: ")
            user_input_base = input("Enter base of log: ")
            try:
                log_int = int(user_input_log)
                log_int_2 = int(user_input_base)
                log_answer = math.log(log_int, log_int_2)
                print(log_answer)
            except:
                print("Not a Number")
calculator()
