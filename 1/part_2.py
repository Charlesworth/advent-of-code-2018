print("Advent of Code: Day 1 Part 2")


with open("input") as f:
    frequency_lines = f.readlines()

frequencies = [int(frequency_line.strip()) for frequency_line in frequency_lines] 

results_set = {0}
result_found = False
result = 0

while not result_found:
    for frequency in frequencies:
        result += frequency
        if result in results_set:
            result_found = True
            break
        else:
            results_set.add(result)

print("Answer:", result)
