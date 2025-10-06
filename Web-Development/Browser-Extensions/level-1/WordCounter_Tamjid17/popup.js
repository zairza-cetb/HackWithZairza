
  // Select necessary DOM elements for extension use
document.addEventListener("DOMContentLoaded", () => {
  const textInput = document.getElementById("textInput");
  const analyzeBtn = document.getElementById("analyzeBtn");
  const clearBtn = document.getElementById("clearBtn");

  const wordCountEl = document.getElementById("wordCount");
  const charCountEl = document.getElementById("charCount");
  const charCountNoSpaceEl = document.getElementById("charCountNoSpace");
  const sentenceCountEl = document.getElementById("sentenceCount");

  // Read any selection stored by background and auto-analyze
  chrome.storage.local.get(["lastSelection"], (result) => {
    if (result.lastSelection) {
      textInput.value = result.lastSelection;
      chrome.storage.local.remove("lastSelection");
      analyzeAndUpdate(result.lastSelection);
    }
  });

  analyzeBtn.addEventListener("click", () => {
    analyzeAndUpdate(textInput.value);
  });

  clearBtn.addEventListener("click", () => {
    textInput.value = "";
    updateUI(0, 0, 0, 0);
  });

  function analyzeAndUpdate(text) {
    const trimmed = text ?? "";
    const words = countWords(trimmed);
    const charsWithSpaces = trimmed.length;
    const charsNoSpaces = trimmed.replace(/\s+/g, "").length;
    const sentences = countSentences(trimmed);

    updateUI(words, charsWithSpaces, charsNoSpaces, sentences);
  }

  function updateUI(words, charsWithSpaces, charsNoSpaces, sentences) {
    wordCountEl.textContent = words;
    charCountEl.textContent = charsWithSpaces;
    charCountNoSpaceEl.textContent = charsNoSpaces;
    sentenceCountEl.textContent = sentences;
  }

  // Word counting: Unicode-aware, counts words like "don't" or "user-name"
  function countWords(text) {
    if (!text) return 0;
    const cleaned = text.trim();
    if (cleaned.length === 0) return 0;
    const matches = cleaned.match(/[\p{L}\p{N}]+(?:['-][\p{L}\p{N}]+)*/gu);
    return matches ? matches.length : 0;
  }

  // Sentence counting: basic heuristic (splits on . ? ! groups)
  function countSentences(text) {
    if (!text) return 0;
    const trimmed = text.trim();
    if (trimmed.length === 0) return 0;

    const matched = trimmed.match(/[^.?!\n]+[.?!]+/g) || [];

    const leftover = trimmed.replace(/[^.?!\n]+[.?!]+/g, "").trim();
    return matched.length + (leftover.length > 0 ? 1 : 0);
  }
});
