import numpy as np
import csv as csv

def d5p2(rules, reports):
    sum = 0
    reordered_reports = []
    for report in reports:
        pertinent_rules = []
        check = True
        for rule in rules:
            if check_rule(report, rule):
                check = False
        if check:
            continue
        else:
            reordered_reports.append(reorder_report(report, rules))

    for report in reordered_reports:
        midpoint = int(len(report) / 2)
        sum += report[midpoint]

    return sum

def check_rule(report, rule):
    for i in range(len(report)):
        if report[i] == rule[1]:
            if rule[0] in report[list(report).index(report[i]):]:
                return True

    return False


def reorder_report(report, rules):
    unchanged = False
    while unchanged == False:
        report_copy = report.copy()
        for rule in rules:
            if rule[0] in report_copy and rule[1] in report_copy:
                index_0 = report_copy.index(rule[0])
                index_1 = report_copy.index(rule[1])
                if index_0 > index_1:
                    report_copy[index_0], report_copy[index_1] = report_copy[index_1], report_copy[index_0]
        if report == report_copy:
            unchanged = True
        report = report_copy

    return report


if __name__ == '__main__':
    rules = np.genfromtxt('./d5p2/input1.txt', delimiter='|', dtype=int).tolist()
    with open('./d5p2/input2.txt') as f:
        reports = [list(map(int,rec)) for rec in csv.reader(f, delimiter=',')]
    print(d5p2(rules, reports))