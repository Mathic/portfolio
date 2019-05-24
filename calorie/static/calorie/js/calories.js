$(function () {
  $("#datepicker").datepicker({maxDate: '0'});
});

$("#datepicker").change(function() {
  var date = $(this).val();
  if(date !== '') {
    var url = $(this).attr("date-picked-url");
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
});

$('#id_mood_time').timepicker();

$('#id_time_awake').datetimepicker();

$('#id_time_slept').datetimepicker();
