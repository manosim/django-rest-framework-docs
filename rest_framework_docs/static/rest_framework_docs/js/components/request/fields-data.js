var React = require('react');

var Input = require('../helpers/input');

var FieldsData = React.createClass({

  handleChange: function (fieldName, event) {
    this.props.onChange(event.target.value, fieldName);
  },

  _renderFields: function () {
    return this.props.fields.map(function (field, key) {
      var value = this.props.data[field.name];
      return (
        <Input
          key={key}
          name={field.name}
          value={value}
          placeholder={field.type}
          required={field.required}
          onChange={this.handleChange.bind(this, field.name)} />
      );
    }, this);
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
