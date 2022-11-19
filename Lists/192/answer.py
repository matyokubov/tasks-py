lights = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

# Input data
changes = [
    [13, 85, 77],
    [25, 50, 45],
    [65, 79, 9]
]

# Calculate starts
for row in range(len(changes)):
    for col in range(len(changes[row])):
        if 0!=changes[row][col]:
            targets = [(row, col), (row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            targets = list(filter(lambda t: t[0] >= 0 and
                                            t[0] <= len(changes)-1 and
                                            t[1] >= 0 and t[1] <= len(changes[row])-1,
                                        targets
                                    ))
            for i in range(changes[row][col]):
                for tr, tc in targets:
                    lights[tr][tc] = abs(lights[tr][tc]-1)
# Have Finish

# Output result
for row in lights:
    print(row)