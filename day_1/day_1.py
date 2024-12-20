# Part 1
left = []
right = []
with open("input.txt", "r") as input:
    for line in input:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
left.sort()
right.sort()
sum = 0
for numbers in zip(left, right):
    sum += (abs(numbers[0] - numbers[1]))
print(f"The total difference of the lists are: {sum}") # 2166959

# Part 2
similarity_score_left = 0
for number in left:
    instances_right = right.count(number)
    similarity_score_left += (number * instances_right)
print(f"The total similarity score of the left list is: {similarity_score_left}") # 23741109
