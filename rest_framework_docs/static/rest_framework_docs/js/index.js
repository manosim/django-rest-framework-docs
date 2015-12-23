'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var Endpoints = require('./components/endpoints');

window.setupEndpoints = function (endpoints) {
  ReactDOM.render(
    <Endpoints endpoints={endpoints} />, document.getElementById('endpoints')
  );
};
