user_input = int(input("yek adad az 2 ta 1000 vared knid:"))
print(user_input)
while user_input != 1:
    if user_input % 2 == 0:
        user_input //= 2
    else:
        user_input = (user_input * 3) + 1
    print(user_input)