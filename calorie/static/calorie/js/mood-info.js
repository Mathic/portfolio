$(document).ready(function() {
  var mood_table = $('#mood-datepicker').attr("mood-table-url");
  load_mood_form();
  $("#mood-target").load(mood_table);

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
    var mood_table = $('#mood-datepicker').attr("mood-table-url");
    $.ajax({
      url: url,
      data: {
        'date_picked': date
      },
      success: function (data) {
        $("#load-mood-info").html(data);
        $("#mood-target").load(mood_table);
        console.log('success');
      },
      error: function(data) {
        console.log('fail');
      }
    });
  }
};
