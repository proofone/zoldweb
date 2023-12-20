var path = require('path');


export const staticOptions: Object = {
  setHeaders: function (res, path, stat) {
    res.set('Access-Control-Allow-Origin', '*')
  }
}

export const publicPath: string = path.join(__dirname, '../brahma/brahma/static');

