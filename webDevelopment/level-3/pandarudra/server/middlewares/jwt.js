const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");
dotenv.config();

const setToken = (email, id) => {
  const token = jwt.sign({ email, id }, process.env.JWT_SECRET, {
    expiresIn: "7d",
  });
  return token;
};

const verifyToken = (req, res, next) => {
  const btoken = req.headers.authorization;
  const token = btoken.split(" ")[1];

  if (!token) {
    return res.status(401).json({ message: "Unauthorized Access" });
  }
  jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
    if (err) {
      if (err.name === "TokenExpiredError") {
        return reissueToken(req, res);
      } else {
        return res.status(401).json({ message: "Unauthorized Access" });
      }
    }
    req.user = decoded;
    next();
  });
};

const reissueToken = (req, res) => {
  const token = setToken(req.user.email, req.user.id);
  res.status(200).json({ token });
};
module.exports = { setToken, verifyToken };
