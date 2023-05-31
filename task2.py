N = abs(int(input('Введи количество элементов: ')))
A_entered = input("Введи через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
X = int(input('Введи число, с которым необходимо сравнивать элементы списка: '))
min = abs(X - A_num[0])
index = 0
for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
print(f'Число {A_num[index]} в списке близко по величине к числу {X}')