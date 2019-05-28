$(document).ready(function() {
  $("#add-exercise-button").click(function() {
    load_exercise_form();
  });
});


function load_exercise_form() {
  var exercise_table = $('#calories-form').attr("calorie-exercise-url");
  $.ajax({
    url: exercise_table,
    // data: {
    //   'date_picked': date
    // },
    success: function (data) {
      // $("#load-calorie-info").html(data);
      $(".add-exercise").hide()
      $("#exercise-target").prepend().load(exercise_table);
      console.log('load_exercise_form success');
    },
    error: function(data) {
      console.log('fail');
    }
  });
};
