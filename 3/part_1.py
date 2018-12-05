import numpy

print("Advent of Code: Day 3 Part 1")

def extract(claim_line):
    _, _, location, size = claim_line.split(' ')
    x_start, y_start = map(int, location[:-1].split(','))
    width, height = map(int, size.split('x'))
    return x_start, y_start, width, height

def main():
    material = numpy.zeros((1000, 1000), dtype=int)

    with open("input") as f:
        fabric_claim_lines = f.readlines()

    for fabric_claim_line in fabric_claim_lines:
        x_start, y_start, width, height = extract(fabric_claim_line)
        material[x_start:x_start+width, y_start:y_start+height] += 1

    overclaimed = 0
    for location in numpy.nditer(material):
        if location > 1:
            overclaimed += 1

    print(overclaimed)
    return 0

if __name__ == "__main__":
    main()
