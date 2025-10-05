const noteInput = document.getElementById("noteInput");
const saveButton = document.getElementById("saveButton");
const clearButton = document.getElementById("clearButton");
const downloadButton = document.getElementById("downloadButton");
const notesList = document.getElementById("notesList");
const boldButton = document.getElementById("boldButton");
const italicButton = document.getElementById("italicButton");
const underlineButton = document.getElementById("underlineButton");

//UPDATE TOOLBAR BUTTON STYLES
function updateStyleButtons() {
  boldButton.classList.toggle("active", document.queryCommandState("bold"));
  italicButton.classList.toggle("active", document.queryCommandState("italic"));
  underlineButton.classList.toggle("active", document.queryCommandState("underline"));
}

// TOOLBAR BUTTON FUNCTIONS
function applyStyle(command) {
  document.execCommand(command, false, null);
  updateStyleButtons(); 
}
boldButton.addEventListener("click", () => applyStyle("bold"));
italicButton.addEventListener("click", () => applyStyle("italic"));
underlineButton.addEventListener("click", () => applyStyle("underline"));

// KEEP THE STYLE UPDATED WHILE TAKING NOTES
noteInput.addEventListener("keyup", updateStyleButtons);
noteInput.addEventListener("mouseup", updateStyleButtons);
noteInput.addEventListener("focus", updateStyleButtons);
noteInput.addEventListener("blur", updateStyleButtons);

// LOAD NOTE WHEN OPENING A NEW WINDOW
window.addEventListener("load", () => {
  // Load saved notes
  const savedNotes = JSON.parse(localStorage.getItem("notes")) || [];
  savedNotes.forEach(note => appendNoteToUI(note));

  // Load unsaved draft if any
  const draftNote = localStorage.getItem("tempNote");
  if (draftNote) noteInput.innerHTML = draftNote;
});

// NOTE SAVE FUNCTIOON
function saveNote() {
  const noteContent = noteInput.innerHTML.trim();
  if (!noteContent) return; // nothing to save

  const savedNotes = JSON.parse(localStorage.getItem("notes")) || [];
  savedNotes.push(noteContent);
  localStorage.setItem("notes", JSON.stringify(savedNotes));

  appendNoteToUI(noteContent);

  // clear input and temp draft
  noteInput.innerHTML = "";
  localStorage.removeItem("tempNote");
}

// SAVE ON BUTTON CLICK FUNCTION
saveButton.addEventListener("click", saveNote);

// SAVE WHEN ENTER IS PRESSED (SHIFT+ENTER ALLOWS NEWLINE)
noteInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    saveNote();
  }
});

// AUTO-SAVE FUNCTION AFTER TYPING
noteInput.addEventListener("input", () => {
  localStorage.setItem("tempNote", noteInput.innerHTML);
});

// ADD THE WRITTEN NOTES TO UI
function appendNoteToUI(note) {
  const noteContainer = document.createElement("div");
  noteContainer.classList.add("note-item");

  const noteText = document.createElement("div");
  noteText.classList.add("note-text");
  noteText.innerHTML = note; // preserve bold/italic/underline

  // DELETE BUTTON FUCNTION IN EACH NOTE
  const deleteBtn = document.createElement("button");
  deleteBtn.classList.add("delete-btn");
  deleteBtn.innerHTML = `<i class="fa-solid fa-trash"></i>`;
  deleteBtn.addEventListener("click", () => {
    noteContainer.remove();
    removeNoteFromStorage(note);
  });

  noteContainer.appendChild(noteText);
  noteContainer.appendChild(deleteBtn);
  notesList.appendChild(noteContainer);
}

// CLEAR NOTES FROM LOCALSTORAGE
function removeNoteFromStorage(note) {
  let savedNotes = JSON.parse(localStorage.getItem("notes")) || [];
  savedNotes = savedNotes.filter(n => n !== note);
  localStorage.setItem("notes", JSON.stringify(savedNotes));
}

// DELETE ALL NOTES
clearButton.addEventListener("click", () => {
  const confirmDelete = confirm("Are you sure you want to delete all notes?");
  if (!confirmDelete) return;

  localStorage.removeItem("notes");
  notesList.innerHTML = "";
});

// DOWNLOAD NOTES INTO TEXT FILES
downloadButton.addEventListener("click", () => {
  const savedNotes = JSON.parse(localStorage.getItem("notes")) || [];
  if (savedNotes.length === 0) {
    alert("No notes to download !");
    return;
  }

  let plainText = "";
  savedNotes.forEach((note, index) => {
    // strip HTML but preserve text
    const cleanNote = note.replace(/<[^>]*>/g, "");
    plainText += `Note ${index + 1}:\n${cleanNote}\n\n----------------------\n\n`;
  });

  const blob = new Blob([plainText], { type: "text/plain" });
  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");
  link.href = url;
  link.download = "QuickNotes.txt";
  link.click();

  URL.revokeObjectURL(url); // cleanup
});
