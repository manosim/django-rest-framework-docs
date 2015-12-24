$( document ).ready(function() {

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

      $('#responseStatusCode').text(response.status);
      $('#responseStatusText').text(response.statusText);
      $('#responseData').text(JSON.stringify(response.responseJSON, undefined, 2));

      console.log(response);
      console.log(response.responseJSON);
    });
  };

  var setupForm = function (data) {
    console.log('------');
    console.log(data.path);
    console.log('------');

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
