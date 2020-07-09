$("#addData").click(function() {
  var url = $("#climateForm").attr("data-save-url");
  var radioValue = $("input[name='sourceRadios']:checked").val();
  var climates = [];
  temps = []
  precips = []
  var student_id = $("#inputName").val();

  $('#inputYear').find('.data').each(function() {
    if($(this).val() == ""){
      climates.push($(this).text());
    } else {
      climates.push($(this).val());
    }
  });

  $('#inputYear').find('.temps').each(function() {
    temps.push($(this).val())
  });

  $('#inputYear').find('.precips').each(function() {
    precips.push($(this).val())
  });

  $.ajax({
    url: url,
    data: {
      'climates': climates,
      'temps': temps,
      'precips': precips,
      'source': radioValue,
      'student_id': student_id
    },
    success: function (data) {
      $("#success-alert").show();
      $("#success-alert").fadeOut(3250);
    },
    error: function() {
      $("#error-alert").show();
      $("#error-alert").fadeOut(3250);
    }
  });
});
