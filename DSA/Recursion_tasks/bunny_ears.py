def bunnies(n, count=0):
    if n == count:
        return 0
    else:
        return 2+ bunnies(n, count+1)


n = int(input())
print(bunnies(n))