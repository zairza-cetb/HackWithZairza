# Level 2: Data Format Converters

Build scripts to convert between different data formats including CSV, JSON, XML, and Excel. Handle data transformation, validation, and format-specific requirements.

## Project Options

### Option 1: CSV to JSON Converter
Convert CSV files to JSON with various structure options.

**Features:**
- Read CSV files with pandas
- Convert to JSON array or object
- Handle nested structures
- Custom field mappings
- Pretty print option

### Option 2: Multi-Format Data Converter
Support conversion between CSV, JSON, XML, and Excel formats.

**Features:**
- Detect input format automatically
- Convert to specified output format
- Preserve data types
- Handle large files efficiently
- Batch conversion support

### Option 3: Excel Report Generator
Convert data from CSV/JSON into formatted Excel reports.

**Features:**
- Create multiple sheets
- Apply formatting and styles
- Generate charts and summaries
- Add headers and footers
- Custom column widths

## Implementation Example
```
import pandas as pd
import json
import argparse

def csv_to_json(csv_file, json_file, orient='records'):
"""Convert CSV to JSON format."""
try:
# Read CSV
df = pd.read_csv(csv_file)

    # Convert to JSON
    json_data = df.to_json(orient=orient, indent=2)
    
    # Write to file
    with open(json_file, 'w') as f:
        f.write(json_data)
    
    print(f"Converted {csv_file} to {json_file}")
    print(f"Records: {len(df)}")
    
except Exception as e:
    print(f"Error: {e}")

def json_to_csv(json_file, csv_file):
"""Convert JSON to CSV format."""
try:
# Read JSON
with open(json_file, 'r') as f:
data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Write to CSV
    df.to_csv(csv_file, index=False)
    
    print(f"Converted {json_file} to {csv_file}")
    print(f"Records: {len(df)}")
    
except Exception as e:
    print(f"Error: {e}")

if name == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--format', choices=['csv', 'json'], required=True)
    args = parser.parse_args()

    if args.format == 'json':
        csv_to_json(args.input, args.output)
    else:
        json_to_csv(args.input, args.output)
```


## Technical Requirements

1. **Multiple format support**
2. **Data validation** before conversion
3. **Handle encoding issues** (UTF-8, etc.)
4. **Large file streaming** for efficiency
5. **Progress indicators** for large files

## Dependencies
```
pandas>=1.5.0
openpyxl>=3.0.0
lxml>=4.9.0
```


## Submission Requirements

Folder: `Converter_YourGitHubUsername/` containing:

1. `main.py` - Conversion script
2. `requirements.txt` - Dependencies
3. `README.md` - Usage guide
4. `sample_data/` - Example input files

## Resources

- [Pandas I/O Tools](https://pandas.pydata.org/docs/user_guide/io.html)
- [Python JSON Module](https://docs.python.org/3/library/json.html)
- [openpyxl Documentation](https://openpyxl.readthedocs.io/)

