n = int(input())

if (0 <= n <= 10000):
    if n >= 3000:
        print("book")
    elif 1000 <= n < 3000:
        print("mask")
    else:
        print("no")