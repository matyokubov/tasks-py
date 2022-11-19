from math import sqrt

n = [(0, 1), (5, 8), (9, 9), (7,3)]
parts = []
c = []
d = []

# 01. Get triangle cordinates
for a1 in n:
    for a2 in n:
        for a3 in n:
            parts.append([a1, a2, a3])
for part in parts:
    if sorted(part) == sorted(list(set(part))):
        c.append(part)
for part2 in c:
    d.append(tuple(sorted(part2)))
triangles = list(set(d))

# 2. Get sizes
sizes = []
for t in triangles:
    a = sqrt((t[0][0]-t[1][0])**2+(t[0][1]-t[1][1])**2)
    b = sqrt((t[0][0]-t[2][0])**2+(t[0][1]-t[2][1])**2)
    c = sqrt((t[1][0]-t[2][0])**2+(t[1][1]-t[2][1])**2)
    sizes.append((a, b, c))

# 3. Get surfaces
surfaces = []
for tSizes in sizes:
    halfP = (tSizes[0]+tSizes[1]+tSizes[2])/2
    surface = sqrt(halfP*(halfP-tSizes[0])*(halfP-tSizes[1])*(halfP-tSizes[2]))
    surfaces.append(surface)

res = max(surfaces)
print(res)