import numpy as np
import matplotlib.pyplot as plt
# Fungsi untuk menghitung faktorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Fungsi untuk menghitung kombinasi


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# Fungsi untk mencari titik pada kurva bezier dengan bruteforce untuk n titik


def bezier_points_with_bruteforce_n(points, iteration):
    total = 2 ** iteration + 1
    n = len(points) - 1
    t = np.linspace(0, 1, total)
    bezier_points = np.zeros((total, 2))
    # Memakai rumus polinomial bernstein
    for i in range(n + 1):
        coef = combination(n, i)
        for j in range(total):
            formula = coef * (t[j] ** i) * ((1 - t[j]) ** (n - i))
            bezier_points[j] += np.array(points[i]) * formula
    return bezier_points


if __name__ == "__main__":
    control_points = [(0, 0), (1, 1), (2, 1), (3, 0)]
    iteration = 2
    bezier_points = bezier_points_with_bruteforce_n(control_points, iteration)
    print(bezier_points)

    plt.plot(*zip(*control_points), 'ro--', label='Control Points')
    plt.plot(*zip(*bezier_points), 'b-', label='Bezier Curve')
    plt.title('Bézier Curve using Brute Force (n points)')
    plt.legend()
    plt.show()
