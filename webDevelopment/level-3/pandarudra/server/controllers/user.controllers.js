const { setToken } = require("../middlewares/jwt");
//Signup controller
const signup = (req, res) => {
  const { name, email, password } = req.body;
  if (!name || !email || !password) {
    return res.status(400).json({ error: "Please fill all the fields" });
  }
  try {
    return res.json({ message: "Signup successful" });
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
};
//Signin controller
const signin = (req, res) => {
  const { email, password, db } = req.body;
  if (!email || !password) {
    return res.status(400).json({ error: "Please fill all the fields" });
  }
  try {
    const user = db.find((user) => user.email === email);
    if (!user) {
      return res.status(400).json({ error: "User not found" });
    }
    if (user.password !== password) {
      return res.status(400).json({ error: "Invalid password" });
    }
    const token = setToken(email, user.id);
    res.json({ id: user.id, message: "Signin successful", token: token });
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
};
//Tasks controller
const tasks = (req, res) => {
  const { id, db, tasks } = req.body;
  console.log({ id, db });
  if (!id) {
    return res.status(400).json({ error: "Please provide user info" });
  }
  try {
    let dbArray = Array.isArray(db) ? db : JSON.parse(db);
    const user = dbArray.find((user) => user.id === id);

    if (!user) {
      return res.status(400).json({ error: "User not found" });
    }
    return res.json({ tasks: user.tasks, tasks });
  } catch (error) {
    console.log({ error });
    res.status(500).json({ error: error.message });
  }
};
module.exports = { signup, signin, tasks };
