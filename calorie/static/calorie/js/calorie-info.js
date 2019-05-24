$("#savecalorie").click(function() {
  var date = $("#datepicker").val();

  if(date !== '') {
    console.log('save clicked');
    var url = $("#datepicker").attr("save-calorie-url");
    console.log(date);

    $.ajax({
      method: "POST",
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      url: url,
      data: {
        'date_picked': date
      },
      success: function (data) {
        console.log('savecalorie')
        console.log('success');
      },
      error: function(data) {
        console.log('fail savecalorie');
      }
    });
  }
});
