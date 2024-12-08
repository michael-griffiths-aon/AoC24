import itertools

if __name__ == '__main__':
    with open('d7p1/input.txt') as f:
        lines = f.read().strip().split('\n')

    sum = 0

    for line in lines:
        target = int(line.split()[0][:-1])
        values = list(map(int, line.split()[1:]))
        
        def test_operators(operators):
            rolling_sum = values[0]
            for i in range(1, len(values)):
                if operators[i - 1] == '+':
                    rolling_sum += values[i]
                elif operators[i - 1] == '*':
                    rolling_sum *= values[i]
                else:
                    rolling_sum = concatenate(rolling_sum, values[i])
            return rolling_sum

        def concatenate(a, b):
            return int(str(a) + str(b))

        for operators in itertools.product('*+~', repeat = len(values) - 1):#
            if test_operators(operators) == target:
                sum += target
                break

    print(sum)
