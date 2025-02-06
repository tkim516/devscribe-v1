import os
import json

def parse_repo(folder):
    file_contents = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(('.py', '.ipynb', '.md', '.txt', '.json')):  # Add file types as needed
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        if file.endswith('.ipynb'):
                            # Process .ipynb files
                            notebook = json.load(f)
                            raw_code = []
                            for cell in notebook.get('cells', []):
                                if cell.get('cell_type') == 'code':
                                    raw_code.extend(cell.get('source', []))
                            file_contents[file_path] = '\n'.join(raw_code)
                        else:
                            # Process other files
                            file_contents[file_path] = f.read()
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return file_contents
