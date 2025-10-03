# Level 2: Storage Integration

Develop browser extensions that persist data across sessions using Chrome Storage API. These projects introduce state management and data synchronization concepts essential for practical applications.

## Project Options

### Option 1: Bookmark Manager
Advanced bookmark management system with categories and tags.

**Features:**
- Save current page with custom tags
- Organize bookmarks into folders
- Search and filter functionality
- Import/export bookmarks as JSON
- Quick access popup

**Technical Requirements:**
- Chrome Storage API (sync or local)
- Bookmark data structure design
- Search/filter algorithms
- JSON import/export

### Option 2: Task Manager Extension
Lightweight todo list accessible from browser toolbar.

**Features:**
- Add, edit, delete tasks
- Mark tasks as complete
- Categorize by priority
- Due date tracking
- Persistent storage across sessions

**Technical Requirements:**
- Chrome Storage API
- Task data model
- CRUD operations
- Date handling
- State management

### Option 3: Settings Manager
Create an extension that remembers user preferences for websites.

**Features:**
- Store site-specific settings
- Dark mode toggle per website
- Font size adjustments
- Custom CSS injection
- Settings sync across devices

**Technical Requirements:**
- Chrome Storage Sync API
- Content scripts for CSS injection
- Domain-specific settings
- Options page

## Submission Requirements

Create a folder `ProjectName_YourGitHubUsername` containing:

1. **manifest.json** with storage permissions
2. **popup.html** and **popup.js** - Main interface
3. **storage.js** - Storage helper functions
4. **background.js** - Background operations (if needed)
5. **options.html** - Settings page (optional)
6. **styles.css** - Styling
7. **README.md** - Documentation with data structure explanation

## Storage API Example
```
// Save data
chrome.storage.local.set({ key: 'value' }, function() {
console.log('Data saved');
});

// Retrieve data
chrome.storage.local.get(['key'], function(result) {
console.log('Value is ' + result.key);
});

// Remove data
chrome.storage.local.remove(['key'], function() {
console.log('Data removed');
});
```

## Learning Resources

- [Chrome Storage API Documentation](https://developer.chrome.com/docs/extensions/reference/storage/)
- [Data Storage Best Practices](https://developer.chrome.com/docs/extensions/mv3/storage/)
- [Storage API Examples](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/api-samples/storage)

## Evaluation Criteria

- Proper use of Storage API
- Data structure design
- Error handling
- State synchronization
- User experience
- Code documentation
