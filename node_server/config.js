"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.publicPath = exports.staticOptions = void 0;
var path = require('path');
exports.staticOptions = {
    setHeaders: function (res, path, stat) {
        res.set('Access-Control-Allow-Origin', '*');
    }
};
exports.publicPath = path.join(__dirname, '../brahma/brahma/static');
