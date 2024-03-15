# Fungsi untuk mencari titik tengah dari 2 titik
def find_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Fungsi untuk mencari titik pada kurva bezier dengan dnc untuk n titik
def bezier_points_with_dnc_n(point, iteration):
    # Membuat titik awal
    bezier_points = [point[0]]

    def recursive(points, current_iteration):
        if current_iteration < iteration:
            new_points = [points]
            for _ in range(len(points) - 1):
                new_mid = [find_mid_point(points[i], points[i+1]) for i in range(len(points)-1)]
                new_points.append(new_mid)
                points = new_mid

            # Membuat sisi kiri
            left = []
            for point in new_points:
                left.append(point[0])

            # Membuat sisi kanan
            right = []
            for i in range(len(new_points)-1, -1, -1):  # Iterating in reverse order
                right.append(new_points[i][-1])

            # rekursif untuk sisi kiri lalu sisi kanan
            recursive(left, current_iteration + 1)
            bezier_points.append(new_points[-1][0])
            recursive(right, current_iteration + 1)

    recursive(point, 0)
    # Menambahkan titik akhir
    bezier_points.append(point[-1])
    return bezier_points

points = [(0, 0), (1, 1), (2, 0)]
iteration = 2
bezier_points = bezier_points_with_dnc_n(points, iteration)
print(bezier_points)