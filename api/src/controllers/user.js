const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const users = []; // In-memory for demo only

exports.register = async (req, res, next) => {
  try {
    const { email, password } = req.body;
    if (!email || !password)
      return res.status(400).json({ error: 'Email and password required' });
    const hashed = await bcrypt.hash(password, 10);
    users.push({ email, password: hashed });
    res.status(201).json({ message: 'User registered' });
  } catch (err) {
    next(err);
  }
};

exports.login = async (req, res, next) => {
  try {
    const { email, password } = req.body;
    const user = users.find(u => u.email === email);
    if (!user) return res.status(401).json({ error: 'Invalid credentials' });
    const valid = await bcrypt.compare(password, user.password);
    if (!valid) return res.status(401).json({ error: 'Invalid credentials' });
    const token = jwt.sign({ email }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token });
  } catch (err) {
    next(err);
  }
};

exports.profile = (req, res) => {
  res.json({ email: req.user.email }); // hi i made a change
  console.log('making very important changes')
};
