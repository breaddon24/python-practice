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


nums = [3, 7, 2]
total = 12

for num in nums:
    total = total - num
print(total)

number = 15
if number % 2 == 0 or number % 3 == 0:
    print("Divisible by 2 or 3")
else:
    print("Not divisible by 2 or 3")

lowest = 4
i = 16

while i > lowest:
    print(i, end=' ')
    i = i // 2

print(i, end=' ')