var _ = require('underscore');
var slugify = require("underscore.string/slugify");
var React = require('react');
var Endpoint = require('./endpoint');

var Endpoints = React.createClass({

  getInitialState: function () {
    return {
      endpoints: [],
    };
  },

  componentDidMount: function() {
    var grouped = _.groupBy(this.props.endpoints, 'name_parent');
    this.setState({
      endpoints: grouped
    });
  },

  _renderGroups: function () {
    return _.map(this.state.endpoints, function (group, name) {
      var slug = slugify(name, 'group');
      return (
        <div key={slug}>
          <h1 id={slug}>{name}</h1>
          <div className="panel-group" role="tablist">
            {_.map(group, function (endpoint) {
              return <Endpoint key={endpoint.path} endpoint={endpoint} group={slug} />
            })}
          </div>
        </div>
      );
    })
  },

  render: function () {
    return (
      <div>
        {this._renderGroups()}
      </div>
    );
  }
});

module.exports = Endpoints;
