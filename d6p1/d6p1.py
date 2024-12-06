def d6p1(input):
    move_guard(input)
    
    count = 0
    for i in input:
        for j in i:
            if j == 'X':
                count += 1

    return count

def find_guard(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] in ['^', '>', '<', 'v']:
                return (i, j)

def move_guard(input):
    length = len(input)
    width = len(input[0])
    total = length * width
    check = False
    position = find_guard(input)
    while check == False:
        # Up
        if input[position[0]][position[1]] == '^':
            if position[0] - 1 < 0:
                input[position[0]][position[1]] = 'X'
                check = True
            elif input[position[0] - 1][position[1]] == '#':
                input[position[0]][position[1]] = '>'
                position = (position[0], position[1])
            else:
                input[position[0] - 1][position[1]] = '^'
                input[position[0]][position[1]] = 'X'
                position = (position[0] - 1, position[1])
        # Right
        elif input[position[0]][position[1]] == '>':
            if width <= position[1] + 1:
                input[position[0]][position[1]] = 'X'
                check = True
            elif input[position[0]][position[1] + 1] == '#':
                input[position[0]][position[1]] = 'v'
                position = (position[0], position[1])
            else:
                input[position[0]][position[1] + 1] = '>'
                input[position[0]][position[1]] = 'X'
                position = (position[0], position[1] + 1)
        # Down
        elif input[position[0]][position[1]] == 'v':
            if length <= position[0] + 1:
                input[position[0]][position[1]] = 'X'
                check = True
            elif input[position[0] + 1][position[1]] == '#':
                input[position[0]][position[1]] = '<'
                position = (position[0], position[1])
            else:
                input[position[0] + 1][position[1]] = 'v'
                input[position[0]][position[1]] = 'X'
                position = (position[0] + 1, position[1])
        # Left
        elif input[position[0]][position[1]] == '<':
            if position[1] - 1 < 0:
                input[position[0]][position[1]] = 'X'
                check = True
            elif input[position[0]][position[1] - 1] == '#':
                input[position[0]][position[1]] = '^'
                position = (position[0], position[1])
            else:
                input[position[0]][position[1] - 1] = '<'
                input[position[0]][position[1]] = 'X'
                position = (position[0], position[1] - 1)

    return input


if __name__ == '__main__':
    with open('./d6p1/input.txt') as f:
        raw = list(f.readlines())
    input = []
    for i in raw:
        input.append(list(i.strip()))
    print(d6p1(input))