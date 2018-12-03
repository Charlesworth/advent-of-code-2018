print("Advent of Code: Day 1 Part 1")

with open("input") as f:
    frequency_lines = f.readlines()

result = 0
for frequency_str in frequency_lines:
    result += int(frequency_str.strip())

print("Answer:", result)