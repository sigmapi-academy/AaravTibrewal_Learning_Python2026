num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter operator (+,-,*,/): ')

match op:
    case '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    
    case '-':
        print(f'Difference = {num1 - num2}')
    
    case '*':
        print(f'Product = {num1 * num2}')
    
    case '/':
        if num2 == 0:
            print('Division by 0 is not allowed')
        else:
            print(f'Quotient = {num1 / num2}')
    case _:
        print('Wrong operator selected')
    