n = int(input())

if (-200 <= n <= 200):
    if n < 0:
        print("ice")
    elif n >= 100:
        print("vapor")
    else:
        print("water")