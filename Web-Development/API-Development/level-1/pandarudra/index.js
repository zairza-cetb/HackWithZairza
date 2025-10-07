import express from "express";
import cors from "cors";
import "dotenv/config";
import QuoteRouter from "./routes/quote.routes.js";

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const PORT = process.env.PORT || 3000;

app.use("/api", QuoteRouter);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
