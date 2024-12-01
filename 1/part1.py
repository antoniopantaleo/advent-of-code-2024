import re
from sys import maxsize as maxint
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

def findNextDistance(left, right) -> int:
    minimumLeft = maxint
    minimumRight = maxint
    for l, r in zip(left, right):
        if l < minimumLeft:
            minimumLeft = l
        if r < minimumRight:
            minimumRight = r

    distance = abs(minimumLeft - minimumRight)
    left.remove(minimumLeft)
    right.remove(minimumRight)
    return distance

distances = []
while len(left) > 0:
    distance = findNextDistance(left, right)
    distances.append(distance)

print(sum(distances))