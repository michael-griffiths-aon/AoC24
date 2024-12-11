with open('./d10p1/input.txt') as f:
    data = f.read().split()

processed_data = []
for i in range(len(data)):
    processed_line = []
    for j in range(len(data[0])):
        processed_line.append(data[i][j])
    processed_data.append(list(map(int, processed_line)))

data = processed_data

def trailhead(data, i, j):
    for h, w in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if i + h >= 0 and i + h < len(data) and j + w >= 0 and j + w < len(data[0]):
            if data[i + h][j + w] == data[i][j] + 1:
                if data[i][j] == 8 and (i + h, j + w) not in passed_trailheads:
                    global total_trailheads
                    total_trailheads += 1
                    passed_trailheads.append((i + h, j + w))
                else:
                    trailhead(data, i + h, j + w)

    return 1

total_trailheads = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 0:
            passed_trailheads = []
            trailhead(data, i, j)


print(total_trailheads)