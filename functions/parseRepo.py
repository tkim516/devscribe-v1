import os

def parse_repo(folder, file_types: list):
    file_contents = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file.endswith(ft) for ft in file_types):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_contents[file_path] = f.read()
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return file_contents


