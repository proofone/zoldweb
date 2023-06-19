const express = require("express");
const mongoose = require('mongoose')
//var cors = require('cors');

// Connect MongoDB
const mongoService = process.env.MONGO_SERVICE || "localhost"
const mongoPort = process.env.MONGO_PORT || 27017;
const mongoUrl = `mongodb://${mongoService}:${mongoPort}/mini-message-board`;
mongoose.connect(mongoUrl).then(() => {
    console.log(`MongoDB running at port ${mongoPort}`);    
}
).catch(err => console.log(err))

const PORT = process.env.PORT || 3001;

const app = express();

app.engine('.html', require('ejs').__express);

app.set('views', './templates')
var staticOptions = {setHeaders: function (res, path, stat) {
    res.set('Access-Control-Allow-Origin', '*')
  }
}  //TODO: import from settings file

app.use(express.static('public', staticOptions));

app.get("/", (req, res) => {
    res.render("index.html");
});
app.get("/base", (req, res) => {
    res.render("base.html")
});
app.post("/newsfeed/sendpost", (req, res) => {
    console.log(`Request received: ${req.body}`)

    res.send({status: "OK"})
});

app.listen(PORT, () => {
    console.log(`Zoldweb NodeJS Server listening on :${PORT}`);
});
