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
      console.log('load_calorie_form success');
    },
    error: function(data) {
      console.log('fail');
    }
  });
};
