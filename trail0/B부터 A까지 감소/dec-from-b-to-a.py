a, b = map(int, input().split())

if all(1 <= x <= 100 for x in (a,b)):
    for i in range(b, a-1, -1):
        print(i, end=" ")