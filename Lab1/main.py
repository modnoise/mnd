# Variant: 306 (min(Y-Yэт)²)
import timeit
from random import randint

start = timeit.default_timer()

a0, a1, a2, a3 = 3, 1, 13, 4
X1, X2, X3 = [], [], []
Xn1, Xn2, Xn3 = [], [], []

print("a0={0} \na1={1} \na2={2} \na3={3}\n".format(a0, a1, a2, a3))

# ------------------------------------Формування масивів----------------------------------------------------------------
for i in range(8):
    X1.append(randint(0, 20))
    X2.append(randint(0, 20))
    X3.append(randint(0, 20))

print(f"X1: {X1}")
print(f"X2: {X2}")
print(f"X3: {X3}" + '\n')

# ------------------------------------Обчислення Yi, X0, dx, Xn---------------------------------------------------------
Y = [a0 + a1 * X1[i] + a2 * X2[i] + a3 * X3[i] for i in range(8)]

X01 = (max(X1) + min(X1)) / 2
X02 = (max(X2) + min(X2)) / 2
X03 = (max(X3) + min(X3)) / 2
print("x01={0} \nx02={1} \nx03={2} \n".format(X01, X02, X03))

dX1 = X01 - min(X1)
dX2 = X02 - min(X2)
dX3 = X03 - min(X3)
print("dx01={0} \ndx02={1} \ndx03={2} \n".format(dX1, dX2, dX3))

for i in range(8):
    Xn1.append(round(((X1[i] - X01) / dX1), 3))
    Xn2.append(round(((X2[i] - X02) / dX2), 3))
    Xn3.append(round(((X3[i] - X03) / dX3), 3))

print("Xn1: " + str(Xn1))
print("Xn2: " + str(Xn2))
print("Xn3: " + str(Xn3) + '\n')
# ------------------------Обчислення Y еталонне та значення функції згідно варіанту-------------------------------------
Yet = a0 + a1 * X01 + a2 * X02 + a3 * X03
f = [(Y[i] - Yet) ** 2 for i in range(8)]
res = min(f)

stop = timeit.default_timer()
time = (stop - start)
print("Yэт: " + str(Yet))
print("(Y-Yэт)²: " + str(f))
print("min(Y-Yэт)²: " + str(res))
print(f"Час роботи програми = {round(time, 10)} sec")
