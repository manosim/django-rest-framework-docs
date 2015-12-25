var _ = require('underscore');
var React = require('react');

var Request = require('./request');
var Response = require('./response');

var LiveAPIEndpoints = React.createClass({

  render: function () {

    return (
      <form className="form-horizontal">
        <div className="modal-body">
          <div className="row">
            <div className="col-md-6 request">
              <Request endpoint={this.props.endpoint} />
            </div>
            <div className="col-md-6 response">
              <Response />
            </div>
          </div>
        </div>
        <div className="modal-footer">
          <button type="button" className="btn btn-default" data-dismiss="modal">Close</button>
          <button type="submit" id="submitButton" className="btn btn-primary">Send</button>
        </div>
      </form>
    );
  }
});

module.exports = LiveAPIEndpoints;
