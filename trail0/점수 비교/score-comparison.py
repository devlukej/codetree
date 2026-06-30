a_m, a_e = map(int, input().split())
b_m, b_e = map(int, input().split())

if all(1 <= x <= 100 for x in (a_m, a_e, b_m, b_e)):
    print(int(a_m > b_m and a_e > b_e))
