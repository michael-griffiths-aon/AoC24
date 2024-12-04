def d4p2(input):
    
    sum = 0
    lines = len(input)

    admissible = [[['M', 'M'], ['S', 'S']], [['M', 'S'], ['M', 'S']], [['S', 'S'], ['M', 'M']], [['S', 'M'], ['S', 'M']]]

    for i in range(lines):
        linelen = len(input[i])

        for j in range(linelen):
            corners = [['?'] * 2 for i in range(2)]

            if input[i][j] != 'A':
                continue
            else:
                for h in [-1, 1]:
                    for v in [-1, 1]:
                        if 0 <= (i + v) and (i + v) < lines and 0 <= (j + h) and (j + h) < linelen:
                            if h == -1 and v == -1:
                                corners[0][0] = input[i + v][j + h]
                            if h == -1 and v == 1:
                                corners[1][0] = input[i + v][j + h]
                            if h == 1 and v == -1:
                                corners[0][1] = input[i + v][j + h]
                            if h == 1 and v == 1:
                                corners[1][1] = input[i + v][j + h]
                            if corners in admissible:
                                sum += 1

    return sum

if __name__ == '__main__':
    with open('./d4p2/input.txt') as f:
        input = f.readlines()
        print(d4p2(input))