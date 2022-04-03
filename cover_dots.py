"""По данным nn отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано 1<=n<=100 отрезков. Каждая из последующих n строк содержит по два числа 0 <= l <= r <= 10^9, задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них."""

count, points = 0, []

n = int(input())
for i in range(n):
    points.append(tuple(map(int, input().split())))

points.sort(key=lambda coordinate: coordinate[1])

need_points = [points.pop(0)[1]]

for point in points:
    if point[0] <= need_points[count] <= point[1]:
        continue
    else:
        need_points.append(point[1])
        count += 1

print(len(need_points))
print(*need_points)
