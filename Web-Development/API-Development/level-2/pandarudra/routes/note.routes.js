import express from "express";
import {
  createNote,
  deleteNote,
  getNoteById,
  getNotes,
  updateNote,
} from "../controllers/note.controller.js";

const NoteRouter = express.Router();

NoteRouter.post("/", createNote);
NoteRouter.get("/", getNotes);
NoteRouter.get("/:id", getNoteById);
NoteRouter.put("/:id", updateNote);
NoteRouter.delete("/:id", deleteNote);

export default NoteRouter;
