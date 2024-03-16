import numpy as np
import matplotlib.pyplot as plt


def bezier_points_with_bruteforce(points, iteration):
    points = np.array(points)
    total = 2 ** iteration + 1
    t = np.linspace(0, 1, total)
    bezier_points = np.zeros((total, 2))

    for i in range(total):
        bezier_points[i] = (1 - t[i])**2 * points[0] + 2 * \
            (1 - t[i]) * t[i] * points[1] + t[i]**2 * points[2]
    return bezier_points


if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 0)]
    iteration = 3
    bezier_points = bezier_points_with_bruteforce(points, iteration)
    print(bezier_points)

    plt.plot(*zip(*points), 'ro--', label='Control Points')
    plt.plot(*zip(*bezier_points), 'b-', label='Bezier Curve')
    plt.title('Bézier Curve using Brute Force (3 points)')
    plt.legend()
    plt.show()
