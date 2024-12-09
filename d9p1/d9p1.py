with open('./d9p1/input.txt') as f:
    data = f.read().strip('\n')

    ID = 0
    processed_data = []

    for i in range(len(data)):
        if i == 0 or i % 2 == 0:
            for i in range(int(data[i])):
                processed_data.append(int(str(ID)))
            ID += 1
        else:
            for i in range(int(data[i])):
                processed_data.append('.')

    l = 0
    r = len(processed_data) - 1

    nums = [1 for i in processed_data if i != '.']
    count_nums = sum(nums)

    sum = 0
    r = len(processed_data) - 1
    for i in range(count_nums):
        if processed_data[i] != '.':
            sum += int(processed_data[i]) * i
        else:
            while processed_data[r] == '.':
                r -= 1
            temp = processed_data[i]
            processed_data[i] = processed_data[r]
            processed_data[r] = temp
            sum += int(processed_data[i]) * i

    print(sum)
    
