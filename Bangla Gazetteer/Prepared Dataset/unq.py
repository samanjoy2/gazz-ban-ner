lines = set()

# Read the input file
with open('PROD.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Remove leading/trailing whitespaces and add the line to the set
        lines.add(line.strip())

# Write the unique lines to a new file
with open('PROD UNQ.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line + '\n')