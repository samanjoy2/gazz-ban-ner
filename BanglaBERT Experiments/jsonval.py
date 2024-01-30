import json

w = open("good_dev.jsonl", "w", encoding='utf-8')
count = 0

with open("processed_dev2022.jsonl", "r", encoding = 'utf-8') as f:
    for i, line in enumerate(f):
        try:
            json_data = json.loads(line)
            # print(f"Valid JSON on line {i+1}")
            w.write(line)
            count += 1
        except json.JSONDecodeError as e:
            print(f"Invalid JSON on line {i+1}: {e}")

    print(count)
