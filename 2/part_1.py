print("Advent of Code: Day 2 Part 1")

def contains_n_matching_chars(box_id, n):
    letters_set = set(box_id)
    for letter in letters_set:
        if box_id.count(letter) == n:
            return True
    return False

with open("input") as f:
    box_id_lines = f.readlines()

box_ids = [box_id_line.strip() for box_id_line in box_id_lines] 

two_matching_chars = 0
three_matching_chars = 0
for box_id in box_ids:
    if contains_n_matching_chars(box_id, 2):
        two_matching_chars += 1
    if contains_n_matching_chars(box_id, 3):
        three_matching_chars += 1    

checksum = two_matching_chars * three_matching_chars
print("Answer:", checksum)