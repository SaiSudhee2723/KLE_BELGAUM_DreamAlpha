import os

def replace_in_file(file_path, old_text, new_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(old_text, new_text)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    root_dir = r"c:\Users\saisu\Downloads\DreamAlpha_For\DreamAlpha_For_Amd-main"
    replacements = [
        ("Asteria Hackathon", "Asteria Hackathon"),
        ("Asteria Hackathon", "Asteria Hackathon"),
        ("Asteria Hackathon", "Asteria Hackathon"),
        ("Asteria Hackathon", "ASTERIA HACKATHON"),
    ]
    
    for subdir, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            file_path = os.path.join(subdir, file)
            for old, new in replacements:
                replace_in_file(file_path, old, new)

if __name__ == "__main__":
    main()

