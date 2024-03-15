# Fungsi untuk mencari titik tengah dari 2 titik
def find_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Fungsi untuk mencari titik pada kurva bezier dengan dnc untuk 3 titik
def bezier_points_with_dnc(point1, point2, point3, current_iteration, iteration, bezier_points):
    if current_iteration < iteration:
        mid_point1 = find_mid_point(point1, point2)
        mid_point2 = find_mid_point(point2, point3)
        mid_point = find_mid_point(mid_point1, mid_point2)
        current_iteration += 1

        # sisi kiri
        bezier_points_with_dnc(point1, mid_point1, mid_point, current_iteration, iteration, bezier_points)
        bezier_points.append(mid_point)

        # sisi kanan
        bezier_points_with_dnc(mid_point, mid_point2, point3, current_iteration, iteration, bezier_points)

# Fungsi untuk membuat array dari titik bezier
def generate_bezier(point1, point2, point3, iterations):
    bezier_points = [point1]
    bezier_points_with_dnc(point1, point2, point3, 0, iterations, bezier_points)
    bezier_points.append(point3)
    return bezier_points

points = [(0, 0), (1, 1), (2, 0)]
iteration = 2
bezier = generate_bezier(points[0], points[1], points[2], iteration)
print(bezier)