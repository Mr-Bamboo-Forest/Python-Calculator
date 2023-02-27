import math
def calculator():
    while True:
        user_input = input("Enter a type of maths (math, log, cos, sin, tan) or type exit to exit: ")
        #exit
        if user_input == 'exit':
            break
        #pi
        if user_input == 'pi':
            print(math.pi)
        #math
        if user_input == 'math':
            math_question = input("Enter a math question (2+1, 10/2, 3-2, 3*5):")
            try:
                result = eval(math_question)
                print(result)
            except:
                print("Invalid input, please try again.")
        #logarithms
        if user_input == 'log':
            user_input_log = input("Enter x of log: ")
            user_input_base = input("Enter base of log: ")
            try:
                log_int = int(user_input_log)
                log_int_2 = int(user_input_base)
                log_answer = math.log(log_int, log_int_2)
                print(log_answer)
            except:
                print("Invalid input, please try again.")
        #cosine
        if user_input == 'cos':
            user_cosine_input1 = input('Enter cosine: ')
            try:
                user_cosine_input = int(user_cosine_input1)
                user_cosine_solve = math.cos(user_cosine_input)
                print(user_cosine_solve)
            except: 
                print('Invalid input, please try again.')
        #sine
        if user_input == 'sin':
            user_sine_input1 = input('Enter sine: ')
            try:
                user_sine_input = int(user_sine_input1)
                user_sine_solve = math.sin(user_sine_input)
                print(user_sine_solve)
            except: 
                print('Invalid input, please try again.')
calculator()