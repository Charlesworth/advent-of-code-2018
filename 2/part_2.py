print("Advent of Code: Day 2 Part 2")

def matches_apart_from_one(a, b):
    matches = 0
    end_range = len(a)
    for n in range(0, end_range):
        if a[n] == b[n]:
            matches += 1
    if matches == end_range - 1:
        return True
    return False


def main():
    with open("input") as f:
        box_id_lines = f.readlines()

    box_ids = [box_id_line.strip() for box_id_line in box_id_lines] 

    for box_id_a in box_ids:
        for box_id_b in box_ids:
            if matches_apart_from_one(box_id_a, box_id_b):
                print(box_id_a, box_id_b)
                return 0

if __name__ == "__main__":
    main()
