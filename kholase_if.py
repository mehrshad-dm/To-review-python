user_input = int(input("Enter a number:"))
if user_input % 2 == 0:
    res = "Zoj"
else:
    res = "Fard"
print(res)


res2 = "Zoj" if user_input % 2 == 0 else "Fard"
print(res2)