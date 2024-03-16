import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def find_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


def bezier_points_with_dnc_n(point, iteration):
    bezier_points = [point[0]]

    def recursive(points, current_iteration):
        if current_iteration < iteration:
            new_points = [points]
            for _ in range(len(points) - 1):
                new_mid = [find_mid_point(points[i], points[i+1])
                           for i in range(len(points)-1)]
                new_points.append(new_mid)
                points = new_mid

            left = [p[0] for p in new_points]  # Left side
            right = [p[-1] for p in reversed(new_points)]  # Right side

            recursive(left, current_iteration + 1)
            bezier_points.append(new_points[-1][0])
            recursive(right, current_iteration + 1)

    recursive(point, 0)
    bezier_points.append(point[-1])
    return bezier_points


if __name__ == "__main__":
    control_points = [(0, 0), (1, 8), (5, 0), (8, 10), (14, 0),
                      (20, 15), (25, 20), (35, 30), (20, 4), (10, 0)]
    iteration = 11
    bezier_points = bezier_points_with_dnc_n(control_points, iteration)
    print(bezier_points)

    plt.plot(*zip(*control_points), 'ro--', label='Control Points')
    plt.plot(*zip(*bezier_points), 'b-', label='Bezier Curve')
    plt.title('Bézier Curve using Divide and Conquer (n points)')
    plt.legend()
    plt.show()
