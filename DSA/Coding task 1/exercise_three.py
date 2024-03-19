def shuffle_numbers(n, k, numbers_to_shuffle):
    init_list = list(range(1, n+1))

    index_map = {number: index for index, number in enumerate(init_list)}

    for num in numbers_to_shuffle:
        if num % 2 == 0:
            target_num = num//2
        else:
            if (num*2) <= n:
                target_num = num *2
            else:
                target_num = n

        if num == target_num:
            continue

        current_index, target_index = index_map[num], index_map[target_num]

        if current_index == target_index + 1:
            continue

        init_list.pop(current_index)
        if target_index < current_index:
            new_index = target_index + 1
        else:
            new_index = target_index
        init_list.insert(new_index, num)

        min_index, max_index = sorted([current_index, new_index])
        for i in range(min_index, max_index+2):
            if i < len(init_list):
                index_map[init_list[i]] = i

    return init_list

n, k = map(int, input().split())
numbers_to_shuffle = list(map(int, input().split()))

new_nums = shuffle_numbers(n, k, numbers_to_shuffle)
print(*new_nums)