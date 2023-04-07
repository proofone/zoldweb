const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();

app.set('views', './templates')

app.get("/", (req, res) => {
    res.json({ message: "Hello world!" });
});
app.get("/base", (req, res) => {
    res.render("base")
});

app.listen(PORT, () => {
    console.log(`Zoldweb NodeJS Server listening on ${PORT}`);
});