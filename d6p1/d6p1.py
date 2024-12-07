def locate_blocks(input):
    blocks = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '#':
                blocks.append(complex(j, i))

    return blocks

def locate_guard(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '^':
                return complex(j, i)

def guard_path(input):
    length = len(input)
    width = len(input[0])
    guard_pos = locate_guard(input)
    path = []
    blocks = locate_blocks(input)
    direction = complex(0, -1)
    inrange = True
    while inrange:
        if guard_pos not in path:
            path.append(guard_pos)
        if (guard_pos + direction).imag < 0 or (guard_pos + direction).imag >= length or (guard_pos + direction).real < 0 or (guard_pos + direction).real >= width:
            inrange = False
        if guard_pos + direction in blocks:
            direction *= 1j
            guard_pos += direction
        else:
            guard_pos += direction

    return path

def d6p1(input):
    path = guard_path(input)

    return len(path)

if __name__ == '__main__':
    with open('./d6p1/input.txt') as f:
        raw = list(f.readlines())
    input = []
    for i in raw:
        input.append(list(i.strip()))
    print(d6p1(input))
                