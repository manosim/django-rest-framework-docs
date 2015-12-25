var React = require('react');

var Input = require('../helpers/input');

var FieldUrl = React.createClass({

  getInitialState: function() {
    return {
      value: this.props.url
    };
  },

  componentWillReceiveProps: function(nextProps) {
    this.setState({
      url: nextProps.url
    });
  },

  handleChange: function (value) {
    this.props.onChange(value);
  },

  render: function () {
    return (
      <Input
        name='Url Endpoint'
        value={this.state.url}
        placeholder='Endpoint Url'
        onChange={this.handleChange} />
    );
  }
});

module.exports = FieldUrl;
