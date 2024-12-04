import re

# 0,0 -> 0,n
# 0,n -> n,n
# n,n -> n,0
# n,0 -> 0,0


def rotate_90deg(lines):
    new_lines = []
    i = 0
    for line_index in range(len(lines)):
        line = lines[len(lines) - line_index - 1]

        for c in line:
            if line_index == 0:
                new_lines.append(c)
            else:
                new_lines[i] += (c)
            i += 1
        i = 0
    return new_lines


def count_horizontal(lines):
    count = 0
    for line in lines:
        matches = re.findall("XMAS", line)
        count += len(matches)

    print("Found horizontal: " + str(count))
    return count


def count_diagonal(lines):
    count = 0
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] != 'X':
                continue

            if y+1 >= len(lines) or x+1 >= len(line) or lines[y+1][x+1] != 'M':
                continue
            if y+2 >= len(lines) or x+2 >= len(line) or lines[y+2][x+2] != 'A':
                continue
            if y+3 >= len(lines) or x+3 >= len(line) or lines[y+3][x+3] != 'S':
                continue

            count += 1
    print("Found diagonal: " + str(count))
    return count


def count_x_mas(lines):
    count = 0
    for y in range(len(lines)):
        if y == 0 or y == len(lines)-1:
            continue
        line = lines[y]
        for x in range(len(line)):
            if x == 0 or x == len(line)-1:
                continue

            if line[x] != 'A':
                continue
            if lines[y+1][x+1] == 'S' and lines[y+1][x-1] == 'S' and lines[y-1][x+1] == 'M' and lines[y-1][x-1] == 'M':
                count += 1
    print("Found x-mas: " + str(count))
    return count


with open("04/input.txt") as f:
    fileContent = f.read().splitlines()
count = 0
for i in range(4):
    # print(fileContent)
    count += count_horizontal(fileContent)
    count += count_diagonal(fileContent)
    fileContent = rotate_90deg(fileContent)

print("Total XMAS: " + str(count))

x_count = 0
for i in range(4):
    # print(fileContent)
    x_count += count_x_mas(fileContent)
    fileContent = rotate_90deg(fileContent)
print("Total X-MAS: " + str(x_count))
