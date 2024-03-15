import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fungsi faktorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Fungsi kombinasi
def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# Fungsi bruteforce untuk n titik kontrol
def bezier_curve_with_bruteforce(points, num_points):
    n = len(points) - 1
    t = np.linspace(0, 1, num_points)
    bezier_point = np.zeros((num_points, 2))
    # Memakai rumus polinomial bernstein
    for i in range(n + 1):
        coef = combination(n, i)
        for j in range(num_points):
            formula = coef * (t[j] ** i) * ((1 - t[j]) ** (n - i))
            bezier_point[j] += np.array(points[i]) * formula
    return bezier_point

num_iterations = int(input("Masukkan jumlah iterasi: "))
num_points = 2 ** num_iterations + 1

control_points = [(0, 0), (1, 1), (2, 1), (3, 0)]
bezier_points = bezier_curve_with_bruteforce(control_points, num_points)
print(bezier_points)