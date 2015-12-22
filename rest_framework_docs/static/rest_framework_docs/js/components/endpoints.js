var _ = require('underscore');
var React = require('react');

var Endpoints = React.createClass({

  getInitialState: function () {
    return {
      loading: false,
    };
  },

  componentDidMount: function() {
    console.log(this.props.endpoints);
  },

  handleChange: function (key, event) {
    if (!event.target.value) {
      this.setState({
        url: event.target.value,
        submitDisabled: true
      });
    } else {
      this.setState({
        url: event.target.value,
        submitDisabled: false
      });
    }
  },

  render: function () {
    return (
      <div className='autogenerator'>
        <h4>Generate from GitHub Repository</h4>
        <form className='form'>
          <div className='form-group'>
            <input type='text' id='name' className='form-control input-lg' value={this.state.url} placeholder='Example: http://www.github.com/atom/electron' onChange={this.handleChange.bind(this, 'url')} />
          </div>
          {this.state.errors ? (
            <div className='alert alert-danger'>Oops! Something went wrong and we could not auto-populate the form.</div>
          ) : null}
          <button className='btn btn-primary btn-lg btn-block' disabled={this.state.submitDisabled} onClick={this.onSubmit}>Populate Submision Form</button>
         </form>
      </div>
    );
  }
});

module.exports = Endpoints;
