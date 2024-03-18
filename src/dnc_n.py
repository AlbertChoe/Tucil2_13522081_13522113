import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def find_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Ini untuk menyimpan semua titik yang dihasilkan


def bezier_points_with_dnc_n(point, iteration):
    iteration_points = []
    save_point = []

    def recursive(points, current_iteration):
        if current_iteration < iteration:
            new_points = [points]
            for _ in range(len(points) - 1):
                new_mid = [find_mid_point(points[i], points[i + 1])
                           for i in range(len(points) - 1)]
                new_points.append(new_mid)
                points = new_mid

            left = [p[0] for p in new_points]  # Left side
            right = [p[-1] for p in reversed(new_points)]  # Right side

            recursive(left, current_iteration + 1)
            iteration_points.append(new_points[-1][0])
            save_point.append([new_points[-1]])
            recursive(right, current_iteration + 1)

    recursive(point, 0)
    return save_point


# Ini menampilkan titik awal dan akhir  bezier
# def bezier_points_with_dnc_n(point, iteration):
#     bezier_points = [point[0]]

#     def recursive(points, current_iteration):
#         if current_iteration < iteration:
#             new_points = [points]
#             for _ in range(len(points) - 1):
#                 new_mid = [find_mid_point(points[i], points[i+1])
#                            for i in range(len(points)-1)]
#                 new_points.append(new_mid)
#                 points = new_mid

#             left = [p[0] for p in new_points]  # Left side
#             right = [p[-1] for p in reversed(new_points)]  # Right side

#             recursive(left, current_iteration + 1)
#             bezier_points.append(new_points[-1][0])
#             recursive(right, current_iteration + 1)

#     recursive(point, 0)
#     bezier_points.append(point[-1])
#     return bezier_points


if __name__ == "__main__":
    control_points = [(0, 0), (0, 5), (5, 5), (5, 0)]
    iteration = 2

    fig, ax = plt.subplots()
    ax.plot(*zip(*control_points), 'ro--', label='Control Points')
    bezier_lines_dnc = []
    for i in range(iteration + 1):
        bezier_points_dnc = bezier_points_with_dnc_n(control_points, i)
        bezier_points_flat = [
            item for sublist in bezier_points_dnc for subsublist in sublist for item in subsublist]
        bezier_points_flat = [control_points[0]] + \
            bezier_points_flat + [control_points[-1]]
        line, = ax.plot(*zip(*bezier_points_flat), 'b-',
                        label='Bezier Curve' if i == iteration else None)
        bezier_lines_dnc.append(line)

    def update_dnc(frame):
        if frame == iteration:
            for line in bezier_lines_dnc:
                line.set_visible(False)
            bezier_lines_dnc[-1].set_visible(True)
        else:
            for i, line in enumerate(bezier_lines_dnc):
                line.set_visible(i == frame)
        return bezier_lines_dnc

    ani_dnc = FuncAnimation(fig, update_dnc, frames=range(
        iteration + 1), interval=500, blit=True)
    ax.set_title(f'Divide and Conquer Method')
    ax.legend()
    plt.show()
