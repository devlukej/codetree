a, n = map(int, input().split())

if all(1 <= x <= 10 for x in (a,n)):
    for x in range(n):
        a += n
        print(a)