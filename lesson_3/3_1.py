# Вычислить модуль числа без использования библиотечных функций.
a = int(input('Число:'))
if a > 0:
    print('Модуль равен',a)
elif a < 0:
    print('Модуль равен',-a)
else:
    print('Введен ноль')
