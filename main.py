# Импортирование необходимых модулей
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

# Загрузка библиотеки
lib = ctypes.CDLL("./libtestpp.so")  # Путь к вашей библиотеке .so

# Определение функций real
spherical_harmonic_imag = lib.spherical_harmonic_real
spherical_harmonic_imag.restype = ctypes.c_double
spherical_harmonic_imag.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]


# Определение функций real
spherical_harmonic_real = lib.spherical_harmonic_real
spherical_harmonic_real.restype = ctypes.c_double
spherical_harmonic_real.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]

# Создание значений theta и phi
theta_values = np.linspace(0, 2 * np.pi, 100)
phi_values = np.linspace(0, np.pi, 100)

# Вычисление значений для функции сферических гармоник
Ylm_values_real = np.zeros((100, 100))
for i, theta in enumerate(theta_values):
    for j, phi in enumerate(phi_values):
        Ylm_values_real[i, j] = sph_harm(theta, phi, 2, 1)

Ylm_values_image = np.zeros((100, 100))
for i, theta in enumerate(theta_values):
    for j, phi in enumerate(phi_values):
        Ylm_values_image[i, j] = spherical_harmonic_imag(theta, phi, 1, 1)

# Построение графика
plt.figure()
plt.contourf(theta_values, phi_values, Ylm_values_image, levels=100, cmap='viridis')
plt.colorbar()
plt.title('Реальная часть сферических гармоник (l=2, m=1)')
plt.xlabel('Theta')
plt.ylabel('Phi')
plt.show()


