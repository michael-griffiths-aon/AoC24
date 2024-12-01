import pandas as pd

def d1p2(input):
    list1 = sorted(input[0].tolist())
    list2 = sorted(input[1].tolist())

    sum = 0

    for i in range(len(list1)):
        count = 0

        for j in range(len(list2)):
            if list1[i] == list2[j]:
                count += 1
        sum += list1[i] * count
    
    return sum

if __name__ == '__main__':
    with open('./d1p2/input.txt') as f:
        input = pd.read_csv('./d1p2/input.txt', header = None, sep = '\s+')
    print(d1p2(input))