DEMO = False

input = "demo1.txt" if DEMO else "input.txt"
reports = open(input).readlines()
reports = [[int(y) for y in x.split()] for x in reports]

result = 0

def isValidReport(report):
    decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))
    increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    monotone = decreasing or increasing
    if not monotone:
        return False
    for idx, number in enumerate(report[1:]):
        difference = number - report[idx]
        if abs(difference) > 3:
            return False
    return True

for report in reports:
    if isValidReport(report):
        result += 1
print(result)
