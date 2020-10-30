total = 0
counter = 0

while True:
    user_input = input("Enter a number:")
    try:
        if user_input == "done":
            break
        total = total + int(user_input)
        counter = counter + 1
    except:
        print("Invalid input")

print(total, counter, (total/counter))