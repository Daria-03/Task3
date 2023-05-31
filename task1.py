N = abs(int(input('Введи количество элементов: ')))
A_entered = input("Введи через пробел элементы: ").split()
A_num = list(map(int, A_entered))
count = 0
X = int(input('Введи число, которое необходимо найти в списке: '))
for i in range(N):
  if A_num[i] == X:
   count += 1
print(f'Число {X} встречается в списке {count} раз') 