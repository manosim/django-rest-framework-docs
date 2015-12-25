'use strict';

var React = require('react');
var ReactDOM = require('react-dom');
var LiveAPI = require('./components/liveapi');

$('.plug').bind('click', function(evt) {
  // Prevent the accordion from collapsing
  evt.stopPropagation();
  evt.preventDefault();

  // Open Modal
  $('#liveAPIModal').modal('toggle');

  // Setup the form
  var data = $(this).data();

  ReactDOM.render(
    <LiveApi endpoint={data} />, document.getElementById('endpoints')
  );
});
