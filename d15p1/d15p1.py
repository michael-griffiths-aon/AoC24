with open("./d15p1/input1.txt") as f:
    data = f.read().split("\n")

warehouse = {j + i * 1j: c  for i,r in enumerate(data)
                            for j,c in enumerate(r.strip())}

width = max(int(x.real) for x in warehouse.keys()) + 1
length = max(int(x.imag) for x in warehouse.keys()) + 1

with open("./d15p1/input2.txt") as f:
    moves = ''.join(f.read().split("\n"))

def move_boxes(warehouse, pos, direction):
    if warehouse[pos + direction] == "O":
        warehouse = move_boxes(warehouse, pos + direction, direction)
    if warehouse[pos + direction] == ".":
        warehouse[pos + direction] = "O"
        if warehouse[pos] == "O":
            warehouse[pos] = "."
        if warehouse[pos - direction] == "@":
            warehouse[pos] = "@"
            warehouse[pos - direction] = '.'
    return warehouse

def move_robot(warehouse, move):
    pos = [k for k,v in warehouse.items() if v == "@"][0]
    move_dict = {"^": -1j, "v": 1j, "<": -1, ">": 1}

    direction = move_dict[move]
    new_pos = pos + direction
    if new_pos in warehouse and warehouse[new_pos] != "#":
        if new_pos in warehouse and warehouse[new_pos] == "O":
            warehouse = move_boxes(warehouse, pos, direction)
        else:
            warehouse[new_pos] = "@"
            warehouse[pos] = "."
    elif new_pos in warehouse and warehouse[new_pos] == "#":
        return warehouse

    return warehouse

for i in range(len(moves)):
    warehouse = move_robot(warehouse, moves[i])

sum = 0
for k,v in warehouse.items():
    if v == "O":
        sum += 100 * int(k.imag) + int(k.real)

print(sum)