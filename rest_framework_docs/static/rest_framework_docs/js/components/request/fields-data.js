var _ = require('underscore');
var React = require('react');

var Input = require('../helpers/input');

var FieldsData = React.createClass({

  handleChange: function (value) {
    this.props.onChange(value);
  },

  _renderFields: function () {
    return _.each(this.props.fields, function (field, key) {
      console.log('======');
      console.log(key);
      console.log(field);

      return (
        <Input key={key} name={field.name} value='' placeholder={field.type} required={field.required} onChange={this.handleChange} />
      );
    }, this )
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
