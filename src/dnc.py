import matplotlib.pyplot as plt


# Fungsi untuk mencari titik tengah
def find_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Fungsi untuk mencari titik pada kurva bezier dengan dnc untuk 3 titik
def bezier_points_with_dnc(point1, point2, point3, current_iteration, iteration, bezier_points):
    if current_iteration < iteration:
        mid_point1 = find_mid_point(point1, point2)
        mid_point2 = find_mid_point(point2, point3)
        mid_point = find_mid_point(mid_point1, mid_point2)
        current_iteration += 1

        # Left side
        bezier_points_with_dnc(point1, mid_point1, mid_point,
                               current_iteration, iteration, bezier_points)
        bezier_points.append(mid_point)

        # Right side
        bezier_points_with_dnc(mid_point, mid_point2, point3,
                               current_iteration, iteration, bezier_points)

# Fungsi untuk menggabungkan titik awal, titik akhir, dan hasil titik dari dnc
def generate_bezier(point1, point2, point3, iterations):
    bezier_points = [point1]
    bezier_points_with_dnc(point1, point2, point3, 0,
                           iterations, bezier_points)
    bezier_points.append(point3)
    return bezier_points


if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 0)]
    iteration = 2
    bezier_points = generate_bezier(*points, iteration)
    print(bezier_points)

    plt.plot(*zip(*points), 'ro--', label='Control Points')
    plt.plot(*zip(*bezier_points), 'b-', label='Bezier Curve')
    plt.title('Bézier Curve using Divide and Conquer')
    plt.legend()
    plt.show()
