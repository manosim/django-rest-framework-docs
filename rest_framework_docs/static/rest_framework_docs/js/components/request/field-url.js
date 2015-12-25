var _ = require('underscore');
var React = require('react');

var Input = require('../helpers/input');

var FieldUrl = React.createClass({

  handleChange: function (value) {
    console.log('111111');
    this.props.onChange(value);
  },

  render: function () {
    return (
      <Input name='Url Endpoint' value={this.props.value} onChange={this.handleChange} />
    );
  }
});

module.exports = FieldUrl;
