var _ = require('underscore');
var slugify = require('underscore.string/slugify');
var React = require('react');

var Endpoint = React.createClass({
  getInitialState: function() {
    return {
      open: false
    };
  },

  toggleAccordion: function () {
    this.setState({
      open: !this.state.open
    });
  },

  _renderMethods: function () {
    var methods = this.props.endpoint.allowed_methods;

    return _.map(methods, function (method) {
      var slug = slugify(method, 'group');
      return <li key={slug} className={'method ' + slug}>{method}</li>
    })
  },

  _renderFields: function () {
    var fields = this.props.endpoint.fields;

    return _.map(fields, function (field) {
      return (
        <li key={field.name} className='field'>
          {field.name}: {field.type}
          {field.required ?(
            <span className="label label-primary label-required" title="Required">R</span>
          ) : null}
        </li>
      )
    })
  },

  render: function () {
    var endpoint = this.props.endpoint;
    var isOpen = this.state.open ? ' in' : '';

    return (
      <div className='panel panel-default endpoint' onClick={this.toggleAccordion}>

        <div className='panel-heading'>
          <div className='row'>
            <div className='col-md-7'>
              <h4 className='panel-title title'>
                <i className='fa fa-link'></i> {this.props.group}{endpoint.path}
              </h4>
            </div>

            <div className='col-md-5 text-right'>
              <ul className='list-inline methods'>
                {this._renderMethods()}
                <li key='plug' className={'method plug'}><i className='fa fa-plug' /></li>
              </ul>
            </div>
          </div>
        </div>

        <div className={'panel-collapse collapse' + isOpen}>
          <div className="panel-body">
            {endpoint.docstring ? (
              <p className='lead'>{endpoint.docstring}</p>
            ) : null}

            {endpoint.errors ? (
              <div className="alert alert-danger" role="alert">
                Oops! There was something wrong with {endpoint.errors}. Please check your code.
              </div>
            ) : null}

            {endpoint.fields.length ? (
              <div>
                <p className="fields-desc">Fields:</p>
                <ul className="list fields">
                  {this._renderFields()}
                </ul>
              </div>
            ) : <div><p className="fields-desc">No Fields.</p></div>}
          </div>
        </div>
      </div>
    );
  }
});

module.exports = Endpoint;
