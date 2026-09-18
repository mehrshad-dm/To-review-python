def print_name(name , n=1):
    '''
    this function is for print name,
    n times, and use defult for n, if i don't pass n, n=1 and
    else n = my input for pass function
    '''

    for i in range(n):
        print(i, name)

print_name("Mehrshad", 10)