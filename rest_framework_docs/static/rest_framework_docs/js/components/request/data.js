var React = require('react');

var FieldText = require('../fields/text');

var Data = React.createClass({
  getInitialState: function() {
    return {
      fields: this.props.fields
    };
  },

  componentWillReceiveProps: function(nextProps) {
    this.setState({
      fields: nextProps.fields
    });
  },

  removeCustomField: function (fieldName) {
    this.props.removeCustomField(fieldName);
  },

  handleChange: function (fieldName, event) {
    this.props.onChange(event.target.value, fieldName);
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
        onChange={this.handleChange.bind(this, field.name)} />
    );
  },

  _renderFields: function () {
    return this.state.fields.map(function (field, key) {
      switch (field.type) {
      case ('CharField'):
        return this._renderTextInput(field, key);
      }
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
