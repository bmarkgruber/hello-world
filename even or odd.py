#get inputs from user
num = int(input('Pick a number: '))
check = int(input('Is number divisible by '))

#check if even or odd
if num % 2 == 0:
    print(num, 'is a even!')
else:
    print(num, 'is odd!')

#check if num is a multiple of check
mult_of_check = num % check
if mult_of_check == 0:
    print('Number is a multiple of ' + str(check))
else:
    print('Number is not a multiple of ' + str(check))
