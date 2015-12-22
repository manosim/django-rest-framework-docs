'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var Endpoints = require('./components/endpoints');

ReactDOM.render(
  <Endpoints items={endpoints} tags={tags} />, document.getElementById('endpoints')
);
