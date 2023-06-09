const mongoose = require('mongoose');

const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;

const Message = new Schema({
    id: { type: ObjectId },
    author: {
        type: String,
        default: "John Doe",
        required: true
    },
    recipient: {
        type: String,
        default: "John Doe",
        required: false
    },
    body: {
        type: String,
        default: "Roses are Red, Violets are Blue. Unexpected '{' on line 32.",
        required: true
    },
    date: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Message', Message);