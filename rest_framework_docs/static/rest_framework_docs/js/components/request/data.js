var React = require('react');

var FieldInput = require('../fields/input');

var Data = React.createClass({

  removeCustomField: function (fieldName) {
    this.props.removeCustomField(fieldName);
  },

  handleChange: function (fieldName, event) {
    this.props.onChange(event.target.value, fieldName);
  },

  _renderFields: function () {
    return this.props.fields.map(function (field, key) {
      var value = this.props.data[field.name];
      var type = field.name == 'password' ? 'password' : 'text';

      return (
        <FieldInput
          key={key}
          type={type}
          name={field.name}
          value={value}
          placeholder={field.type}
          required={field.required ? 'required' : false}
          removeField={this.removeCustomField}
          isCustom={field.isCustom ? 'isCustom' : false}
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

module.exports = Data;
