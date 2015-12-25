var React = require('react');

var JSONpp = require('../utils/jsonpp');

var Response = React.createClass({

  getInitialState: function () {
    return {
      endpoints: [],
    };
  },

  render: function () {
    if (!this.props.payload) {
      return (
        <div>
          <h3>Response <span className='label status-code pull-right'></span></h3>
          <p className='lead text-center'>Awaiting request...</p>
        </div>
      );
    }

    var responseJSON = JSONpp.prettyPrint(this.props.payload.body);
    var statusText = this.props.payload.statusText.toLowerCase();
    var statusCodeFirstChar = String(this.props.payload.status).charAt(0);
    var statusCodeClass = 'label status-code pull-right status-code-' + statusCodeFirstChar;

    return (
      <div>
        <h3>Response <span className={statusCodeClass}>{this.props.payload.status}</span></h3>

        <div><strong>Status</strong>: <span className='status-text'>{statusText}</span></div>
        <pre><code dangerouslySetInnerHTML={{__html: responseJSON}}></code></pre>
        <div className='well well-default text-center'>
          <button className='btn btn-sm btn-info'><i className='fa fa-key'></i> Save Token</button>
          <h6>Your token will be lost when you refresh the page.</h6>
        </div>
      </div>
    );
  }
});

module.exports = Response;
