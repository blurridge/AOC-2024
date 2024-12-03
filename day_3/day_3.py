# Part One
import re

def get_line_sum(line):
    pattern = r"mul\(\s?(\d+)\s?,\s?(\d+)\s?\)"
    matches = re.findall(pattern, line)
    sum = 0
    for match in matches:
        product = int(match[0]) * int(match[1])
        sum += product
    return sum

sum = 0
with open("input.txt", "r") as input:
    for line in input:
        sum += get_line_sum(line)
print(f"The sum is: {sum}")  # 159892596

# Part Two
lines = []
sum = 0
with open("input.txt", "r") as input:
    for line in input:
        lines.append(line)
    single_line = "".join(lines)
    split_lines = single_line.split("don't()")
    sum += get_line_sum(split_lines[0])
    for i in range(1, len(split_lines)):
        index = split_lines[i].find("do()")
        string_with_do = split_lines[i][index:]
        sum += get_line_sum(string_with_do)
print(f"The sum is: {sum}")
