import numpy as np
from itertools import pairwise

def d2p1(input):
    safe_reports = 0

    for i in range(len(input)):
        report = []

        report = list(map(int, input[i].split()))

        diffs = [y - x for x, y in pairwise(report)]

        if check_diffs(diffs):
            safe_reports += 1

    return safe_reports

def check_diffs(input = []):
    if any(np.abs(input) == 0) or any(np.abs(input) > 3):
        return False
    
    if all(np.sign(input) < 0) or all(np.sign(input) > 0):
        return True
    
    return False

if __name__ == '__main__':
    with open('./d2p1/input.txt') as f:
        input = f.readlines()
    print(d2p1(input))