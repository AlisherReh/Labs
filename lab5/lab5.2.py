# Define empty lists for each subject
math_group = []
science_group = []
history_group = []

# Prompt students for their names and subjects
while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name == "q":
        break
    subject = input("Enter the subject (math, science, or history): ")
    
    # Add student to the appropriate group
    if subject == "math":
        math_group.append(name)
    elif subject == "science":
        science_group.append(name)
    elif subject == "history":
        history_group.append(name)
    else:
        print("Wrong subject.")

# Sort the groups alphabetically by student name
math_group.sort()
science_group.sort()
history_group.sort()

# Display the sorted groups on the screen
print("Math group:")
for name in math_group:
    print(name)

print("Science group:")
for name in science_group:
    print(name)

print("History group:")
for name in history_group:
    print(name)