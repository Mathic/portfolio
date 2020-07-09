var $th = $('.tableFixHead').find('thead th')
$('.tableFixHead').on('scroll', function() {
  $th.css('transform', 'translateY('+ this.scrollTop +'px)');
});

$("#inputName").change(function () {
  var url = $("#climateForm").attr("data-years-url");
  var nameId = $(this).val();
  if(nameId == '---------') {
    $("#inputYear").hide();
  } else {
    $.ajax({
      url: url,
      data: {
        'student': nameId
      },
      success: function (data) {
        $("#inputYear").html(data);
        $("#inputYear").show();
      },
      error: function(data) {
        $("#inputYear").hide();
      }
    });
  }
});
