# Level 4: Multi-Modal AI Applications

Build advanced applications that process both text and images using AI models. Implement complex workflows combining multiple APIs and processing pipelines.

## Project Options

### Option 1: Image Description & Analysis Tool
Analyze images and generate detailed descriptions with contextual information.

**Features:**
- Upload and analyze images
- Generate descriptions at various detail levels
- Extract text from images (OCR)
- Answer questions about image content
- Batch processing for multiple images
- Export results to markdown or JSON

### Option 2: Document Intelligence System
Process documents with text and images for comprehensive analysis.

**Features:**
- Extract and analyze document content
- Summarize multi-page documents
- Identify key information and entities
- Generate structured data from documents
- Handle PDFs, images, and text files

### Option 3: Visual Code Assistant
AI assistant that understands code screenshots and diagrams.

**Features:**
- Convert code screenshots to text
- Explain code from images
- Analyze architecture diagrams
- Generate documentation from visual content
- Support flowcharts and UML diagrams

## Technical Requirements

**Image Processing:**
```
from openai import OpenAI
import base64

def encode_image(image_path):
with open(image_path, "rb") as image_file:
return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image(image_path, prompt):
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    }],
    max_tokens=500
)
return response.choices.message.content

```


**Multi-Modal Workflow:**
```
def process_document(doc_path):
    # Extract text
    text = extract_text_from_pdf(doc_path)

    # Extract images
    images = extract_images_from_pdf(doc_path)

    # Analyze each component
    text_analysis = analyze_text(text)
    image_analyses = [analyze_image(img) for img in images]

    # Combine results
    return combine_analyses(text_analysis, image_analyses)
```


## Submission Requirements

Create folder `ProjectName_YourGitHubUsername` containing:

1. **main.py** - Application entry point
2. **processors/** - Text and image processing modules
3. **models/** - Data models and schemas
4. **utils/** - Helper functions
5. **examples/** - Sample inputs and outputs
6. **.env.example** - API keys template
7. **requirements.txt** - All dependencies
8. **README.md** - Complete documentation

## Dependencies Example
```
openai>=1.0.0
anthropic>=0.8.0
pillow>=10.0.0
pypdf2>=3.0.0
python-dotenv>=1.0.0
requests>=2.31.0
```


## Advanced Features

- Asynchronous processing for multiple files
- Progress bars for batch operations
- Caching mechanisms to reduce API calls
- Error recovery and retry logic
- Output formatting options (JSON, Markdown, HTML)
- Configuration management

## Resources

- [OpenAI Vision API](https://platform.openai.com/docs/guides/vision)
- [Claude Vision Capabilities](https://docs.anthropic.com/claude/docs/vision)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [PyPDF2 Guide](https://pypdf2.readthedocs.io/)

