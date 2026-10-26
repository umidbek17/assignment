def replace_value(values, index, new_value):
    values[index] = new_value
    return None


def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def summarize(values):
    return (min(values), max(values), sum(values))


num_days = int(input("Enter the number of days: "))

original = []
for _ in range(num_days):
    time = int(input("Enter reading time in minutes: "))
    original.append(time)

updated = original[:]

index_to_correct = int(input("Enter the index to correct: "))
new_time = int(input("Enter the new reading time: "))
replace_value(updated, index_to_correct, new_time)

target = int(input("Enter the reading time to search for: "))

first_index = find_first(updated, target)
match_count = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_list = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum reading time: {minimum} minutes")
print(f"Maximum reading time: {maximum} minutes")
print(f"Total reading time: {total} minutes")

if first_index == -1:
    print("First matching index: Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {match_count}")
