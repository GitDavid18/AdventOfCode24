def calculate_plus(searchedResult, curResult, nums):
    curResult += nums[0]
    if len(nums) == 1:
        return searchedResult == curResult
    if curResult > searchedResult:
        return False
    return calculate_plus(searchedResult, curResult, nums[1:]) or calculate_times(searchedResult, curResult, nums[1:]) or calculate_concat(searchedResult, curResult, nums[1:])


def calculate_times(searchedResult, curResult, nums):
    curResult *= nums[0]
    if len(nums) == 1:
        return searchedResult == curResult

    if curResult > searchedResult:
        return False

    return calculate_plus(searchedResult, curResult, nums[1:]) or calculate_times(searchedResult, curResult, nums[1:]) or calculate_concat(searchedResult, curResult, nums[1:])


def calculate_concat(searchedResult, curResult, nums):
    curResult *= 10
    curResult += nums[0]
    if len(nums) == 1:
        return searchedResult == curResult

    if curResult > searchedResult:
        return False

    return calculate_plus(searchedResult, curResult, nums[1:]) or calculate_times(searchedResult, curResult, nums[1:]) or calculate_concat(searchedResult, curResult, nums[1:])


def can_calculate(searchedResult,  nums):
    # or calculate_plus(searchedResult, 0, nums) or calculate_concat(searchedResult, 0, nums)
    return calculate_times(searchedResult, 1, nums)


# with open("07/example_input.txt") as f:
with open("07/input.txt") as f:
    fileContent = f.read().splitlines()

input = []

for line in fileContent:
    split = line.split(':')
    calc = split[1].split()
    nums = []
    for num in calc:
        nums.append(int(num))
    input.append((int(split[0]), nums))

print(input)
print(len(input))

sum = 0
for calc in input:
    if can_calculate(calc[0], calc[1]):
        print(str(sum) + ' + ' + str(calc[0]) + ' = ' + str(sum + calc[0]))
        sum += calc[0]
    # else:
        # print("cannot: " + str(calc))

print(sum)
