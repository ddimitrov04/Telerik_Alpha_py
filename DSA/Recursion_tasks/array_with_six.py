def value_by_ten(arr, count):
    if count >= len(arr) - 1:
        return "false"
    elif arr[count]*10 == arr[count+1]:
        return "true"
    else:
        return value_by_ten(arr, count+1)


arr = list(map(int, input().split(",")))
count = int(input())
print(value_by_ten(arr, count))
