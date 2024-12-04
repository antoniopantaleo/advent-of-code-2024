import re
DEMO = False

input = "demo2.txt" if DEMO else "input.txt"
line = open(input).read()

regex = r"mul\((\d+),(\d+)\)"
dont = r"(?<!don't\(\))"
result = 0

def getMultiplications(string):
    sum = 0
    for match in re.findall(regex, string):
        sum += int(match[0]) * int(match[1])
    return sum

for zone in re.split(r"don't\(\)|do\(\)", line):
    if re.search(dont + re.escape(zone), line) is not None:
        result += getMultiplications(zone)

print(result)