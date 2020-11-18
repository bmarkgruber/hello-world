# Collatz sequence
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (3 * number) + 1

while True:
    try:
        user_input = input('Enter any positive integer\n')
        intuser_input = int(user_input)
        if intuser_input < 0:
            print('Please enter a positive integer')
            continue
        while True:
            if collatz(intuser_input) > 1:
                intuser_input = collatz(intuser_input)
                print(intuser_input)
            else:
                print('1')
                break
        break
    except ValueError:
        print('Please Enter valid input\n')
        continue