def increase_nums(numbers: list):
    output = []

    for num in numbers:
        num += 1
        if num == 10:
            num = 0
        output.append(num)
    return output

print(increase_nums(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# --------------------------------------------------------------------------------------------------------

def rotate_left(list, number: int):
    return list[number:] + list[:number]

print(rotate_left([1, 2, 3, 4, 5], 1))

# --------------------------------------------------------------------------------------------------------

def transactions(list):
    expenses = []

    for num in list:
        if num < -100:
            expenses.append(num)
    return expenses

print("--- Bank Log ---")
print(transactions([1200.50, -45.00, -120.00, 350.00, -15.50, -500.00, 20.00]))

# --------------------------------------------------------------------------------------------------------