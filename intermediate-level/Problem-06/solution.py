# Flatten a Nested JSON

def flatten_json(nested_json, parent_key='', sep='.'):
    items = []
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == "__main__":
    nested_json = {"a": {"b": 1}}
    print(f"Flattened JSON: {flatten_json(nested_json)}")