year = int(input())

if 1 <= year <= 2222:
    if (year % 4 == 0):
        if (year % 100 == 0 and year % 400 != 0):
            print("false")
        else:
            print("true")
    else:
        print("false")