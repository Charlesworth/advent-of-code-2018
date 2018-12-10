print("Advent of Code: Day 5 Part 1")

def opposite(a, b):
    return (a != b) and (b.lower() == a.lower())

def reaction(polymer_line):
    for i in range(len(polymer_line)-1):
        if opposite(polymer_line[i], polymer_line[i+1]):
            polymer_line = polymer_line[:i] + polymer_line[i+2:]
            return (polymer_line, False)
    return (polymer_line, True)
        
def main():
    with open("input") as f:
        polymer_line = f.readlines()[0].strip()

    reaction_complete = False
    while not reaction_complete:
        if len(polymer_line) < 2:
            break
        polymer_line, reaction_complete = reaction(polymer_line)

    print(len(polymer_line))
    return 0

if __name__ == "__main__":
    main()
