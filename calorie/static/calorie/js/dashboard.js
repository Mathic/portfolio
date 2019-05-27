$(document).ready(function() {
  var days = []
  var cals_in = cals_out = moods = []

  callAjax('api/chart/health_graph', dailyGraph);

  function callAjax(endpoint, callFunction) {
    // $("#loading-alert").show();
    $.ajax({
      method: "GET",
      url: endpoint,
      success: function(data){
        days = data.days
        cals_in = data.cals_in
        cals_out = data.cals_out
        weight = data.weight
        moods = data.moods
        $('#totalDeficit').text(data.deficit)
        $('#dailyDeficit').text(data.daily)
        $('#weeklyDeficit').text(data.weekly)
        $('#bmr').text(data.bmr)

        callFunction();
        // $("#loading-alert").hide();
        // $("#success-alert").show();
        // $("#success-alert").fadeOut(3250);
      },
      error: function(error_data){
        console.log("error")
      }
    });
  };

  function dailyGraph(){
    var trace1 = {
      x: days,
      y: cals_in,
      type: 'bar',
      name: 'Calories In',
      marker: {
        color: 'rgba(219, 64, 82, 0.7)',
        line: {
          color: 'rgba(219, 64, 82, 1.0)',
          width: 1.5
        }
      },
    };

    var trace2 = {
      x: days,
      y: cals_out,
      type: 'bar',
      name: 'Calories Out',
      marker: {
        color: 'rgba(158,202,225,0.7)',
        line: {
          color: 'rgba(8,48,107,1.0)',
          width: 1.5
        }
      },
    };

    var trace3 = {
      x: days,
      y: weight,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Weight',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(255,140,0)",
        "width": 2
      },
      yaxis: 'y2',
    };

    var data = [trace1, trace2, trace3];

    var layout = {
      title: "Health Graph",
      legend: {
        title: 'Year',
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Calories',
        side: 'left',
        autorange: true,
        nticks: 11,
      },
      yaxis2: {
        title: 'Weight',
        overlaying: 'y',
        autorange: true,
        side: 'right'
      }
    };

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };
});
