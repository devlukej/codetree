a = float(input())
b = float(input())
c = float(input())

if all(0 < x < 1000 for x in (a,b,c)):
    print(f'{a:.3f}')
    print(f'{b:.3f}')
    print(f'{c:.3f}')