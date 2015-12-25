'use strict';

var $ = window.$ = window.jQuery = require('jquery');
var jQuery = require('jquery');

var React = require('react');
var ReactDOM = require('react-dom');
var LiveAPIEndpoints = require('./components/liveapi');


$('.plug').bind('click', function(evt) {
  // Prevent the accordion from collapsing
  evt.stopPropagation();
  evt.preventDefault();

  // Open Modal
  $('#liveAPIModal').modal('toggle');

  // Setup the form
  var data = $(this).data();

  ReactDOM.render(
    <LiveAPIEndpoints endpoint={data} />, document.getElementById('liveAPIEndpoints')
  );
});
