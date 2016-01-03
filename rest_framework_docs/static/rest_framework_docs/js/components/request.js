var _ = require('underscore');
var React = require('react');

var AddFieldsForm = require('./request/add-fields');
var Headers = require('./request/headers');
var Data = require('./request/data');
var FieldUrl = require('./request/field-url');
var Methods = require('./request/methods');

var Request = React.createClass({
  getInitialState: function () {
    return {
      data: {},
      endpoint: null,
      headers: {},
      selectedMethod: null,
    };
  },

  componentWillMount: function() {
    var endpoint = this.props.endpoint;
    var headers = this.state.headers;
    headers['authorization'] = window.token ? window.token : '';

    this.setState({
      endpoint: endpoint,
      headers: headers,
      selectedMethod: endpoint['methods'][0]
    });
  },

  addField: function (fieldName) {
    var endpoint = this.state.endpoint;

    // Check if field already exists
    if (_.findWhere(endpoint.fields, {'name': fieldName})) return;

    endpoint.fields.push({
      name: fieldName,
      required: false,
      type: 'text',
      isCustom: true
    });

    this.setState({
      endpoint: endpoint
    });
  },

  removeField: function (fieldName) {
    var data = this.state.data;
    var endpoint = this.state.endpoint;
    var fields = endpoint.fields;

    data = _.omit(data, fieldName);
    fields = _.without(fields, _.findWhere(fields, {name: fieldName}));
    endpoint.fields = fields;

    this.setState({
      data: data,
      endpoint: endpoint
    });
  },

  setSelectedMethod: function (method) {
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

  handleHeaderChange: function (value, fieldName) {
    var headers = this.state.headers;
    headers[fieldName] = value;
    this.setState({
      headers: headers
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

        <FieldUrl
          name='urlEndpoint'
          url={endpoint.path}
          onChange={this.handleUrlChange} />

        <Methods
          methods={this.state.endpoint.methods}
          selectedMethod={this.state.selectedMethod}
          setMethod={this.setSelectedMethod} />

        <Headers
          headers={this.state.headers}
          permissions={this.state.endpoint.permissions}
          handleHeaderChange={this.handleHeaderChange} />

        <Data
          method={this.state.selectedMethod}
          fields={endpoint.fields}
          data={this.state.data}
          removeCustomField={this.removeField}
          onChange={this.handleDataFieldChange} />

        <AddFieldsForm
          onAdd={this.addField} />
      </div>
    );
  }
});

module.exports = Request;
