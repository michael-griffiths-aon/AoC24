import re

def optimal_buttons(machine_nums):
    x_1, x_2 = machine_nums[0][0], machine_nums[1][0]
    y_1, y_2 = machine_nums[0][1], machine_nums[1][1]
    x_target, y_target = machine_nums[2][0] + 10000000000000, machine_nums[2][1] + 10000000000000

    determinant = x_1 * y_2 - x_2 * y_1

    if determinant != 0:
        a, b = int((y_2 * x_target - x_2 * y_target) / determinant), int((x_1 * y_target - y_1 * x_target) / determinant)
        if a * x_1 + b * x_2 == x_target and a * y_1 + b * y_2 == y_target:
            return 3 * a + b
        else:
            return 0
    else:
        return 0

sum = 0

with open("./d13p1/input.txt") as f:
    machine_nums = []
    for line in f:
        if len(machine_nums) < 3:
            machine = re.findall(r"[\d,]", line)
            num1 = int(''.join(machine[:machine.index(',')]))
            num2 = int(''.join(machine[machine.index(',') + 1:]))
            machine_nums.append((num1, num2))
        else:
            sum += optimal_buttons(machine_nums)
            machine_nums = []
    sum += optimal_buttons(machine_nums)

print(sum)