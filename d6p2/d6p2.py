if __name__ == '__main__':
    with open('./d6p2/input.txt') as f:
        input = f.readlines()

    range = {j + i * 1j: c  for i,r in enumerate(input)
                            for j,c in enumerate(r.strip())}
    
    def get_start_pos():
        for position, state in range.items():
            if state == '^':
                return position

    start_pos = get_start_pos()

    def guard_loop(domain):
        guard_pos = start_pos
        direction = -1j
        path_dir = []
        while guard_pos in domain:
            path_dir.append((guard_pos, direction))
            if domain.get(guard_pos + direction) == '#':
                direction *= 1j
            else:
                guard_pos += direction
            if (guard_pos, direction) in path_dir:
                return True, path_dir

        return False, path_dir

    path_dir = guard_loop(range)[1]
    path = {pos for pos, _ in path_dir}

    print(len(path))

    count = 0
    for i, pos in enumerate(path):
        print(i, '/', len(path))
        if guard_loop(range | {pos: '#'})[0]:
            print('Number of loops:', count)
            count += 1

    print(count)



            