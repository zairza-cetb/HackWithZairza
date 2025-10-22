import { notes } from "../db/notes.js";
import { v4 as uuidv4 } from "uuid";
import fs from "fs";
import path from "path";

const updateDB = () => {
  const fileContent = `export const notes = ${JSON.stringify(
    notes,
    null,
    2
  )};\n`;
  fs.writeFileSync(path.join(process.cwd(), "db", "notes.js"), fileContent);
};

export const createNote = (req, res) => {
  const { title, content, tags } = req.body;
  try {
    const newNote = {
      id: uuidv4(),
      title,
      content,
      tags,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };
    notes.push(newNote);
    updateDB();
    res.status(201).send(newNote);
  } catch (error) {
    res.status(500).send({ message: error.message });
  }
};
export const getNotes = (req, res) => {
  try {
    res.status(200).send(notes);
  } catch (error) {
    res.status(500).send({ message: "Server Error" });
  }
};
export const getNoteById = (req, res) => {
  const note = notes.find((n) => n.id === req.params.id);
  if (note) {
    res.status(200).send(note);
  } else {
    res.status(404).send({ message: "Note not found" });
  }
};
export const updateNote = (req, res) => {
  const note = notes.find((n) => n.id === req.params.id);
  if (note) {
    const { title, content, tags } = req.body;
    note.title = title;
    note.content = content;
    note.tags = tags;
    note.updatedAt = new Date().toISOString();
    updateDB();
    res.status(200).send(note);
  } else {
    res.status(404).send({ message: "Note not found" });
  }
};
export const deleteNote = (req, res) => {
  const noteIndex = notes.findIndex((n) => n.id === req.params.id);
  if (noteIndex !== -1) {
    notes.splice(noteIndex, 1);
    updateDB();
    res.status(204).send();
  } else {
    res.status(404).send({ message: "Note not found" });
  }
};
