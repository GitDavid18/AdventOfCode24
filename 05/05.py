def page_before(a, b, rules):
    if b in rules[a]:
        return True

    return False


def is_valid_page_order(pages, rules):
    if len(pages) == 1:
        return True

    if is_valid_page_order(pages[1:], rules):
        if page_before(pages[0], pages[1], rules):
            return True
        fix_pages(pages)
    return False


def fix_pages(pages):
    print("flipping " + str(pages[0]) + "and" + str(pages[1]))
    save = pages[0]
    pages[0] = pages[1]
    pages[1] = save

    return pages


def get_middle(list):
    return list[int((len(list) - 1)/2)]


with open("05/example_rules.txt") as f:
    # with open("05/rules.txt") as f:
    fileContent = f.read().splitlines()

rules = []
for line in fileContent:
    split = line.split('|')
    rules.append((int(split[0]), int(split[1])))

print(rules)

greater_map = []
for i in range(100):
    greater_map.append([])

for rule in rules:
    greater_map[rule[0]].append(rule[1])

print(greater_map)

with open("05/example_pages.txt") as f:
    # with open("05/pages.txt") as f:
    fileContent = f.read().splitlines()
pages = []

for line in fileContent:
    split = line.split(',')
    page = []
    for num in split:
        page.append(int(num))
    pages.append(page)

print(pages)

sum = 0
sum_fixed = 0

for page in pages:
    if is_valid_page_order(page, greater_map):
        print("Me: ")
        print(page)
        print(get_middle(page))
        sum += get_middle(page)
    else:
        print(page)
        # fixed = fix_pages(page, greater_map)
        # print(fixed)
        print(get_middle(page))
        sum_fixed += get_middle(page)
print(sum)
print(sum_fixed)
