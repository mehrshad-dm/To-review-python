user_input = int(input("adad mored nazar khod ra vared knid:"))
count = int(input("tedad marahel ra vered knid:"))
for i in range(count):
    if user_input % 2 == 0:
        user_input //= 2
    else:
        user_input = (user_input * 2) - 1
print(user_input)