import re

def d3p2(input):
    statements = re.findall("(mul\([0-9]{1,9}\,[0-9]{1,9}\)|do\(\)|don\'t\(\))", input)

    sum = 0

    do = True

    for i in range(len(statements)):
        if statements[i].startswith('mul'):
            if do == True:
                numbers = list(map(int, statements[i][4:len(statements[i]) - 1].split(',')))

                sum += numbers[0] * numbers[1]
            if do == False:
                continue
        elif statements[i].startswith('don\'t()'):
            do = False
        else:
            do = True

    return sum


if __name__ == '__main__':
    with open('./d3p2/input.txt') as f:
        input = f.read().replace('\n', '')
    print(d3p2(input))