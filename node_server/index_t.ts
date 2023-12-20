import path = require('path');
import express = require("express");
import bodyParser = require('body-parser');
const { MongoClient } = require("mongodb");
import { Message } from './models/messages';
import { staticOptions, publicPath } from './config';


const PORT = process.env.PORT || 3001;
//const publicPath = path.join(__dirname, '../public');
const mongoService = process.env.MONGO_SERVICE || "0.0.0.0"
const mongoPort = process.env.MONGO_PORT || 27017;
const mongoUrl = `mongodb://${mongoService}:${mongoPort}/mini-message-board`;
const mongoClient = new MongoClient(mongoUrl);
const database = mongoClient.db('zoldweb');
const messagesColl = database.collection('messages');

const app = express();
app.engine('.html', require('ejs').__express);
app.set('views', publicPath)
app.use('/static', express.static(publicPath, staticOptions));
app.use(bodyParser.json())

//Endpoints:
app.get("/", (req, res) => {
    res.render("index.html");
});
app.post("/newsfeed/sendpost", (req, res) => {
    console.log(`Request received: ${req.path} ${req.body}`)
    const msg: Message = {
        author_id: '1',
        created_date: new Date(),
        content: ""
    };
    messagesColl.insertOne(msg).then(r => {
        res.send({status: "OK"})
    }).catch(err => {
        console.log(`Error saving to db: ${err}`)
    }) 
});
app.get("/newsfeed/getpost", (req, res) => {
    console.log(`Request received: ${req.path}`)
    const params = {}
    const sort = {_id: -1};
    const cursor = messagesColl.find(params).sort(sort).limit(100)
    cursor.toArray()
        .then(arr => {
            res.send({status: "OK", messages: arr})
        }).catch(err => {
            console.log(`Error loading messages from db: ${err}`)
        })
});

//Startup:
app.listen(PORT, () => {
    console.log(`Zoldweb NodeJS Server listening on :${PORT}`);

});
