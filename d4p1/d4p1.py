def d4p1(input):
    
    sum = 0
    lines = len(input)

    for i in range(lines):
        linelen = len(input[i])

        for j in range(linelen):
            if input[i][j] != 'X':
                continue

            else:
                for h in [-1, 0, 1]:
                    for v in [-1, 0, 1]:
                        if 0 <= (i + v) and (i + v) < lines and 0 <= (j + h) and (j + h) < linelen:
                            if input[i + v][j + h] == 'M':
                                if 0 <= (i + 2 * v) and (i + 2 * v) < lines and 0 <= (j + 2 * h) and (j + 2 * h) < linelen:
                                    if input[i + 2 * v][j + 2 * h] == 'A':
                                        if 0 <= (i + 3 * v) and (i + 3 * v) < lines and 0 <= (j + 3 * h) and (j + 3 * h) < linelen:
                                            if input[i + 3 * v][j + 3 * h] == 'S':
                                                sum += 1

    return sum



if __name__ == '__main__':
    with open('./d4p1/input.txt') as f:
        input = f.readlines()
        print(d4p1(input))