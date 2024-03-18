import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# FOR RUNNING MAIN IN THIS FILE
# def bezier_points_with_dnc_n(point, iteration):
#     iteration_points = []

#     def recursive(points, current_iteration):
#         if current_iteration < iteration:
#             new_points = [points]
#             for _ in range(len(points) - 1):
#                 new_mid = [find_mid_point(points[i], points[i + 1])
#                            for i in range(len(points) - 1)]
#                 new_points.append(new_mid)
#                 points = new_mid

#             left = [p[0] for p in new_points]  # Left side
#             right = [p[-1] for p in reversed(new_points)]  # Right side

#             recursive(left, current_iteration + 1)
#             iteration_points.append(new_points[-1][0])
#             recursive(right, current_iteration + 1)

#     recursive(point, 0)
#     return iteration_points

def find_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


def bezier_points_with_dnc_n(point, iteration):
    iteration_points = []

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
            iteration_points.append([new_points[-1]])  # Modified line
            recursive(right, current_iteration + 1)

    recursive(point, 0)
    return iteration_points


if __name__ == "__main__":
    control_points = [(0, 0), (0, 5), (5, 5), (5, 0)]
    iteration = 2

    fig, ax = plt.subplots()
    ax.plot(*zip(*control_points), 'ro--', label='Control Points')

    bezier_lines = []
    for i in range(iteration + 1):
        bezier_points = bezier_points_with_dnc_n(control_points, i)
        bezier_points = [control_points[0]] + \
            bezier_points + [control_points[-1]]
        line, = ax.plot(*zip(*bezier_points), 'b-',
                        label='Bezier Curve' if i == iteration else None)
        bezier_lines.append(line)

    def update(frame):
        for i, line in enumerate(bezier_lines):
            if i == frame:
                line.set_visible(True)
            else:
                line.set_visible(False)
        return bezier_lines

    ani = FuncAnimation(fig, update, frames=range(
        iteration + 1), interval=500, blit=True)

    ax.legend()
    plt.title('Bézier Curve using Divide and Conquer (n points)')
    plt.show()
