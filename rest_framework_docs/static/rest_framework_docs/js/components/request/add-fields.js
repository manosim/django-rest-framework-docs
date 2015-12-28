var React = require('react');

var Header = require('../helpers/header');

var AddFieldsForm = React.createClass({

  getInitialState: function() {
    return {
      fieldName: ''
    };
  },

  addField: function () {
    this.props.onAdd(this.state.fieldName);
  },

  handleChange: function (event) {
    this.setState({
      fieldName: event.target.value
    });
  },

  render: function () {
    return (
      <div>
        <Header title='Add Extra Fields' />

        <div className='form-group'>
          <label className='col-sm-4 control-label'>Add Field</label>
          <div className="col-sm-6">
            <input
              type='text'
              className='form-control input-sm'
              placeholder='Field Name (ie. email_address)'
              onChange={this.handleChange}
              value={this.state.fieldName} />
          </div>
          <div className="col-sm-2">
            <button
              type="button"
              className='btn btn-sm btn-block btn-primary'
              onClick={this.addField}>
              Add
            </button>
          </div>
        </div>
      </div>
    );
  }
});

module.exports = AddFieldsForm;
