import numpy as np
import csv as csv

def d5p1(rules, reports):
    sum = 0
    for report in reports:
        check = True
        for rule in rules:
            if check_rule(report, rule):
                check = False
        if check:
            midpoint = int(len(report) / 2)
            sum += report[midpoint]

    return sum

def check_rule(report, rule):
    for i in range(len(report)):
        if report[i] == rule[1]:
            if rule[0] in report[list(report).index(report[i]):]:
                return True

    return False

if __name__ == '__main__':
    rules = np.genfromtxt('./d5p1/input1.txt', delimiter='|', dtype=int).tolist()
    with open('./d5p1/input2.txt') as f:
        reports = [list(map(int,rec)) for rec in csv.reader(f, delimiter=',')]
    print(d5p1(rules, reports))