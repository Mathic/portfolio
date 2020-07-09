$("#inputYear").change(function () {
  var url = $("#dataMonth").attr("data-months-url");
  var year = $(this).val();

  if(year == '---------') {
    $("#months").hide();
  } else {
    $.ajax({
      url: url,
      data: {
        'year': year
      },
      success: function (data) {
        $("#months").html(data);
        $("#months").show();
      },
      error: function(data) {
        $("#months").hide();
      }
    });
  }
});
