def classify(value):
    if value < 248:
        return "Below range"
    elif 248 <= value <= 252:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    if count == 0:
        return 0.0
    return total / count

num_jars = int(input("Enter the number of jars: "))

total_volume = 0
below_count = 0
in_range_count = 0
above_count = 0

for _ in range(num_jars):
    volume = int(input("Enter the jar volume: "))
    total_volume += volume
    
    category = classify(volume)
    print(category)
    
    if category == "Below range":
        below_count += 1
    elif category == "In range":
        in_range_count += 1
    elif category == "Above range":
        above_count += 1
        
avg_volume = calculate_average(total_volume, num_jars)

print(f"Total volume: {total_volume} ml")
print(f"Average volume: {avg_volume:.1f} ml")
print(f"Below range: {below_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_count}")
