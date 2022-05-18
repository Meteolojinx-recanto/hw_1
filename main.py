def DivisibleBy2(num):
    if num % 2 == 0:
        return True
    else:
        return False

numbers = int(input('Введите число: '))

print(DivisibleBy2(numbers))

