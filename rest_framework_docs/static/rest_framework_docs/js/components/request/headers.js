var React = require('react');

var Input = require('../helpers/input');

var Headers = React.createClass({

  getInitialState: function() {
    return {
      authorization: this.props.headers.authorization
    };
  },

  handleChange: function (fieldName, event) {
    this.props.handleHeaderChange(event.target.value, fieldName);
  },

  componentWillReceiveProps: function(nextProps) {
    this.setState({
      authorization: nextProps.headers.authorization
    });
  },

  render: function () {
    return (
      <div>
        <Input
          name='authorization'
          value={this.state.authorization}
          placeholder='Token 1234567890'
          onChange={this.handleChange.bind(this, 'authorization')} />
      </div>
    );
  }
});

module.exports = Headers;
