var React = require('react');

var FieldsData = require('./request/fields-data');
var FieldUrl = require('./request/field-url');
var Header = require('./helpers/header');
var Methods = require('./request/methods');
var RequestUtils = require('../utils/request');

var Request = React.createClass({
  getInitialState: function () {
    return {
      endpoint: null,
      data: {},
      selectedMethod: null,
    };
  },

  componentWillMount: function() {
    var endpoint = this.props.endpoint;

    this.setState({
      endpoint: endpoint,
      selectedMethod: endpoint['methods'][0]
    });
  },

  setSelectedMethod: function (method) {
    console.log('REQUEST _ setSelectedMethod');

    this.setState({
      selectedMethod: method
    });
  },

  handleUrlChange: function (event) {
    var endpoint = this.state.endpoint;
    endpoint.path = event.target.value;

    this.setState({
      endpoint: endpoint
    });
  },

  handleDataFieldChange: function (value, fieldName) {
    var data = this.state.data;
    data[fieldName] = value;
    this.setState({
      data: data
    });
  },

  render: function () {
    var endpoint = this.state.endpoint;
    return (
      <div>
        <h3>Request</h3>

        <Header title='API Endpoint' />
        <FieldUrl
          name='urlEndpoint'
          url={endpoint.path}
          onChange={this.handleUrlChange} />

        <Header title='Method' />
        <Methods
          methods={this.state.endpoint.methods}
          selectedMethod={this.state.selectedMethod}
          setMethod={this.setSelectedMethod} />

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
            {this.state.endpoint.fields.length ? <Header title='Data' /> : null}
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
