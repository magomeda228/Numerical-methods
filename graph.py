import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import matplotlib.patches as mpatches

# Определяем кусочно заданную функцию
def piecewise_function(x):
    if (x < r1 and x >= r0) or (x > -r1 and x <= -r0):
        return -q * x**2 /(4*l) - C5 * np.log(np.abs(x)) + C6
    elif (x >= r1 and x < r2) or (x <= -r1 and x > -r2):
        return C3 * np.log(np.abs(x)) + C4
    elif (x <= r3 and x >=r2) or (x >= -r3 and x <= -r2):
        return C1 * np.log(np.abs(x)) + C2
    else:
        return -q * r0 ** 2 / (4 * l) - C5 * np.log(r0) + C6

# Генерируем данные для графика
Db=9.1e-3
cob=0.8e-3
cg=0.1e-3
a=30e3
lg=0.35
lob=20
l=3
q=8e8
Tg=60+273
r3=Db/2
r2=r3-cob
r1=r2-cg
r0=1.2e-3/2
qe = q * np.pi * (r1**2 - r0**2)

dTob = qe * np.log(r3/r2)/(2 * np.pi * lob)
dTg = qe * np.log(r2/r1)/(2 * np.pi * lg)
Tall = dTob + dTg + qe/(np.pi*a*Db)
Tadd = qe/(np.pi*a*Db)

C1 = -dTob / np.log(r3/r2)
C2 = Tg + Tadd + dTob - C1 * np.log(r2)
C3 = -dTg / np.log(r2/r1)
C4 = Tg + dTob + Tadd  - C3 * np.log(r2)
C5 = +q * r0**2/(2 * l)
C6 = Tall + Tg + q * r1**2/(4 * l) + q * r0**2 *np.log(r1) /( 2 * l)

x = np.linspace(-Db/2, Db/2, 1000) # Диапазон значений x
y = [piecewise_function(val) for val in x]  # Применяем функцию к каждому x

#Построени графика
cs = CubicSpline(x, y, bc_type='natural')
y = cs(x)
plt.figure(figsize=(8, 6))
plt.ylim(0, 1900)
plt.xlim(-Db/2-1e-4,Db/2+1e-4)
#.plot(x, y, 'o', label='Original points')
plt.plot(x, y, label="Кусочно заданная функция", color="blue")

plt.axvline(x=r1, color='r', linestyle='--')
plt.axvline(x=-r1, color='r', linestyle='--', label=f'|r1| = {r1:.4f} м')
plt.axvline(x=r2, color='g', linestyle='--')
plt.axvline(x=-r2, color='g', linestyle='--', label=f'|r2| = {r2:.4f} м')
plt.axvline(x=r3, color='b', linestyle='--')
plt.axvline(x=-r3, color='b', linestyle='--', label=f'|r3| = {r3:.4f} м')
plt.axvline(x=r0, color='r', linestyle='--', label=f'|r0| = {r0:.4f} м')
plt.axvline(x=-r0, color='r', linestyle='--')

plt.fill_between(x, 2000, where=(np.abs(x) >= r0) & (np.abs(x) <= r1), color='red', alpha=0.5)
plt.fill_between(x, 2000, where=(np.abs(x) >= r1) & (np.abs(x) <= r2), color='grey', alpha=0.5)
plt.fill_between(x, 2000, where=(np.abs(x) >= r2) & (np.abs(x) <= r3), color='blue', alpha=0.5)
plt.fill_between(x, 2000, where=((np.abs(x) <= r0) | ((np.abs(x) <= (r3+1e-2)) & (np.abs(x) >= r3))), color='lightblue', alpha=0.5)
# Добавляем оформление
plt.title("Функция температуры в цилиндрическом ТВЭЛ")
plt.xlabel("X, м")
plt.ylabel("T, K")
red_patch = mpatches.Patch(color='red', label='UO2  (r0 to r1)')
grey_patch = mpatches.Patch(color='grey', label='Gas (r1 to r2)')
blue_patch = mpatches.Patch(color='blue', label='Shell (r2 to r3)')

plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.legend(handles=[red_patch, grey_patch,blue_patch ], loc='upper left', bbox_to_anchor=(0.65, 0.25), title="Shaded Areas")

# Показываем график
plt.show()
