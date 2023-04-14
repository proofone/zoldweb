const express = require("express");
var path = require('path');

const PORT = process.env.PORT || 3001;

const app = express();

app.engine('.html', require('ejs').__express);

app.set('views', './templates')
app.use(express.static(path.join(__dirname, 'public')));

app.get("/", (req, res) => {
    res.json({ message: "Hello world!" });
});
app.get("/base", (req, res) => {
    res.render("base.html")
});

app.listen(PORT, () => {
    console.log(`Zoldweb NodeJS Server listening on ${PORT}`);
});