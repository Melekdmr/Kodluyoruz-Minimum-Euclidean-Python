# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Noktalar listesi (örnek noktalar)
points = [(1, 2), (3, 4), (5, 8), (7, 6)]

# Mesafeleri saklamak için liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma ve yazdırma
min_distance = min(distances)
min_distance
