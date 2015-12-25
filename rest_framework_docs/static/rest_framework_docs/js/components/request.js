var _ = require('underscore');
var React = require('react');

var Methods = require('./request/methods');

var Request = React.createClass({

  getInitialState: function () {
    return {
      method: null
    };
  },

  setMethod: function (method) {
    this.setState({
      method: method
    });
  },

  render: function () {
    var endpoint = this.props.endpoint;

    return (
      <div>
        <h3>Request</h3>

        <div className="form-group">
          <label htmlFor="urlInput" className="col-sm-4 control-label">Endpoint</label>
          <div className="col-sm-8">
            <input type="text" className="form-control input-sm" id="urlInput" placeholder="Url" value={endpoint.path} />
          </div>
        </div>

        <h5 className="section-title"><span>Method</span></h5>
        <Methods methods={endpoint.methods} active={this.state.method} setMethod={this.setMethod} />

        <div id="headers">
          <h5 className="section-title"><span>Headers</span></h5>
          <div className="form-group">
            <label htmlFor="authorization" className="col-sm-4 control-label">Authorization</label>
            <div className="col-sm-8">
              <input type="text" className="form-control input-sm" id="authorization" placeholder="Token" />
            </div>
          </div>
        </div>

        <h5 className="section-title" id="headerData"><span>Data</span></h5>
        <div id="fields" className="fields"></div>
      </div>
    );
  }
});

module.exports = Request;
