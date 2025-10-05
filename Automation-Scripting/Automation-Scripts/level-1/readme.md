# Level 1: File Organization Scripts

Create Python scripts that automatically organize files based on extensions, creation dates, or custom rules. Focus on file system operations and directory management.

## Project Options

### Option 1: File Extension Organizer
Organize files into folders based on file extensions.

**Features:**
- Scan directory for files
- Create folders by extension type
- Move files to appropriate folders
- Handle duplicate filenames
- Support custom extension mappings

**Example Usage:**
```
python organize_files.py --path ~/Downloads
```


### Option 2: Date-Based File Organizer
Organize files by creation or modification date into year/month folders.

**Features:**
- Group files by date created or modified
- Create year/month/day folder structure
- Preserve original filenames
- Skip already organized files
- Generate organization report

### Option 3: Duplicate File Finder
Find and handle duplicate files based on content hash.

**Features:**
- Scan directory recursively
- Calculate file hashes (MD5 or SHA256)
- Identify duplicate files
- Option to delete or move duplicates
- Generate duplicate report

## Implementation Example
```
import os
import shutil
def organize_by_extension(directory):
"""Organize files by extension into folders"""

# Extension to folder mapping
extensions = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.doc', '.docx', '.txt'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'audio': ['.mp3', '.wav', '.flac']
}

for file in path.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        
        # Find appropriate folder
        folder = 'others'
        for folder_name, exts in extensions.items():
            if ext in exts:
                folder = folder_name
                break
        
        # Create folder if not exists
        dest_folder = path / folder
        dest_folder.mkdir(exist_ok=True)
        
        # Move file
        try:
            shutil.move(str(file), str(dest_folder / file.name))
            print(f"Moved {file.name} to {folder}/")
        except Exception as e:
            print(f"Error moving {file.name}: {e}")

if name == "main":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='Directory to organize')
    args = parser.parse_args()

organize_by_extension(args.path)
```


## Technical Requirements

1. **Command-line arguments** for directory path
2. **Error handling** for file operations
3. **Logging** of operations performed
4. **Dry-run mode** to preview changes
5. **Undo functionality** (optional)

## Submission Requirements

File: `ScriptName_YourGitHubUsername.py` containing:

1. Main script with clear functions
2. Command-line argument parsing
3. Error handling
4. Documentation strings
5. Usage instructions in comments

## Resources

- [Python pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python shutil](https://docs.python.org/3/library/shutil.html)
- [Python argparse](https://docs.python.org/3/library/argparse.html)
