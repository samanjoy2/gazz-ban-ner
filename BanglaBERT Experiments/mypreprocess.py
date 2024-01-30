import json

with open('dev.txt', 'r', encoding='utf-8') as f_in:
    lines = f_in.readlines()

with open('output.jsonl', 'w', encoding='utf-8') as f_out:
    tokens = []
    tags = []
    for line in lines:
        line = line.strip()
        if line:
            fields = line.split()
            if len(fields) != 2:
                print(f"Warning: Skipping line with invalid format: {line}")
                continue
            token, tag = fields
            tokens.append(token)
            tags.append(tag)
        else:
            if tokens and tags:
                json_data = {'tokens': tokens, 'tags': tags}
                json.dump(json_data, f_out, ensure_ascii=False)
                f_out.write('\n')
                tokens = []
                tags = []
    if tokens and tags:
        json_data = {'tokens': tokens, 'tags': tags}
        json.dump(json_data, f_out, ensure_ascii=False)
        f_out.write('\n')
