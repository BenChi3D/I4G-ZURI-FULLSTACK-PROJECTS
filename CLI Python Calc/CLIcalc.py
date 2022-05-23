def calculator():
    operation = input('''
    Please enter the mathematical operation you will like to use to continue 
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    # numbers to be worked with by the user
    num1 = int(input('Enter your first number:\n'))
    num2 = int(input('Enter your second number:\n'))
    
    if operation == '+' :
        # Addition
        print('{} + {} = '.format(num1 , num2))
        print(num1 + num2)
    elif operation == '-' :
        # Subtraction
        print('{} - {} = '.format(num1 , num2))
        print(num1 - num2)
    elif operation == '*':
        # Multiplication
        print('{} * {} = '.format(num1 , num2))
        print(num1 * num2)
    elif operation == '/':
        # division
        print('{} / {} = '.format(num1 , num2))
        print(num1 / num2)
    else:
        print('What you entered is not a valid operator')

calculator()