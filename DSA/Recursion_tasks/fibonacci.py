def fibonacci(n, save={}):
    if n in save:
        return save[n]

    if n == 0 or n == 1:
        return n

    save[n]= fibonacci(n-1, save) + fibonacci(n-2, save)
    return save[n]

n = int(input())
print(fibonacci(n))