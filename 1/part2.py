import re
from sys import maxsize as maxint
from collections import defaultdict
DEMO = False

input = "demo1.txt" if DEMO else "input.txt"
input = open(input).readlines()
left = []
right = []
for line in input:
    match = re.match("(\\d+)\\s+(\\d+)", line)
    l, r = match.group(1), match.group(2)
    left.append(int(l))
    right.append(int(r))

similaritiesDict = {}
occurencesDict = defaultdict(int)

for number in left:
    occurrences = right.count(number)
    similaritiesDict[number] = occurrences
    occurencesDict[number] += 1

result = 0
for (a, b), (_, d) in zip(similaritiesDict.items(), occurencesDict.items()):
    result += (d * (a * b))

print(result)