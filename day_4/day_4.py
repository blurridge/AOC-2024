# Part One
def check_forwards(index, current_line):
    if index + 3 > (len(current_line) - 1):
        return False
    current_string = "".join(current_line[index : index + 4])
    return current_string.upper().strip() == "XMAS"


def check_backwards(index, current_line):
    if index - 3 < 0:
        return False
    current_string = "".join([current_line[index - i] for i in range(4)])
    return current_string.upper().strip() == "XMAS"


def check_upwards(index, current_line, line_index, all_lines):
    if line_index - 3 < 0:
        return False
    current_string = ""
    for i in range(4):
        current_string += all_lines[line_index - i][index]
    return current_string.upper().strip() == "XMAS"


def check_downwards(index, current_line, line_index, all_lines):
    if line_index + 3 > (len(all_lines) - 1):
        return False
    current_string = ""
    for i in range(4):
        current_string += all_lines[line_index + i][index]
    return current_string.upper().strip() == "XMAS"


def check_diagonal_se(index, current_line, line_index, all_lines):  # +x +y
    if index + 3 > (len(current_line) - 1) or line_index + 3 > (len(all_lines) - 1):
        return False
    current_string = ""
    for i in range(4):
        current_string += all_lines[line_index + i][index + i]
    return current_string.upper().strip() == "XMAS"


def check_diagonal_nw(index, current_line, line_index, all_lines):  # -x -y
    if index - 3 < 0 or line_index - 3 < 0:
        return False
    current_string = ""
    for i in range(4):
        current_string += all_lines[line_index - i][index - i]
    return current_string.upper().strip() == "XMAS"


def check_diagonal_sw(index, current_line, line_index, all_lines):  # -x +y
    if index - 3 < 0 or line_index + 3 > (len(all_lines) - 1):
        return False
    current_string = ""
    for i in range(4):
        current_string += all_lines[line_index + i][index - i]
    return current_string.upper().strip() == "XMAS"


def check_diagonal_ne(index, current_line, line_index, all_lines):  # +x -y
    if index + 3 > (len(current_line) - 1) or line_index - 3 < 0:
        return False
    current_string = ""
    for i in range(4):
        current_string += all_lines[line_index - i][index + i]
    return current_string.upper().strip() == "XMAS"


def check_xmas(current_line, line_index, all_lines):
    total = 0
    for index, char in enumerate(current_line):
        # Check if character is an "x"
        if char.lower() == "x":
            total += check_forwards(index, current_line)
            total += check_backwards(index, current_line)
            total += check_upwards(index, current_line, line_index, all_lines)
            total += check_downwards(index, current_line, line_index, all_lines)
            total += check_diagonal_se(index, current_line, line_index, all_lines)
            total += check_diagonal_sw(index, current_line, line_index, all_lines)
            total += check_diagonal_ne(index, current_line, line_index, all_lines)
            total += check_diagonal_nw(index, current_line, line_index, all_lines)
    return total


lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.strip())
grand_total = 0
for i, line in enumerate(lines):
    grand_total += check_xmas(line, i, lines)
print(f"The total is {grand_total}")  # 2646


# Part Two
def check_validity(top_left, bottom_left, top_right, bottom_right):
    if top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S':
        return True
    if top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M':
        return True
    if top_left == 'S' and bottom_left == 'S' and top_right == 'M' and bottom_right == 'M':
        return True
    if top_left == 'M' and bottom_left == 'M' and top_right == 'S' and bottom_right == 'S':
        return True  
    return False


def find_x(index, current_line, line_index, all_lines):
    if (
        index - 1 < 0
        or index + 1 > (len(current_line) - 1)
        or line_index - 1 < 0
        or line_index + 1 > (len(all_lines) - 1)
    ):
        return False
    top_left = all_lines[line_index - 1][index - 1]
    bottom_left = all_lines[line_index + 1][index - 1]
    top_right = all_lines[line_index - 1][index + 1]
    bottom_right = all_lines[line_index + 1][index + 1]

    if check_validity(top_left, bottom_left, top_right, bottom_right):
        return True
    return False


def check_mas(current_line, line_index, all_lines):
    total = 0
    for index, char in enumerate(current_line):
        # Check if character is an "a"
        if char.lower() == "a":
            total += find_x(index, current_line, line_index, all_lines)
    return total


lines = []
with open("input.txt", "r") as input:
    for line in input:
        lines.append(line.strip())
grand_total = 0
for i, line in enumerate(lines):
    grand_total += check_mas(line, i, lines)
print(f"The total is {grand_total}")  # 2000 
