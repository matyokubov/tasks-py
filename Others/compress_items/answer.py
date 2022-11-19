# Input
a = [1, 1, 2, 1, 3, 4, 4]

compress = lambda data: data[:1] + [data[i] for i in range(1, len(data)) if data[i-1]!=data[i]]
compressed = compress(a)

# Output
print(compressed)