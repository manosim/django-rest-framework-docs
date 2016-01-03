var React = require('react');

var FieldText = require('../fields/text');
var FieldBoolean = require('../fields/boolean');
var Header = require('../helpers/header');
var RequestUtils = require('../../utils/request');

var Data = React.createClass({
  removeCustomField: function (fieldName) {
    this.props.removeCustomField(fieldName);
  },

  handleBooleanChange: function (fieldName, value) {
    this.props.onChange(value, fieldName);
  },

  handleTextChange: function (fieldName, event) {
    this.props.onChange(event.target.value, fieldName);
  },

  _renderBooleanField: function (field, key) {
    var value = this.props.data[field.name];

    return (
      <FieldBoolean
        key={key}
        name={field.name}
        value={value}
        required={field.required ? 'required' : false}
        removeField={this.removeCustomField}
        isCustom={field.isCustom ? 'isCustom' : false}
        onChange={this.handleBooleanChange.bind(this, field.name)} />
    );
  },

  _renderTextInput: function (field, key) {
    var value = this.props.data[field.name];
    var type = field.name == 'password' ? 'password' : 'text';
    return (
      <FieldText
        key={key}
        type={type}
        name={field.name}
        value={value}
        placeholder={field.type}
        required={field.required ? 'required' : false}
        removeField={this.removeCustomField}
        isCustom={field.isCustom ? 'isCustom' : false}
        onChange={this.handleTextChange.bind(this, field.name)} />
    );
  },

  _renderFields: function () {
    return this.props.fields.map(function (field, key) {

      switch (field.type) {
      case ('BooleanField'):
        return this._renderBooleanField(field, key);

      case ('CharField'):
      default:
        return this._renderTextInput(field, key);

      }
    }, this);
  },

  render: function () {
    if (!RequestUtils.shouldIncludeData(this.props.method)) {
      return null;
    }

    return (
      <div>
        {this.props.fields.length ? <Header title='Data' /> : null}
        {this._renderFields()}
      </div>
    );
  }
});

module.exports = Data;
