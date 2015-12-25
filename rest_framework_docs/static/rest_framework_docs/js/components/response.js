var _ = require('underscore');
var React = require('react');

var Response = React.createClass({

  getInitialState: function () {
    return {
      endpoints: [],
    };
  },

  render: function () {
    return (
      <div>
        <h3>Response <span className="label status-code pull-right"></span></h3>

        <div><strong>Status</strong>: <span className="status-text"></span></div>
        <pre><code></code></pre>
        <div className="well well-default text-center">
          <button className='btn btn-info'><i className='fa fa-key'></i> Save Token</button>
          <h5>Your token will be lost when you refresh the page.</h5>
        </div>
      </div>
    );
  }
});

module.exports = Response;
