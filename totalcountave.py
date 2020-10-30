#Set counter
total = 0
counter = 0

#take user input until user enters "done"
while True:
    user_input = input("Enter a number:")
    try:
        if user_input == "done":
            break
        total = total + int(user_input)
        counter = counter + 1
    except:
        print("Invalid input")

#Print the total of the users input, count of how many inputs the user entered, and the average value of all user inputs
print(total, counter, (total/counter))
