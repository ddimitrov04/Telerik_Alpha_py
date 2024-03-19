def triangle(n):
    if n == 0:
        return 0
    else:

        return n+triangle(n-1)

n = int(input())
print(triangle(n))