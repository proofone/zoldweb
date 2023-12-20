const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  mode: 'development',

  devtool: 'inline-source-map',
  devServer: {
    static: '../public',
    port: 3002
  },
  optimization: {
    runtimeChunk: 'single',
  },

  entry: {
    'main': './react_client/src/App.js'
  },
  plugins: [
    // new HtmlWebpackPlugin({
    //   title: 'Development',
    //   template: 'templates/base.html'
    // }),
    new MiniCssExtractPlugin(),
  ],
  output: { 
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, '../public'),
  },

  module: {
    rules: [
      {
        test: /\.jsx?$/,
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
      },
      {
        test: /\.tsx?$/,
        exclude: /node_modules/,
        use: 'ts-loader',
      },      
      {
        test: /\.(scss)$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: () => [
                  require('autoprefixer')
                ]
              }
            }
          },
          {
            loader: 'sass-loader'
          }
        ]
      }
    ]
  }
};
