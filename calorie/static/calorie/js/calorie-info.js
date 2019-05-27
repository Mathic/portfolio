$(document).ready(function() {
  var calorie_table = $('#calorie-datepicker').attr("calorie-table-url");
  load_calorie_form();
  $("#calorie-target").load(calorie_table);

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
    var calorie_table = $('#calorie-datepicker').attr("calorie-table-url");
    $.ajax({
      url: url,
      data: {
        'date_picked': date
      },
      success: function (data) {
        $("#load-calorie-info").html(data);
        $("#calories-target").load(calorie_table);
        console.log('success');
      },
      error: function(data) {
        console.log('fail');
      }
    });
  }
};
