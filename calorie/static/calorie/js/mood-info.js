$(document).ready(function() {
  load_mood_form();

  $(function () {
    $("#mood-datepicker").datepicker({maxDate: '0'});
  });

  $("#mood-datepicker").change(function() {
    load_mood_form();
  });
});

function load_mood_form() {
  var date = $('#mood-datepicker').val();
  if(date !== '') {
    var url = $('#mood-datepicker').attr("date-picked-url");
    $.ajax({
      url: url,
      data: {
        'date_picked': date
      },
      success: function (data) {
        $("#load-mood-info").html(data);
        console.log('success');
      },
      error: function(data) {
        console.log('fail');
      }
    });
  }
};
