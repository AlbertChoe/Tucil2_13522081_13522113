def find_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def find_bezier_points(point, iteration):
    # Membuat titik awal
    bezier_points = [point[0]]

    def recurse(points, current_iteration):
        if current_iteration < iteration:
            next_level_points = [points]
            for _ in range(len(points) - 1):
                temp = [find_mid_point(points[i], points[i+1]) for i in range(len(points)-1)]
                next_level_points.append(temp)
                points = temp

            # Membuat sisi kiri
            left_half = []
            for point in next_level_points:
                left_half.append(point[0])

            # Membuat sisi kanan
            right_half = []
            for i in range(len(next_level_points)-1, -1, -1):  # Iterating in reverse order
                right_half.append(next_level_points[i][-1])

            # rekursif untuk sisi kiri lalu sisi kanan
            recurse(left_half, current_iteration + 1)
            bezier_points.append(next_level_points[-1][0])
            recurse(right_half, current_iteration + 1)

    recurse(point, 0)
    
    # Menambahkan titik akhir
    bezier_points.append(point[-1])
    return bezier_points

control_points = [(0, 0), (1, 1), (2, 1), (3, 0)]
iteration = 3 
bezier_points = find_bezier_points(control_points, iteration)