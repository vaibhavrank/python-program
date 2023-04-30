# List containing names of boys and girls
name_list = ['vaibhav', ('yatri', 'urvisha'), 'maulik', ('nehal', 'happy')]

# Initialize counters for boys and girls
boys_count = 0
girls_count = 0

# Iterate through the list
for name in name_list:
    # Check if the name is a tuple (indicating a boy's name)
    if isinstance(name, tuple):
        # Increment boys_count by the number of names in the tuple
        boys_count += len(name)
    else:
        # If not a tuple, assume it's a girl's name and increment girls_count
        girls_count += 1

# Print the counts of boys and girls
print("Number of boys:", boys_count)
print("Number of girls:", girls_count)
