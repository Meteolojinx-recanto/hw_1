def divisible_by_2(num):
    return len(num) % 2 == 0

numbers = input('Введите число ').split()
numbers_list = list(map(divisible_by_2, numbers))

print(numbers)
print(numbers_list)