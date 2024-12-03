import re

def d3p1(input):
    statements = re.findall("(mul\([0-9]{1,9}\,[0-9]{1,9}\))", input)

    sum = 0

    for i in range(len(statements)):
        numbers = list(map(int, statements[i][4:len(statements[i]) - 1].split(',')))

        sum += numbers[0] * numbers[1]

    return sum

if __name__ == '__main__':
    with open('./d3p1/input.txt') as f:
        input = f.read().replace('\n', '')
    print(d3p1(input))