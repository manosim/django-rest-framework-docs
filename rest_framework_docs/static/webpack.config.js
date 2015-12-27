// var path = require('path');
var webpack = require('webpack');

module.exports = {
  context: __dirname + '/rest_framework_docs/js',
  entry: './index.js',
  output: {
    path: __dirname + '/rest_framework_docs/js',
    filename: 'dist.js'
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false,
      },
      output: {
        comments: false,
        sourceMap: false
      }
    }),
    new webpack.NoErrorsPlugin()
  ],
  module: {
    loaders: [{
      test: /\.js?$/,
      // include: path.join(__dirname, '/rest_framework_docs/js'),
      exclude: /node_modules/,
      loader: 'babel',
      query: {
        presets: ['es2015', 'react']
      }
    }]
  }
};
