from random import randint
from numpy.linalg import det
from functools import reduce


def naturalize(matrix_of_plan, min_max_arr):
    result = []
    for i in matrix_of_plan:
        result.append(min_max_arr[1]) if i == 1 else result.append(min_max_arr[0])
    return result


M = 4
x1 = [10, 40]
x2 = [15, 50]
x3 = [10, 30]
print(f'x1_min = {x1[0]}, x1_max = {x1[1]}')
print(f'x2_min = {x2[0]}, x2_max = {x2[1]}')
print(f'x3_min = {x3[0]}, x3_max = {x3[1]}')

# ------------------------------------Матриця планування експерименту з +1,-1-------------------------------------------
x0_p1 = [1, 1, 1, 1]
x1_p1 = [-1, -1, 1, 1]
x2_p1 = [-1, 1, -1, 1]
x3_p1 = [-1 * (x1_p1[i] * x2_p1[i]) for i in range(len(x1_p1))]
print('x0:', x0_p1)
print('x1:', x1_p1)
print('x2:', x2_p1)
print('x3:', x3_p1)

# -------------------------------Матриця планування з натуралізованими значеннями факторів------------------------------
x1_p2 = naturalize(x1_p1, x1)
x2_p2 = naturalize(x2_p1, x2)
x3_p2 = naturalize(x3_p1, x3)
print('\nx1:', x1_p2)
print('x2:', x2_p2)
print('x3:', x3_p2)

xAverage_max = (max(x1_p2) + max(x2_p2) + max(x3_p2)) / 3
xAverage_min = (min(x1_p2) + min(x2_p2) + min(x3_p2)) / 3
print(f'\nx_avg_max = {xAverage_max}')
print(f'x_avg_min = {xAverage_min}')

# -------------------------------------------------Діапазон y-----------------------------------------------------------
y_Max = int(200 + xAverage_max)
y_Min = int(200 + xAverage_min)
print(f'\ny_max = {y_Max}')
print(f'y_min = {y_Min}')

y1 = [randint(y_Min, y_Max) for _ in range(4)]
y2 = [randint(y_Min, y_Max) for _ in range(4)]
y3 = [randint(y_Min, y_Max) for _ in range(4)]
print('y1:', y1)
print('y2:', y2)
print('y3:', y3)

y_avg_arr = [(y1[i] + y2[i] + y3[i]) / 3 for i in range(4)]
print('y average:', y_avg_arr)

# ------------------------------------------Математичне очікування------------------------------------------------------
mx1 = reduce(lambda a, b: a + b, x1_p2) / 4
mx2 = reduce(lambda a, b: a + b, x2_p2) / 4
mx3 = reduce(lambda a, b: a + b, x3_p2) / 4
my = reduce(lambda a, b: a + b, y_avg_arr) / 4
print(f'\nmx1 = {mx1}')
print(f'mx2 = {mx2}')
print(f'mx3 = {mx3}')
print(f'my = {my}')

a1 = sum([x1_p2[i] * y_avg_arr[i] for i in range(4)]) / 4
a2 = sum([x2_p2[i] * y_avg_arr[i] for i in range(4)]) / 4
a3 = sum([x3_p2[i] * y_avg_arr[i] for i in range(4)]) / 4
print(f'\na1 = {a1}')
print(f'a2 = {a2}')
print(f'a3 = {a3}')

a11 = sum([i * i for i in x1_p2]) / 4
a22 = sum([i * i for i in x2_p2]) / 4
a33 = sum([i * i for i in x3_p2]) / 4
print(f'\na11 = {a11}')
print(f'a22 = {a22}')
print(f'a33 = {a33}')

a12 = sum([x1_p2[i] * x2_p2[i] for i in range(4)]) / 4
a13 = sum([x1_p2[i] * x3_p2[i] for i in range(4)]) / 4
a23 = sum([x2_p2[i] * x3_p2[i] for i in range(4)]) / 4
a21 = a12
a31 = a13
a32 = a23
print(f'\na12 = {a12}')
print(f'a13 = {a13}')
print(f'a23 = {a23}')
print(f'a21 = {a21}')
print(f'a31 = {a31}')
print(f'a32 = {a32}')

b0 = det([[my, mx1, mx2, mx3],
          [a1, a11, a12, a13],
          [a2, a21, a22, a23],
          [a3, a31, a32, a33]]) / det([[1, mx1, mx2, mx3],
                                       [mx1, a11, a12, a13],
                                       [mx2, a21, a22, a23],
                                       [mx3, a31, a32, a33]])
b1 = det([[1, my, mx2, mx3],
          [mx1, a1, a12, a13],
          [mx2, a2, a22, a23],
          [mx3, a3, a32, a33]]) / det([[1, mx1, mx2, mx3],
                                       [mx1, a11, a12, a13],
                                       [mx2, a21, a22, a23],
                                       [mx3, a31, a32, a33]])
b2 = det([[1, mx1, my, mx3],
          [mx1, a11, a1, a13],
          [mx2, a21, a2, a23],
          [mx3, a31, a3, a33]]) / det([[1, mx1, mx2, mx3],
                                       [mx1, a11, a12, a13],
                                       [mx2, a21, a22, a23],
                                       [mx3, a31, a32, a33]])
b3 = det([[1, mx1, mx2, my],
          [mx1, a11, a12, a1],
          [mx2, a21, a22, a2],
          [mx3, a31, a32, a3]]) / det([[1, mx1, mx2, mx3],
                                       [mx1, a11, a12, a13],
                                       [mx2, a21, a22, a23],
                                       [mx3, a31, a32, a33]])

print(f'y = {b0} + {b1}*x1 + {b2}*x2 + {b3}*x3')

for i in range(4):
    y = b0 + b1 * x1_p2[i] + b2 * x2_p2[i] + b3 * x3_p2[i]
    print('y =', y)

# ------------------------------------Перевірка однорідності дисперсії за критерієм Кохрена-----------------------------
dispersion = [((y1[i] - y_avg_arr[i]) ** 2 + (y2[i] - y_avg_arr[i]) ** 2 + (y3[i] - y_avg_arr[i]) ** 2) / 3 for i in
              range(4)]
print('dispersion:', dispersion)

gp = max(dispersion) / sum(dispersion)
print('Gp =', gp)

# --------------------------------Рівень значимості q = 0.05; f1 = m - 1 = 2; f2 = N = 4--------------------------------
#  Gт = 0.7679
if gp < 0.7679:
    print('Дисперсія однорідна')
    # ------------------------Оцінка значимості коефіцієнтів регресії згідно критерію Стьюдента-------------------------
    s2b = sum(dispersion) / 4
    s2bs_avg = s2b / 4 * M
    sb = s2bs_avg ** (1 / 2)

    beta0 = sum([y_avg_arr[i] * x0_p1[i] for i in range(4)]) / 4
    beta1 = sum([y_avg_arr[i] * x1_p1[i] for i in range(4)]) / 4
    beta2 = sum([y_avg_arr[i] * x2_p1[i] for i in range(4)]) / 4
    beta3 = sum([y_avg_arr[i] * x3_p1[i] for i in range(4)]) / 4

    beta_arr = [beta0, beta1, beta2, beta3]
    print('beta:', beta_arr)
    t_arr = [abs(beta_arr[i]) / sb for i in range(4)]
    print('tetta:', t_arr)

    # --------------------------------------f3 = f1*f2------------------------------------------------------------------
    indexes = []
    for i, v in enumerate(t_arr):
        if t_arr[i] > 2.306:
            indexes.append(i)
        else:
            print(f'Коефіцієнт b{i} = {v} приймаємо не значним')

    b_list = [b0, b1, b2, b3]
    print(f'y = b{indexes[0]}')

    b_res = [b_list[indexes[0]] for _ in range(4)]
    for i in b_res:
        print(f'y = {i}')

    # ------------------------------------------Критерій Фішера---------------------------------------------------------
    # ------------------------------------кількість значимих коефіцієнтів-----------------------------------------------
    d = 1
    s2_ad = M * sum([(y_avg_arr[i] - b_res[i]) ** 2 for i in range(4)]) / 4 - d
    fp = s2_ad / s2b
    print(f'Fp = {fp}')

    # Fт = 4.5
    if fp > 4.5:
        print('Рівняння регресії неадекватно оригіналу при рівні значимості 0.05')
    else:
        print('Рівняння регресії адекватно оригіналу при рівні значимості 0.05')    
else:
    print('Дисперсія неоднорідна')


