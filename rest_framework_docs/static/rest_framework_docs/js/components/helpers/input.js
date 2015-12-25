var _ = require('underscore');
var React = require('react');

var Input = React.createClass({

  handleChange: function (value) {
    this.props.onChange(value);
  },

  render: function () {
    return (
      <div className="form-group">
        <label htmlFor={this.props.name} className="col-sm-4 control-label">{this.props.name}</label>
        <div className="col-sm-8">
          <input
            type="text"
            className="form-control input-sm"
            id={this.props.name}
            placeholder="Url"
            onChange={this.handleChange}
            value={this.props.value} />
        </div>
      </div>
    );
  }
});

module.exports = Input;
