var React = require('react');

var Methods = React.createClass({

  getInitialState: function() {
    return {
      methods: []
    };
  },

  componentWillMount: function() {
    var methods =this.props.methods
        .replace(/\W+/g, " ")
        .replace(/^[ ]+|[ ]+$/g,'')
        .split(" ");

    this.setState({
      methods: methods
    });

    this.props.setMethod(methods[0]);
  },

  setMethod: function (value) {
    this.props.setMethod(value);
  },

  render: function () {
    // var self = this;

    return (
      <div className="btn-group methods">
        {this.state.methods.map(function (method, i) {
          var methodClass = "btn btn-sm method " + method.toLowerCase() + (this.props.active == method ? ' active': null);
          return <button key={i} type='button' className={methodClass} onClick={this.setMethod.bind(this, method)}>{method}</button>;
        }, this)}
      </div>
    );
  }
});

module.exports = Methods;
