var _ = require('underscore');
var React = require('react');

var Endpoints = React.createClass({

  getInitialState: function () {
    return {
      url: '',
      loading: false,
      submitDisabled: true,
      errors: false
    };
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

  onSubmit: function (e) {
    e.preventDefault();

    var self = this;
    var slug = this.state.url.split('.com/')[1];
    var regex = /^(http[s]?:\/\/)?(www\.)?github\.com\/([^\/]+)\/([^\/]+)[\/]?.*$/i;
    var result = regex.exec(this.state.url);

    if (!result) {
      this.setState({
        errors: true
      });
      return;
    }

    var owner = result[3];
    var repo = result[4];

    this.setState({
      loading: true,
      submitDisabled: true,
      errors: false
    });

    apiRequests
      .get('https://api.github.com/repos/' + owner + '/' + repo)
      .end(function (err, response) {
        if (response && response.ok) {
          setTimeout(function() {
            self.setState({
              errors: false,
              loading: false,
              submitDisabled: false
            });
            self.props.gotDetails(response.body);
          }, 1000);
        } else {
          self.setState({
            errors: true,
            loading: false,
            submitDisabled: false
          });
        }
      });
  },

  render: function () {
    return (
      <div className='autogenerator'>
        <h4>Generate from GitHub Repository</h4>
        <Loading className="loading" shouldShow={this.state.loading}>
          <h3>Grabbing your repository details from <i className='fa fa-github' /></h3>
        </Loading>
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
