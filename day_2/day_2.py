def check_in_range(num):
    return num >= 1 and num <= 3


def is_safe(report):
    if report == sorted(report, reverse=True) or report == sorted(report):
        diffs = [
            check_in_range(abs(report[i] - report[i + 1]))
            for i in range(len(report) - 1)
        ]
        return all(diffs)

# Part 1
reports = []
with open("input.txt", "r") as input:
    for line in input:
        levels = list(map(int, line.split()))
        reports.append(levels)
safe = 0
for report in reports:
    if is_safe(report):
        safe += 1
print(f"The number of safe levels are: {safe}")  # 252


# Part 2
reports = []
with open("input.txt", "r") as input:
    for line in input:
        levels = list(map(int, line.split()))
        reports.append(levels)
safe = 0
for report in reports:
    if is_safe(report):
        safe += 1
    else:
        for i in range(len(report)):
            modified_report = report.copy()
            modified_report.pop(i)
            if is_safe(modified_report):
                safe += 1
                break
print(f"The number of safe levels with the dampener are: {safe}")  # 324
