another = True

while another:
    user_value = int(input('Please choose a valid integer > '))
    stop_value = user_value + 1

    print('Number \tSquared Cubed \n===== \t===== \t=====')
    for i in range(1, stop_value, 1):
        squared_i = i ** 2
        cubed_i = i ** 3
        print(f'{i} \t\t {squared_i} \t\t {cubed_i}')
    print()
    print(f'Multiplication table of {user_value}')
    print(end='\t')
    for column in range(1, stop_value, 1):
        print(column, end='\t')
    print('\n', end='\t')
    for column in range(1, stop_value, 1):
        print('=', end='\t')
    print()

    for column in range(1, stop_value, 1):
        print(column, end='|\t')
        for row in range(1, stop_value, 1):
            print(column * row, end='\t')
        print()

    print()

    user_choice = input('Do you want to play again? y or n > ')
    if user_choice == 'n':
        another = False