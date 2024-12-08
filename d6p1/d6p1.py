if __name__ == '__main__':
    with open('./d6p1/input.txt') as f:
        input = f.readlines()

    range = {j + i * 1j: c  for i,r in enumerate(input)
                            for j,c in enumerate(r.strip())}
    
    def get_start_pos():
        for position, state in range.items():
            if state == '^':
                return position

    def guard_path(domain):
        guard_pos = get_start_pos()
        direction = -1j
        path = [] 
        while guard_pos in domain:
            if domain.get(guard_pos + direction) == '#':
                direction *= 1j
                guard_pos += direction    
            else:
                guard_pos += direction
            if guard_pos not in path:
                path.append(guard_pos)
        return path

    path = guard_path(range) 

    print(len(path))  
                