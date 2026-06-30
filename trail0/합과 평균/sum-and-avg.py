a, b = map(int, input().split())

if all(1 < x < 100 for x in (a,b)):
    avg = (a+b) / 2
    print(a+b, f"{avg:.1f}", sep=" ")