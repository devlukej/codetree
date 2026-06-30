a, b = map(int, input().split())

if all(1 <= x <= 100 for x in (a,b)):
    if a > b:
        print(a*b)
    else:
        print(int(b/a))