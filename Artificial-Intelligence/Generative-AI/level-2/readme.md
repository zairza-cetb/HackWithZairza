# Level 2: Simple API Wrappers

Build basic wrappers around ChatGPT or Claude APIs for specific tasks. Create command-line interfaces or simple scripts that demonstrate API integration fundamentals.

## Project Options

### Option 1: Text Summarizer
Command-line tool that summarizes text input using AI.

**Features:**
- Accept text from file or stdin
- Customizable summary length
- Multiple summary styles (brief, detailed, bullet points)
- Output to console or file

### Option 2: Code Reviewer
Automated code review tool using AI analysis.

**Features:**
- Analyze code files for issues
- Generate improvement suggestions
- Check code quality and style
- Output review report

### Option 3: Q&A Assistant
Interactive question-answering tool with context.

**Features:**
- Multi-turn conversations
- Context retention
- Save conversation history
- Clear and restart options

## Technical Requirements

**Python Implementation:**
```
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat_completion(prompt, model="gpt-3.5-turbo"):
response = client.chat.completions.create(
model=model,
messages=[{"role": "user", "content": prompt}]
)
return response.choices.message.content
```

**Node.js Implementation:**
```
import OpenAI from 'openai';

const openai = new OpenAI({
apiKey: process.env.OPENAI_API_KEY
});

async function chatCompletion(prompt) {
const completion = await openai.chat.completions.create({
model: "gpt-3.5-turbo",
messages: [{ role: "user", content: prompt }]
});
return completion.choices.message.content;
}
```


## Submission Requirements

Create folder `ProjectName_YourGitHubUsername` containing:

1. **main.py** or **index.js** - Main application
2. **.env.example** - API key template:
```
OPENAI_API_KEY=your_api_key_here
```
3. **requirements.txt** or **package.json** - Dependencies
4. **README.md** - Setup and usage instructions

## Setup Instructions Template
```
# Project Name
Brief description of what the tool does.

## Setup
1. Clone the repository
2. Install dependencies:
    - Python: pip install -r requirements.txt
    - Node.js: npm install
3. Create .env file with your API key
4. Run: python main.py or node index.js

## Usage
Examples of how to use the tool.
```


## Resources

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [OpenAI Node.js SDK](https://github.com/openai/openai-node)
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
