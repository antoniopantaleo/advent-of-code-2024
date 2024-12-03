import re
DEMO = False

input = "demo1.txt" if DEMO else "input.txt"
line = open(input).read()

regex = r"mul\((\d+),(\d+)\)"
result = 0
for match in re.findall(regex, line):
    result += int(match[0]) * int(match[1])

print(result)
