var React = require('react');

var Header = React.createClass({

  render: function () {
    return (
      <h5 className='section-title'>{this.props.title}</h5>
    );
  }
});

module.exports = Header;
