var React = require('react');

var Header = require('../helpers/header');
var FieldText = require('../fields/text');

var FieldUrl = React.createClass({

  getInitialState: function() {
    return {
      url: this.props.url
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
      <div>
        <Header title='API Endpoint' />
        <FieldText
          type='text'
          name='Url Endpoint'
          value={this.state.url}
          placeholder='Endpoint Url'
          onChange={this.handleChange} />
      </div>
    );
  }
});

module.exports = FieldUrl;
