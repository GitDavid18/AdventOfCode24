import re

file1 = open("03/input.txt", "r")
fileContent = file1.readlines()

matches = re.findall("mul\((\d{1,3}),\s*(\d{1,3})\)", fileContent[0])

sum = 0

for match in matches:
    print(match)
    sum += int(match[0]) * int(match[1])

print(sum)


matches = re.findall(
    "mul\((\d{1,3}),\s*(\d{1,3})\)|(don\'t\(\))|(do\(\))", fileContent[0])

sum = 0
enable = True
for match in matches:
    print(match)
    if match[2] == 'don\'t()':
        enable = False
        continue
    if match[3] == 'do()':
        enable = True
        continue
    if enable:
        sum += int(match[0]) * int(match[1])
print(sum)
