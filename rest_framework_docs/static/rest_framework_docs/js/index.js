$( document ).ready(function() {

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
    $('#responseData').text(JSON.stringify(response.responseJSON, undefined, 2));

    // console.log(response);
    // console.log(response.responseJSON);
  };

  var makeRequest = function () {
    var url = $('#requestForm #urlInput').val();
    var method = 'POST';

    $.ajax({
      url: url,
      method: method,
      context: document.body,
      data: {
        username: 'test',
        password: 'test'
      }
    }).always(function(response) {
      setResponse(response);
    });
  };

  var setupForm = function (data) {
    $('#urlInput').val(data.path);

    $('#requestForm').submit(function (e) {
      // Prevent Submit
      e.preventDefault();

      // Make Request
      makeRequest(data);
    });
  };

  $('.plug').bind('click', function(e) {
    // Prevent the accordion from collapsing
    e.stopPropagation();

    // Open Modal
    $('#liveAPIModal').modal('toggle');

    // Setup the form
    var data = $(this).data();
    setupForm(data);
  });

});
