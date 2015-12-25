var _ = require('underscore');
var React = require('react');

var FieldUrl = require('./request/field-url');
var Header = require('./helpers/header');
var Methods = require('./request/methods');
var FieldsData = require('./request/fields-data');

var Request = React.createClass({

  getInitialState: function () {
    return {
      urlEndpoint: this.props.endpoint.path,
      method: null
    };
  },

  setMethod: function (method) {
    this.setState({
      method: method
    });
  },

  handleInputChange: function (value, event) {
    console.log(value);
    console.log(event.target.value);
    console.log('---------------');

    var state = this.state;
    state[value] = event.target.value;
    this.setState(state);
  },

  render: function () {
    var endpoint = this.props.endpoint;

    return (
      <div>
        <h3>Request</h3>

        <Header title='API Endpoint' />
        <FieldUrl name='urlEndpoint' value={this.state.urlEndpoint} onChange={this.handleInputChange.bind(this, 'urlEndpoint')} />

        <Header title='Method' />
        <Methods methods={endpoint.methods} active={this.state.method} setMethod={this.setMethod} />

        <Header title='Headers' />
        <div className="form-group">
          <label htmlFor="authorization" className="col-sm-4 control-label">Authorization</label>
          <div className="col-sm-8">
            <input type="text" className="form-control input-sm" id="authorization" placeholder="Token" />
          </div>
        </div>

        <Header title='Data' />
        <FieldsData fields={endpoint.fields} onChange={this.handleInputChange.bind(this, 'fields')} />
      </div>
    );
  }
});

module.exports = Request;
