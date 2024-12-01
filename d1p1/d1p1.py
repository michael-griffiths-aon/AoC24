import pandas as pd

def d1p1(input):
    list1 = sorted(input[0].tolist())
    list2 = sorted(input[1].tolist())

    diff = []

    for i in range(len(list1)):
        diff.append(abs(list1[i] - list2[i]))
    
    return sum(diff)

if __name__ == '__main__':
    with open('./d1p1/input.txt') as f:
        input = pd.read_csv('./d1p1/input.txt', header = None, sep = '\s+')
    print(d1p1(input))