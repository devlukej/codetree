n = int(input())

if (0 <= n <= 100):
    if n >= 80:
        print("pass")
    else:
        print(f"{80-n} more score")