import numpy as np

# Fungsi untk mencari titik pada kurva bezier dengan bruteforce untuk 3 titik
def bezier_points_with_bruteforce(points, iteration):
    points = np.array(points)
    total = 2 ** iteration + 1
    t = np.linspace(0, 1, total)
    bezier_points = np.zeros((total, 2))
    
    # Perhitungan x dan y digabung jadi 1
    for i in range(total):
        bezier_points[i] = (1 - t[i])**2 * points[0] + 2 * (1 - t[i]) * t[i] * points[1] + t[i]**2 * points[2]
    return bezier_points

points = [(0, 0), (1, 1), (2, 0)]
iteration = 2
bezier_points = bezier_points_with_bruteforce(points, iteration)
print(bezier_points)