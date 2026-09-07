def increase_nums(numbers: list):
    output = []

    for num in numbers:
        num += 1
        if num == 10:
            num = 0
        output.append(num)
    return output

print(increase_nums(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def rotate_left(list, number: int):
    return list[number:] + list[:number]

print(rotate_left([1, 2, 3, 4, 5], 1))
