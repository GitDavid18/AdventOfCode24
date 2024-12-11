def turn_right(guard):
    if (guard["dir"] == '^'):
        guard["dir"] = '>'
        return
    if (guard["dir"] == '>'):
        guard["dir"] = 'v'
        return

    if (guard["dir"] == 'v'):
        guard["dir"] = '<'
        return

    if (guard["dir"] == '<'):
        guard["dir"] = '^'
        return


def pos_out_of_bounds(x, y, grid):
    if len(grid[0]) - 1 >= x and len(grid)-1 >= y:
        return False
    return True


def move(guard, grid):
    start_x = guard["x"]
    start_y = guard["y"]

    if (guard["dir"] == '^'):
        new_y = guard["y"] - 1
        if pos_out_of_bounds(start_x, new_y, grid):
            return False
        if grid[new_y][start_x] == '#':
            turn_right(guard)
        else:
            guard["y"] = new_y
    if (guard["dir"] == 'v'):
        new_y = guard["y"] + 1
        if pos_out_of_bounds(start_x, new_y, grid):
            return False
        if grid[new_y][start_x] == '#':
            turn_right(guard)
        else:
            guard["y"] = new_y

    if (guard["dir"] == '>'):
        new_x = guard["x"] + 1
        if pos_out_of_bounds(new_x, start_y, grid):
            return False
        if grid[start_y][new_x] == '#':
            turn_right(guard)
        else:
            guard["x"] = new_x
    if (guard["dir"] == '<'):
        new_x = guard["x"] - 1
        if pos_out_of_bounds(new_x, start_y, grid):
            return False
        if grid[start_y][new_x] == '#':
            turn_right(guard)
        else:
            guard["x"] = new_x

    grid[start_y][start_x] = 'X'
    grid[guard["y"]][guard["x"]] = guard["dir"]
    return True


# with open("06/example_input.txt") as f:
with open("06/input.txt") as f:
    fileContent = f.read().splitlines()

grid = []

guard = {"dir": '^',
         "x": 0,
         "y": 0}

for row in fileContent:
    new_row = []
    grid.append(new_row)
    for char in row:
        new_row.append(char)
        if char == '^':
            guard.update({"x": len(new_row) - 1})
            guard.update({"y": len(grid) - 1})
            print(guard)

print(grid[guard["y"]][guard["x"]])
# print(grid)

guard_in_field = True

while (guard_in_field):
    print(guard)
    guard_in_field = move(guard, grid)
grid[guard["y"]][guard["x"]] = 'X'
print("He left")
print(grid)
count = 0
for row in grid:
    for char in row:
        if char == 'X':
            count += 1

print(count)
