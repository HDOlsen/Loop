def prime():
    a = int(input("Please enter an integer."))
    for i in range (2, a):
        if a%i == 0:
            print (f"{a} is not prime.")
            break
        else:
            print (f"{a} is prime.")
            break
prime()
