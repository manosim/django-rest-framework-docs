var React = require('react');

var Input = require('../helpers/input');

var FieldsData = React.createClass({

  handleChange: function (value, event) {
    this.props.onChange(value, event);
  },

  _renderFields: function () {
    return this.props.fields.map(function (field, key) {
      return (
        <Input
          key={key}
          name={field.name}
          value=''
          placeholder={field.type}
          required={field.required}
          onChange={this.handleChange.bind(this, field.name)} />
      );
    }, this)
  },

  render: function () {
    return (
      <div>
        {this._renderFields()}
      </div>
    );
  }
});

module.exports = FieldsData;
