a, b, c = map(int, input().split())

if all(1 < x < 100 for x in (a,b,c)):
    avg = int((a+b+c)/3)
    print(a+b+c)
    print(avg)
    print(a+b+c-avg)