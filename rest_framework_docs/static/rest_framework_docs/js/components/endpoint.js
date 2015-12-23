var _ = require('underscore');
var slugify = require('underscore.string/slugify');
var React = require('react');
var Modal = require('react-modal');

var Endpoint = React.createClass({
  getInitialState: function() {
    return {
      accordionOpen: false,
      modalOpen: false
    };
  },

  setAccordionStyle: function () {
    var box = this.refs.accordionContent.getBoundingClientRect();

    this.setState({
      accordionStyle: {
        height: box.height
      }
    });
  },

  toggleAccordion: function () {
    if (this.state.accordionOpen) {
      window.removeEventListener('resize', this.setAccordionStyle);
    } else {
      window.addEventListener('resize', this.setAccordionStyle);
    }

    this.setAccordionStyle();

    this.setState({
      accordionOpen: !this.state.accordionOpen
    });
  },

  toggleModal: function (e) {
    e.stopPropagation();
    this.setState({
      modalOpen: !this.state.modalOpen
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
                <li key='plug' className={'method plug'}>
                  <i className='fa fa-plug' onClick={this.toggleModal} />
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div className="panel-collapse collapse"
          style={this.state.accordionOpen ? this.state.accordionStyle : {height: 0}}>
          <div className="panel-body" ref="accordionContent">
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

        <Modal
          isOpen={this.state.modalOpen}
          onRequestClose={this.toggleModal}

          style={{
            content : {
                top                   : '50%',
                left                  : '50%',
                right                 : 'auto',
                bottom                : 'auto',
                marginRight           : '-50%',
                transform             : 'translate(-50%, -50%)'
              }
          }} >

          <div className="modal-content">
            <div className="modal-header">
              <button type="button" className="close" onClick={this.toggleModal}>
                <span aria-hidden="true">&times;</span>
                <span className="sr-only">Close</span>
              </button>
              <h4 className="modal-title">Modal title</h4>
            </div>
            <div className="modal-body">
              <h4>Really long content...</h4>
              <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus</p>
              <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus</p>
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-default" onClick={this.toggleModal}>Close</button>
              <button type="button" className="btn btn-primary" onClick={this.handleSaveClicked}>Save changes</button>
            </div>
          </div>

        </Modal>

      </div>
    );
  }
});

module.exports = Endpoint;
