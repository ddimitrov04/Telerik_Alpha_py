def power(n, k, count=1):
    if count == k:
        return n
    else:
        return n*power(n,k,count+1)

n = int(input())
k = int(input())
print(power(n, k))