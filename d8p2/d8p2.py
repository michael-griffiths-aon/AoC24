import numpy as np
import cmath as cm
from itertools import combinations as combo

if __name__ == '__main__':
    with open('./d8p2/input.txt') as f:
        input = f.readlines()

    domain = {j + i * 1j: c for i,r in enumerate(input)
                            for j,c in enumerate(r.strip())}
    
    chars = set(domain.values()) - {'.'}
    
    sum = 0
    antinodes = []
    for char in chars:
        nodes = [k for k,v in domain.items() if v == char]
        for pair in combo(nodes, 2):
            if pair[0] not in antinodes:
                sum += 1
                antinodes.append(pair[0])
            if pair[1] not in antinodes:
                sum += 1
                antinodes.append(pair[1])
            for point in domain:
                if point not in antinodes:
                    if cm.phase(pair[1] - point) == cm.phase(pair[0] - point):
                        sum += 1
                        antinodes.append(point)

    print(sum)