var React = require('react');

var Methods = React.createClass({

  getInitialState: function() {
    return {
      methods: [],
      selectedMethod: null
    };
  },

  componentWillMount: function() {
    this.setState({
      methods: this.props.methods,
      selectedMethod: this.props.selectedMethod
    });
  },

  componentWillReceiveProps: function(nextProps) {
    this.setState({
      methods: nextProps.methods,
      selectedMethod: nextProps.selectedMethod
    });
  },

  setMethod: function (value) {
    this.props.setMethod(value);
  },

  render: function () {
    return (
      <div className='btn-group methods'>
        {this.state.methods.map(function (method, i) {
          var methodClass = 'btn btn-sm method ' + method.toLowerCase() +
            (this.state.selectedMethod == method ? ' active' : null);
          return (
            <button
              key={i}
              type='button'
              className={methodClass}
              onClick={this.setMethod.bind(this, method)}>{method}</button>
          );
        }, this)}
      </div>
    );
  }
});

module.exports = Methods;
