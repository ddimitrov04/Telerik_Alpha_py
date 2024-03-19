def bunnies(n, count=0):
    if n == count:
        return 0
    else:
        if count%2== 0:
            return 2 + bunnies(n, count + 1)

        else:
            return 3+ bunnies(n, count+1)


n = int(input())
print(bunnies(n))