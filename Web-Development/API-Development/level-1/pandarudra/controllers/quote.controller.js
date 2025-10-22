import { quotes } from "../data/mockdata.js";

export const getAllQuotes = (req, res) => {
  try {
    const allQuotes = quotes.map((e, i) => e.text);
    res.status(200).json(allQuotes);
  } catch (error) {
    res.status(500).json({ message: "Server Error" });
  }
};

export const getRandomQuote = (req, res) => {
  try {
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    res.status(200).json(randomQuote.text);
  } catch (error) {
    res.status(500).json({ message: "Server Error" });
  }
};

export const getQuotesByCategory = (req, res) => {
  try {
    const { category } = req.params;
    const filteredQuotes = quotes.filter(
      (quote) => quote.category === category
    );
    res.status(200).json(filteredQuotes);
  } catch (error) {
    res.status(500).json({ message: "Server Error" });
  }
};

export const getAllCategories = (req, res) => {
  try {
    const categories = [...new Set(quotes.map((quote) => quote.category))];
    res.status(200).json(categories);
  } catch (error) {
    res.status(500).json({ message: "Server Error" });
  }
};
