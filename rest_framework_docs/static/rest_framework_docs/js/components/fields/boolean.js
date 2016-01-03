var React = require('react');

var FieldBoolean = React.createClass({
  getInitialState: function() {
    return {
      checked: null
    };
  },

  removeField: function (fieldName, event) {
    event.preventDefault();
    this.props.removeField(fieldName);
  },

  handleChange: function (value) {
    this.props.onChange(value);
  },

  isChecked: function (value) {
    if (this.props.value === undefined) return;
    return this.props.value === value;
  },

  render: function () {
    var labelName = this.props.name.replace('_', ' ');

    return (
      <div className='form-group'>
        <label
          htmlFor={this.props.name}
          className='col-sm-4 control-label'>
            {this.props.isCustom ? (
              <i
                className='fa fa-minus-circle'
                title='Remove Field'
                onClick={this.removeField.bind(this, this.props.name)} />
            ) : null}
            {labelName}
        </label>
        <div className='col-sm-8'>
          <label className='radio-inline'>
            <input
              type='radio'
              name={this.props.name}
              checked={this.isChecked(true)}
              onChange={this.handleChange.bind(this, true)} /> True
          </label>
          <label className='radio-inline'>
            <input
              type='radio'
              name={this.props.name}
              checked={this.isChecked(false)}
              onChange={this.handleChange.bind(this, false)} /> False
          </label>
        </div>
      </div>
    );
  }
});

module.exports = FieldBoolean;
