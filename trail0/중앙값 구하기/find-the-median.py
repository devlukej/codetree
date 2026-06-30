a, b, c = map(int, input().split())


if all(-100 <= x <= 100 for x in (a, b, c)):
    if a > b:
        if b > c:
            print(b)
        else:
            if c > a:
                print(a)
            else:
                print(c)
    else:
        if a > c:
            print(a)
        else:
            if c > b:
                print(b)
            else:
                print(c)