def get_value(values: list, number: int):
    output = []

    for value in values:
        for digit in value:
            if digit == str(number):
                output.append(value)
                break
    return output

print(get_value(values=['123', '8273', '1818', '1725', '333'], number=3))

 
def reversal(num):
    return int(str(num)[::-1])
print(reversal(123456))


def sum_until(n):
    output = 0
    for i in range(1, n + 1):
        output += i
    return output

print(sum_until(10))
