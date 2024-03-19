def occurrence_of_seven(n, check=False):
    if n == 0:
        return 0

    if n % 10 == 8:
        if check == False:
            return 1 + occurrence_of_seven(n // 10, check=True)
        else:
            return 2 + occurrence_of_seven(n // 10, check=True)
    else:
        return 0 + occurrence_of_seven(n // 10, check=False)


n = int(input())
print(occurrence_of_seven(n))