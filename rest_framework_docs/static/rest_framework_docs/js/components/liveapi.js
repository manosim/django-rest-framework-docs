var _ = require('underscore');
var slugify = require("underscore.string/slugify");
var React = require('react');
// var Endpoint = require('./endpoint');

var LiveAPI = React.createClass({

  getInitialState: function () {
    return {
      endpoints: [],
    };
  },

  render: function () {
    return (
      <div>
        {this._renderGroups()}
      </div>
    );
  }
});

module.exports = LiveAPI;
