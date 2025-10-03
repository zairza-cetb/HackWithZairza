# Level 3: AI-Powered CLI Tools

Build production-ready command-line tools using AI for developer workflows. Focus on practical applications with proper argument parsing, error handling, and user experience.

## Project Options

### Option 1: Commit Message Generator
Generate conventional commit messages from staged changes.

**Features:**
- Analyze git diff automatically
- Generate commit message following conventions
- Support multiple commit types (feat, fix, docs, etc.)
- Interactive mode for review and editing
- Configuration file for preferences

**Usage:**
```
ai-commit

or

ai-commit --type feat --scope api
```


### Option 2: Code Explainer
Explain code functionality in natural language.

**Features:**
- Analyze code files or snippets
- Generate explanations at different detail levels
- Support multiple programming languages
- Output in markdown format
- Explain specific functions or entire files

**Usage:**
```
code-explain myfile.py
code-explain myfile.py --function calculate_total --detail high
```


### Option 3: Documentation Generator
Automatically generate documentation from code.

**Features:**
- Parse code and extract functions/classes
- Generate docstrings or JSDoc comments
- Create README sections
- Support multiple output formats
- Batch processing for multiple files

**Usage:**
```
doc-gen src/ --output docs/
```


## Implementation Structure
```
project-name/
├── src/
│ ├── init.py
│ ├── cli.py # Argument parsing
│ ├── ai_client.py # API wrapper
│ └── utils.py # Helper functions
├── tests/
│ └── test_cli.py
├── .env.example
├── requirements.txt
├── README.md
└── setup.py
```


## CLI Argument Parsing Example
```
import argparse
from ai_client import generate_response

def main():
parser = argparse.ArgumentParser(description='AI-powered tool')
parser.add_argument('input', help='Input file or text')
parser.add_argument('--model', default='gpt-3.5-turbo', help='AI model')
parser.add_argument('--output', help='Output file')
parser.add_argument('--verbose', action='store_true')

args = parser.parse_args()

with open(args.input, 'r') as f:
    content = f.read()

result = generate_response(content, model=args.model)

if args.output:
    with open(args.output, 'w') as f:
        f.write(result)
else:
    print(result)

if name == 'main':
    main()
```


## Submission Requirements

1. Working CLI tool with proper argument handling
2. Error handling for API failures and file operations
3. Configuration file support
4. Unit tests for core functionality
5. Comprehensive README with usage examples
6. Installation instructions (pip or npm)

## Resources

- [Python argparse](https://docs.python.org/3/library/argparse.html)
- [Click Framework](https://click.palletsprojects.com/)
- [Commander.js](https://github.com/tj/commander.js)
- [Conventional Commits](https://www.conventionalcommits.org/)
