#!/usr/bin/env python3
import sys 
import json 
import os 

# Get the directory where this script is installed
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "magicDB.json")

def detect_file(filepath):
    with open(db_path, "r") as f:  # Changed to db_path
        sig = json.load(f)

    with open(filepath, "rb") as f:
        header = f.read(32)

    for filetype, magic in sig.items():
        if header.startswith(bytes.fromhex(magic)):
            return filetype
    return "Unknown"

def main():
    print("=" * 70)
    print("TRUE_FILE_FORMAT")
    print("=" * 70)
    path = input("enter the path to a file OR a directory: ").strip()
    print("=" * 70)

    if not os.path.exists(path):
        print("\nPath not found!")
        sys.exit(1)

    if os.path.isfile(path):
        res = detect_file(path)
        print("\nFile: " + path)
        print("\nTrue Format: " + res)

    elif os.path.isdir(path):
        print("\nScanning: " + path)
        
        other_dirs = []
        
        for item in os.listdir(path):
            fullpath = os.path.join(path, item)
            if os.path.isfile(fullpath):
                print("\n  " + item + " → " + detect_file(fullpath))
            else:
                other_dirs.append(item)
        
        if other_dirs:
            print("\nOther directories: " + ', '.join(other_dirs))
            print ("=" * 70)
    print("KEEP_IN_MIND: \nthis tool determines the true format of a file\nfrom most known and most commenly used formats,\nif it is Unknown that doesnt mean it is a hazard \nbut maybe not registered in the datebase(it's a .json)")

if __name__ == "__main__":
    main()
