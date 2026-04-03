#!/usr/bin/env python3
"""Convert MD files to JSON for multilingual support."""

import json
import os
import sys

def md_to_json(input_file, output_file):
    """Convert a markdown file to a JSON file."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"strategies": lines}, f, ensure_ascii=False, indent=2)
    
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_md_to_json.py <input_md_file> <output_json_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    md_to_json(input_file, output_file)
