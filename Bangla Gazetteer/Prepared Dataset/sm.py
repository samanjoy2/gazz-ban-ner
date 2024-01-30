import os

def count_rows(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        row_count = sum(1 for _ in file)
    return row_count

def count_rows_per_file(directory):
    rows_per_file = {}
    total_rows = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            row_count = count_rows(file_path)
            rows_per_file[filename] = row_count
            total_rows += row_count
    return rows_per_file, total_rows

# Provide the directory path where your text files are located
directory_path = r"C:\Users\User\Desktop\gazz_main"

rows_per_file, total_rows = count_rows_per_file(directory_path)
for filename, row_count in rows_per_file.items():
    print(f"{filename}: {row_count} rows")

print(f"Total rows: {total_rows}")
