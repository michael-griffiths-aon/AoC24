from functools import cache

with open('./d11p2/input.txt') as f:
    rocks = f.read().split()
    rocks = list(map(int, rocks))

@cache
def blink(rock, blinks):
    if blinks == 0:
        return 1
    if rock == 0:
        return blink(1, blinks - 1)
    l = len(str(rock))
    if l % 2 == 1:
        return blink(rock * 2024, blinks - 1)
    else:
        return blink(rock // 10 ** (l//2), blinks - 1) + blink(rock %  10 ** (l//2), blinks - 1)

count = 0
for i in range(len(rocks)):
    count += blink(rocks[i], 75)

print(count)