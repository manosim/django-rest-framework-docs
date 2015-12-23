var _ = require('underscore');
var slugify = require('underscore.string/slugify');
var React = require('react');

var Endpoint = React.createClass({
  _renderMethods: function () {
    var methods = this.props.endpoint.allowed_methods;

    return _.map(methods, function (method) {
      var slug = slugify(method, 'group');
      return <li key={slug} className={'method ' + slug}>{method}</li>
    })
  },

  render: function () {
    var endpoint = this.props.endpoint;

    return (
      <div className='panel panel-default endpoint'>

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
              </ul>
            </div>
          </div>
        </div>

        // Body
      </div>
    );
  }
});

module.exports = Endpoint;
