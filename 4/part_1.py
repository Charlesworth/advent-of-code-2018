from enum import Enum
from datetime import datetime
from collections import Counter

print("Advent of Code: Day 4 Part 1")

class guard_action(Enum):
    BEGIN_SHIFT = 0
    FALL_ASLEEP = 1
    WAKE_UP = 2

def get_time(guard_time_line):
    unparsed_time, _ = guard_time_line.split(']')
    return datetime.strptime(unparsed_time, '[%Y-%m-%d %H:%M')    

def get_guard_number(guard_time_line):
    return guard_time_line.split("#")[1].split(" ")[0]

def get_guard_action(guard_time_line):
    if guard_time_line.count("falls asleep") > 0:
        return guard_action.FALL_ASLEEP
    if guard_time_line.count("wakes up") > 0:
        return guard_action.WAKE_UP
    return guard_action.BEGIN_SHIFT

def main():
    with open("input") as f:
        guard_time_lines = f.readlines()

    # sort into chronilogical order
    guard_time_lines.sort(key=lambda l: get_time(l))

    guards_total_sleep = dict()
    minute_counter = Counter()
    # for each gaurd create a 0 - 60 dict or list[0 -> 60]
    # go through each line, parse it and add it to the right ^
    # go through the finished ^ and pick the right one
    for guard_time_line in guard_time_lines:
        # guard_total_sleep
        action = get_guard_action(guard_time_line)
        if action == guard_action.BEGIN_SHIFT:
            current_guard = get_guard_number(guard_time_line)
            if current_guard not in guards_total_sleep:
                guards_total_sleep[current_guard] = 0

        # TODO may need to remove the second
        if action == guard_action.FALL_ASLEEP:
            start_sleep_time = get_time(guard_time_line).minute

        if action == guard_action.WAKE_UP:
            end_sleep_time = get_time(guard_time_line).minute
            guards_total_sleep[current_guard] += end_sleep_time - start_sleep_time


        # print(guard_time_line)
        # print(get_time(guard_time_line))
        # action = get_guard_action(guard_time_line)
        # print(action.name)
        # if action == guard_action.BEGIN_SHIFT:
            # print(get_guard_number(guard_time_line))

    # for guard_time_line in guard_time_lines:
        # print(parse(guard_time_line))

    most_asleep_guard = max(guards_total_sleep, key=guards_total_sleep.get)
    print(most_asleep_guard)

    return 0

if __name__ == "__main__":
    main()
