import math
def calculator():
    while True:
        user_input = input("Enter a type of maths (math, log, cos, sin, tan) or type exit to exit: ")
        if user_input == 'exit':
            break
        if user_input == 'pi':
            print(math.pi)
        if user_input == 'math':
            math_question = input("Enter a math question (2+1, 10/2, 3-2, 3*5):")
            try:
                result = eval(math_question)
                print(result)
            except:
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
                print("Invalid input, please try again.")
calculator()