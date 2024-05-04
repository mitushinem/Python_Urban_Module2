from random import randint

num1 = randint(3, 20)
print(f'Первое число: {num1}')

result = []
for i in range(1, num1):
    for j in range(1, 20):
        if j == num1:
            continue
        elif num1 % (i + j) == 0 and (j, i) not in result and i != j:
            result.append((i, j))

print('Пароль: ', end='')
for i in result:
    for j in i:
        print(j, end='')
