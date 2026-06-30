a, b = map(int, input().split())

if all(1 < x < 100 for x in (a,b)):
    print(int(a>=b))
    print(int(a>b))
    print(int(b>=a))
    print(int(b>a))
    print(int(a==b))
    print(int(a!=b))