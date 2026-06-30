a, b = map(int, input().split())
temp = 0
if all(1 < x < 100 for x in (a,b)):
    temp = a
    a = b
    b = temp
    print(a, b, sep=" ")