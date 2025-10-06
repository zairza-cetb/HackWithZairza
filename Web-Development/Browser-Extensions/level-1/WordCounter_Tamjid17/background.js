
// Create / reset context menu when extension is installed
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.removeAll(() => {
    chrome.contextMenus.create({
      id: "analyzeSelection",
      title: "Analyze selection — Word Counter",
      contexts: ["selection"],
    });
  });
});

// Handle context menu clicks
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "analyzeSelection" && info.selectionText) {
    chrome.storage.local.set({ lastSelection: info.selectionText }, () => {
      chrome.action.openPopup(() => {
        if (chrome.runtime.lastError) {
          chrome.tabs.create({ url: chrome.runtime.getURL("popup.html") });
        }
      });
    });
  }
});
