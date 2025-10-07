import express from "express";
import {
  getAllCategories,
  getAllQuotes,
  getQuotesByCategory,
  getRandomQuote,
} from "../controllers/quote.controller.js";
const QuoteRouter = express.Router();

QuoteRouter.get("/quotes", getAllQuotes);
QuoteRouter.get("/quotes/random", getRandomQuote);
QuoteRouter.get("/quotes/category/:category", getQuotesByCategory);
QuoteRouter.get("/categories", getAllCategories);

export default QuoteRouter;
