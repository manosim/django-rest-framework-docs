var jsonPP = {
  // Thanks to http://jsfiddle.net/unlsj/
  replacer: function (match, pIndent, pKey, pVal, pEnd) {
     var key = '<span class=json-key>';
     var val = '<span class=json-value>';
     var str = '<span class=json-string>';
     var r = pIndent || '';
     if (pKey)
        r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
     if (pVal)
        r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
     return r + (pEnd || '');
  },
  prettyPrint: function (obj) {
     var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
     return JSON.stringify(obj, null, 3)
        .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
        .replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(jsonLine, this.replacer);
  }
};

$( document ).ready(function() {

  var resetForm = function () {
    $('#methods').empty();
    $('#fields').empty();
  };

  var cleanResponse = function () {
    $('#responseStatusCode').removeClass(function (index, css) {
      return (css.match (/(^|\s)label-\S+/g) || []).join(' ');
    });
    $('#responseStatusText').text( '' );
    $('#responseData').html( '' );
  };

  var setResponse = function (response) {
    // Status Code
    var statusCodeFirstChar = String(response.status).charAt(0);
    var statusCodeClass;

    switch (parseInt(statusCodeFirstChar)) {
      case 1:
        statusCodeClass = 'label-info';
        break;
      case 2:
        statusCodeClass = 'label-success';
        break;
      case 3:
        statusCodeClass = 'label-warning';
        break;
      case 4:
        statusCodeClass = 'label-danger';
        break;
      case 5:
        statusCodeClass = 'label-primary';
        break;
    }

    $('#responseStatusCode').text(response.status);
    $('#responseStatusCode').addClass(statusCodeClass);

    $('#responseStatusText').text(response.statusText.toLowerCase());
    $('#responseData').html(jsonPP.prettyPrint(response.responseJSON));
  };

  var getFormData = function () {
    var data = {};

    $( '#fields .form-group' ).each(function(){
      var input = $(this).find( 'input' );
      var name = input.attr( 'id' );
      var value = input.val();
      data[name] = value;
    })

    return data;
  };

  var makeRequest = function () {
    // Clean the response
    cleanResponse();

    var url = $('#requestForm #urlInput').val();
    var method = $("#methods").find( ".active" ).text();
    var data = getFormData();
    $.ajax({
      url: url,
      method: method,
      context: document.body,
      data: data
    }).always(function(data, textStatus, jqXHR) {

      if (textStatus != 'success') {
        jqXHR = data;
      }
      setResponse(jqXHR);
    });
  };

  var _setupMethods = function (methods) {
    // List Methods (Radio Buttons)
    // FIXME: Use regex - convert to JSON
    var methods = methods.replace("[", "").replace("]", "").replace(/'/g, "").replace(/\s/g, "").split(',');
    $.each( methods, function( i, method ) {
      var methodClass = "btn btn-sm method " + method.toLowerCase();
      $('#methods').append("<button type='button' class='" + methodClass + "'>" + method + "</button>");
    });

    // Make the first method active
    $('#methods').children(".btn").first().addClass( 'active' );

    $("#methods .method").on('click', function (evt) {
      // Remove 'active' from all methods
      $("#methods .method").removeClass( 'active' );
      // Add 'active' to the clicked button
      $(this).addClass( 'active' );
    });
  };

  var _setupFields = function (fields) {
    $.each( fields, function( i, field ) {
      var label = field.name.replace('_', ' ');
      $('#fields').append("" +
        '<div class="form-group">' +
          '<label for="field' + field.name + '" class="col-sm-4 control-label">' + label + '</label>' +
          '<div class="col-sm-8">' +
          '<input type="text" class="form-control input-sm" id="' + field.name + '" placeholder="' + field.type + '">' +
          '</div>' +
        '</div>' +
      "");
    });
  };

  var setupForm = function (data) {
    // Reset Form - Remove Methods & Fields
    resetForm();

    $('#urlInput').val(data.path);

    _setupMethods(data.methods);
    _setupFields(data.fields);

    $('#requestForm').submit(function (e) {
      // Prevent Submit
      e.preventDefault();

      // Make Request
      makeRequest(data);
    });
  };

  $('.plug').bind('click', function(evt) {
    // Prevent the accordion from collapsing
    evt.stopPropagation();
    evt.preventDefault();

    // Open Modal
    $('#liveAPIModal').modal('toggle');

    // Setup the form
    var data = $(this).data();
    setupForm(data);
  });

});
