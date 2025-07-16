import os
import re
import json

def load_patterns(file='patterns.json'):
    with open(file, 'r') as f:
        return json.load(f)  # Returns a list of pattern dictionaries

def scan_file(file_path, patterns):
    matches = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_number, line in enumerate(file, start=1):
                for pattern in patterns:
                    pattern_name = pattern['name']
                    regex = pattern['regex']
                    if re.search(regex, line):
                        matches.append({
                            'file': file_path,
                            'line_number': line_number,
                            'pattern': pattern_name,
                            'match': line.strip()
                        })
    except Exception as e:
        print(f"❌ Error reading file {file_path}: {e}")
    return matches

def scan_folder(folder_path, patterns):
    all_matches = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            file_matches = scan_file(full_path, patterns)
            all_matches.extend(file_matches)
    return all_matches
