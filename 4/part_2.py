from enum import Enum
from datetime import datetime
from collections import Counter

print("Advent of Code: Day 4 Part 2")

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

    guards_sleep_counter = dict()

    for guard_time_line in guard_time_lines:
        action = get_guard_action(guard_time_line)

        if action == guard_action.BEGIN_SHIFT:
            current_guard = get_guard_number(guard_time_line)
            if current_guard not in guards_sleep_counter:
                guards_sleep_counter[current_guard] = Counter()

        elif action == guard_action.FALL_ASLEEP:
            start_sleep_time = get_time(guard_time_line).minute

        elif action == guard_action.WAKE_UP:
            end_sleep_time = get_time(guard_time_line).minute
            count = guards_sleep_counter[current_guard]
            for minute in range(start_sleep_time, end_sleep_time):
                count[minute] += 1
            guards_sleep_counter[current_guard] = count

    max_minute_sleep = 0
    for guard_number, counter in guards_sleep_counter.items():
        arr = counter.most_common(1)
        if len(arr) == 0:
            continue
        guard_most_asleep_minute, time_asleep = arr[0]
        if time_asleep > max_minute_sleep:
            max_minute_sleep = time_asleep
            sleepy_guard = guard_number
            sleepy_minute = guard_most_asleep_minute

    print(int(sleepy_guard) * int(sleepy_minute))

    return 0

if __name__ == "__main__":
    main()
