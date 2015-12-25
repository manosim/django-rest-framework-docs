var React = require('react');

var FieldsData = require('./request/fields-data');
var FieldUrl = require('./request/field-url');
var Header = require('./helpers/header');
var Methods = require('./request/methods');
var RequestUtils = require('../utils/request');

var Request = React.createClass({

  getInitialState: function () {
    return {
      data: {},
      method: null,
      urlEndpoint: this.props.endpoint.path
    };
  },

  componentWillReceiveProps: function(nextProps) {
    this.setState({
      urlEndpoint: nextProps.endpoint.path 
    });
  },

  setMethod: function (method) {
    this.setState({
      method: method
    });
  },

  handleInputChange: function (value, event) {
    var state = this.state;
    state[value] = event.target.value;
    this.setState(state);
  },

  handleDataFieldChange: function (value, fieldName) {
    var data = this.state.data;
    data[fieldName] = value;
    this.setState({
      data: data
    });
  },

  render: function () {
    var endpoint = this.props.endpoint;

    return (
      <div>
        <h3>Request</h3>

        <Header title='API Endpoint' />
        <FieldUrl
          name='urlEndpoint'
          url={this.state.urlEndpoint}
          onChange={this.handleInputChange.bind(this, 'urlEndpoint')} />

        <Header title='Method' />
        <Methods methods={endpoint.methods} active={this.state.method} setMethod={this.setMethod} />

        <Header title='Headers' />
        <div className="form-group">
          <label htmlFor="authorization" className="col-sm-4 control-label">Authorization</label>
          <div className="col-sm-8">
            <input
              type="text"
              className="form-control input-sm"
              placeholder="Token" />
          </div>
        </div>

        {RequestUtils.shouldAddData(this.state.method) ? null : (
          <div>
            <Header title='Data' />
            <FieldsData
              fields={endpoint.fields}
              data={this.state.data}
              onChange={this.handleDataFieldChange} />
          </div>
        )}
      </div>
    );
  }
});

module.exports = Request;
