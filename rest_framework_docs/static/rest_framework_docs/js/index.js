var $ = window.$ = window.jQuery = require('jquery');
var bootstrap = require('bootstrap'); // eslint-disable-line no-unused-vars

var _ = require('underscore');
var React = require('react'); // eslint-disable-line no-unused-vars
var ReactDOM = require('react-dom');
var LiveAPIEndpoints = require('./components/liveapi');

var utils = {
  transformMethods: function (methods) {
    return methods
      .replace(/\W+/g, ' ')
      .replace(/^[ ]+|[ ]+$/g,'')
      .split(' ');
  },
};

$('.plug').bind('click', function(evt) {
  // Prevent the accordion from collapsing
  evt.stopPropagation();
  evt.preventDefault();

  // Open Modal
  $('#liveAPIModal').modal('toggle');

  // Setup the form
  var data = $(this).data();
  data.methods =  _.isArray(data.methods) ? data.methods : utils.transformMethods(data.methods);

  ReactDOM.render(
    <LiveAPIEndpoints endpoint={data} />, document.getElementById('liveAPIEndpoints')
  );
});

$('#liveAPIModal').on('hidden.bs.modal', function () {
  ReactDOM.unmountComponentAtNode(document.getElementById('liveAPIEndpoints'));
});
