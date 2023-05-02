const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'development',

  devtool: 'inline-source-map',
  devServer: {
    static: './public',
    port: 3002
  },
  optimization: {
    runtimeChunk: 'single',
  },

  entry: {
    'main': './src/App.js'
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: 'Development',
      template: 'templates/base.html'
    }),
  ],
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'public'),
  },

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [
              ['@babel/preset-env', {"targets": "defaults"}],
              ['@babel/preset-react', {"runtime": "automatic"}]  // runtime: automatic attribute required for React to work
            ]          
	        },
      	},
      }
    ]
  }
};
