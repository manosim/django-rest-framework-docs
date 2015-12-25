var React = require('react');
var APIRequest = require('superagent');

var RequestUtils = require('../utils/request');
var Request = require('./request');
var Response = require('./response');

var LiveAPIEndpoints = React.createClass({

  getInitialState: function() {
    return {
      response: null
    };
  },

  getData: function () {
    var method = this.refs.request.state.method;
    return RequestUtils.shouldAddData(method) ? null : (
      this.refs.request.state.data
    );
  },

  makeRequest: function (event) {
    event.preventDefault();

    var self = this;
    var request = this.refs.request.state;
    var data = this.getData();

    // Now Make the Request
    APIRequest(request.method, request.urlEndpoint)
      .send(data)
      .end(function (err, res) {
        self.setState({
          response: res
        });
      });
  },

  render: function () {

    return (
      <form className="form-horizontal">
        <div className="modal-body">
          <div className="row">
            <div className="col-md-6 request">
              <Request endpoint={this.props.endpoint} ref='request' />
            </div>
            <div className="col-md-6 response">
              <Response payload={this.state.response} />
            </div>
          </div>
        </div>
        <div className="modal-footer">
          <button type="button" className="btn btn-default" data-dismiss="modal">Close</button>
          <button type="submit" onClick={this.makeRequest} className="btn btn-primary">Send</button>
        </div>
      </form>
    );
  }
});

module.exports = LiveAPIEndpoints;
