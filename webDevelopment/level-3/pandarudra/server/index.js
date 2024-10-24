const express = require("express");
const app = express();
const dotenv = require("dotenv");
dotenv.config();
const cors = require("cors");
const path = require("path");
const { signup, signin, tasks } = require("./controllers/user.controllers");

const { verifyToken } = require("./middlewares/jwt");

const PORT = process.env.PORT || 3000;
app.use(express.json());

app.use(cors());
//client rendering
app.use(express.static(path.resolve(__dirname, "../client")));
//Login page
app.get("/login", (req, res) => {
  res.sendFile(path.resolve(__dirname, "../client/Login/index.html"));
});
//Signup page
app.get("/signup", (req, res) => {
  res.sendFile(path.resolve(__dirname, "../client/Signup/index.html"));
});
//Task Profile page
app.get("/profile", (req, res) => {
  res.sendFile(path.resolve(__dirname, "../client/Todo/index.html"));
});
//post request

app.post("/register", signup);
app.post("/signin", signin);
app.post("/tasks", verifyToken, tasks);

//GET request

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
