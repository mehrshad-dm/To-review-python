user_number = int(input("Enter a number:"))
i = 0
while i < user_number:
    i +=1
    if i % 3 == 0 and i % 5 == 0:
        print("HipHop")
        continue
    elif i % 3 == 0:
        print("Hip")
        continue
    elif i % 5 == 0:
        print("Hop")
        continue
    else:
        print(i)
print("End game!")