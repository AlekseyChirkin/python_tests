while True:
    try:
        x = input('Enter number to be squared:\n')
        if x.lower() == 'exit':
            break
        y = int(x) ** 2
        print(f'Result is {y}')
    except:
        print('Enter correct number, please!')
        print('For exit type "exit"...\n')
print('Program finished correct')
