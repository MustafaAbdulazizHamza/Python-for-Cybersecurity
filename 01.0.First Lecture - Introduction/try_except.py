try:
    n = input("Enter an integer: ")
    n = int(n)
    print(n*n)
except Exception as e:
    print(e)