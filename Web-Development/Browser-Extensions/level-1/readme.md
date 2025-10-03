# Level 1: Simple Utilities

Build basic browser extensions that demonstrate core concepts including manifest configuration, popup interfaces, and simple JavaScript functionality. These projects focus on understanding extension structure without complex APIs.

## Project Options

### Option 1: Word Counter Extension
Create an extension that counts words, characters, and sentences in selected text on any webpage.

**Features:**
- Right-click context menu to analyze selected text
- Popup displaying word count, character count, and sentence count
- Clean, minimal interface

**Technical Requirements:**
- Manifest V3 configuration
- Context menu API
- Basic DOM manipulation
- Popup HTML interface

### Option 2: Color Picker Extension
Build a color picker that extracts colors from any webpage element.

**Features:**
- Click extension icon to activate picker mode
- Hover over elements to preview color
- Click to copy hex/rgb values to clipboard
- Display recently picked colors

**Technical Requirements:**
- Content script for page interaction
- Color detection from computed styles
- Clipboard API
- Local storage for color history

### Option 3: Quick Notes Extension
Simple note-taking extension accessible from the browser toolbar.

**Features:**
- Popup interface with textarea
- Auto-save functionality
- Character counter
- Clear notes option

**Technical Requirements:**
- Popup HTML/CSS/JS
- LocalStorage for persistence
- Basic form handling

## Submission Requirements

Create a folder `ProjectName_YourGitHubUsername` containing:

1. **manifest.json** - Basic configuration:
```
{
"manifest_version": 3,
"name": "Your Extension Name",
"version": "1.0",
"description": "Brief description",
"action": {
"default_popup": "popup.html",
"default_icon": "icon.png"
},
"permissions": ["storage", "activeTab"]
}
```

2. **popup.html** - User interface
3. **popup.js** - Extension logic
4. **styles.css** - Styling
5. **README.md** - Installation and usage instructions
6. **icon.png** - Extension icon (128x128px minimum)

## Learning Resources

- [Chrome Extension Getting Started](https://developer.chrome.com/docs/extensions/mv3/getstarted/)
- [Manifest File Format](https://developer.chrome.com/docs/extensions/mv3/manifest/)
- [Chrome Extension Samples - Basic](https://github.com/GoogleChrome/chrome-extensions-samples)

## Evaluation Criteria

- Code quality and organization
- Working functionality
- Clear documentation
- User interface design
- Proper manifest configuration

