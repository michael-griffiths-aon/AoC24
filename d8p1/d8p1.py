from itertools import combinations as combo

if __name__ == '__main__':
    with open('./d8p1/input.txt') as f:
        input = f.readlines()

    range = {j + i * 1j: c  for i,r in enumerate(input)
                            for j,c in enumerate(r.strip())}
    
    chars = set(range.values()) - {'.', '#'}
    
    sum = 0
    antinodes = []
    for char in chars:
        nodes = [k for k,v in range.items() if v == char]
        for pair in combo(nodes, 2):
            diff = pair[1] - pair[0]
            if pair[1] + diff in range and pair[1] + diff not in antinodes:
                sum += 1
                antinodes.append(pair[1] + diff)
            if pair[0] - diff in range and pair[0] - diff not in antinodes:
                sum += 1
                antinodes.append(pair[0] - diff)

    print(sum)