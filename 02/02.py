def is_safe(report):
    last = report[0]
    faultyReports = 0
    ascending = report[0] < report[1]
    for i in range(1, len(report)):
        if ascending:
            if last > report[i]:
                print(str(last) + ">" + str(report[i]))
                faultyReports += 1
            if last == report[i] or last + 3 < report[i]:
                print(str(last) + "asc == or + 3 " + str(report[i]))
                faultyReports += 1
        else:
            if last < report[i]:
                print(str(last) + "<" + str(report[i]))
                faultyReports += 1
            if last == report[i] or last > report[i] + 3:
                print(str(last) + "desc == or +3 " + str(report[i]))
                faultyReports += 1
        last = report[i]
    return faultyReports <= 1


file1 = open("02/input.txt", "r")
fileContent = file1.readlines()

reports = []

for line in fileContent:
    reports.append([int(x) for x in line.split()])

print("Reports: " + str(len(reports)))

safeReports = 0
for report in reports:
    if is_safe(report):
        safeReports += 1

print("Safe reports: " + str(safeReports))
