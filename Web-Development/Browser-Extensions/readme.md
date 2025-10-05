# Browser Extensions

This folder contains browser extension development projects organized by complexity level. Extensions work across Chromium-based browsers (Chrome, Edge, Brave) and can be adapted for Firefox. Each level introduces new concepts and APIs to build progressively complex applications.

## Project Levels

### Level 1: Simple Utilities
Basic extensions focusing on core concepts including manifest configuration, popup interfaces, and simple DOM manipulation. Projects include word counters, color pickers, and text formatters.

**Skills:** Manifest V3 structure, popup HTML/CSS/JS, basic event handling

### Level 2: Storage Integration
Extensions that persist data using Chrome Storage API. Projects include bookmark managers, note-taking apps, and settings managers that maintain state across browser sessions.

**Skills:** Chrome Storage API, data persistence, state management, forms

### Level 3: Content Manipulation
Advanced extensions that interact with web pages using content scripts. Projects include theme changers, ad blockers, page modifiers, and productivity tools that enhance browsing experience.

**Skills:** Content scripts, DOM manipulation, message passing, CSS injection

### Level 4: API Integration
Professional-grade extensions integrating external APIs and services. Projects include GitHub statistics viewers, weather dashboards, and productivity tools with real-time data.

**Skills:** API requests, authentication, background service workers, async operations

## Prerequisites

- Basic knowledge of HTML, CSS, and JavaScript
- A code editor (VS Code recommended)
- Chrome, Edge, or Brave browser
- Understanding of browser DevTools

## Getting Started

1. Choose a level appropriate for your skill set
2. Read the level-specific readme for detailed requirements
3. Create your extension following the project specifications
4. Test locally using Developer Mode
5. Submit your implementation with proper documentation

## Resources

- [Chrome Extension Documentation](https://developer.chrome.com/docs/extensions/)
- [Manifest V3 Migration Guide](https://developer.chrome.com/docs/extensions/mv3/intro/)
- [Chrome Extension Samples](https://github.com/GoogleChrome/chrome-extensions-samples)
- [MDN Web Extensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions)

## Testing Your Extension

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" in the top right
3. Click "Load unpacked" and select your extension folder
4. Your extension icon will appear in the toolbar
5. Test functionality and check console for errors
6. Reload extension after making changes

## Submission Format

Create a folder named `ExtensionName_YourGitHubUsername` containing:

- `manifest.json` - Extension configuration
- `popup.html` - Popup interface (if applicable)
- `popup.js` - Popup logic
- `styles.css` - Styling
- `content.js` - Content script (if applicable)
- `background.js` - Background service worker (if applicable)
- `README.md` - Setup instructions and features
- `screenshots/` - Visual demonstrations

Include clear installation steps and describe all features in your README.
