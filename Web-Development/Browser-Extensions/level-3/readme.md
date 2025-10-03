# Level 3: Content Manipulation

Build extensions that interact with and modify web page content using content scripts. These projects involve DOM manipulation, message passing between scripts, and dynamic page modifications.

## Project Options

### Option 1: Dark Mode Extension
Universal dark mode for any website with customization options.

**Features:**
- Toggle dark mode on any website
- Automatic color inversion
- Whitelist/blacklist websites
- Custom color schemes
- Respect user's prefers-color-scheme

**Technical Requirements:**
- Content scripts for CSS injection
- Dynamic style manipulation
- Message passing between popup and content script
- Domain-specific settings
- CSS filters and transformations

### Option 2: Ad Blocker Basics
Simple advertisement blocker focusing on common ad patterns.

**Features:**
- Block elements by class/id patterns
- Hide sponsored content
- Remove tracking scripts
- Custom blocking rules
- Counter showing blocked elements

**Technical Requirements:**
- Content scripts with MutationObserver
- Element removal/hiding
- Pattern matching
- Storage for custom rules
- Performance optimization

### Option 3: Productivity Focus Tool
Remove distracting elements from websites to improve focus.

**Features:**
- Hide comments sections
- Remove sidebar widgets
- Blur images (focus mode)
- Customizable hiding rules per site
- Quick toggle on/off

**Technical Requirements:**
- Advanced DOM manipulation
- CSS injection
- Site-specific rules
- Observer patterns
- Message communication

## Submission Requirements

Create a folder `ProjectName_YourGitHubUsername` containing:

1. **manifest.json** with content scripts configuration
2. **content.js** - Main content script
3. **background.js** - Background service worker
4. **popup.html/js** - Control interface
5. **styles.css** - Injected styles
6. **utils.js** - Helper functions
7. **README.md** - Technical documentation

## Content Script Example
```
// manifest.json
{
"content_scripts": [{
"matches": ["<all_urls>"],
"js": ["content.js"],
"css": ["styles.css"]
}]
}

// content.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
if (request.action === "toggleDarkMode") {
document.body.classList.toggle('dark-mode');
sendResponse({success: true});
}
});
```


## Learning Resources

- [Content Scripts Documentation](https://developer.chrome.com/docs/extensions/mv3/content_scripts/)
- [Message Passing Guide](https://developer.chrome.com/docs/extensions/mv3/messaging/)
- [DOM Manipulation Best Practices](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [MutationObserver API](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver)

## Evaluation Criteria

- Content script implementation
- DOM manipulation efficiency
- Message passing architecture
- Performance considerations
- User control and customization
- Cross-site compatibility

