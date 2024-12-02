import numpy as np

def d2p1(input):
    safe_reports = 0

    for i in range(len(input)):
        safe = True
        
        report = []

        report = list(map(int, input[i].split()))

        l = 0
        m = 1
        r = 2

        while m < len(report):
            diff1 = report[l] - report[m]

            if abs(diff1) < 1 or abs(diff1) > 3:
                safe = False
                continue

            if r < len(report):
                diff2 = report[m] - report[r]

                if np.sign(diff1) != np.sign(diff2):
                    safe = False
                    continue

            l += 1
            m += 1
            r += 1

        if safe:
            safe_reports += 1

    return safe_reports


if __name__ == '__main__':
    with open('./d2p1/input.txt') as f:
        input = f.readlines()
    print(d2p1(input))