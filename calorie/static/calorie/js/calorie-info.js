$(document).ready(function() {
  load_calorie_form();

  $(function () {
    $("#calorie-datepicker").datepicker({maxDate: '0'});
  });

  $("#calorie-datepicker").change(function() {
    load_calorie_form();
  });
});

function load_calorie_form() {
  var date = $('#calorie-datepicker').val();
  if(date !== '') {
    var url = $('#calorie-datepicker').attr("date-picked-url");
    $.ajax({
      url: url,
      data: {
        'date_picked': date
      },
      success: function (data) {
        $("#load-calorie-info").html(data);
        console.log('success');
      },
      error: function(data) {
        console.log('fail');
      }
    });
  }
};
