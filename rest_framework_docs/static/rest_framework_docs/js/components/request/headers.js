var React = require('react');

var Header = require('../helpers/header');
var FieldText = require('../fields/text');
var RequestUtils = require('../../utils/request');

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
    if (!RequestUtils.shouldAddHeader(this.props.permissions)) {
      return null;
    }

    return (
      <div>
        <Header title='Headers' />
        <FieldText
          name='authorization'
          value={this.state.authorization}
          placeholder='Token 1234567890'
          onChange={this.handleChange.bind(this, 'authorization')} />
      </div>
    );
  }
});

module.exports = Headers;
