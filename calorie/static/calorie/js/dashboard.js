$(document).ready(function() {
  var days = []
  var cals_in = cals_out = moods = []
  // $("#loading-alert").show();

  $.ajax({
    method: "GET",
    url: 'api/chart/calorie_intake',
    success: function(data){
      days = data.days
      cals_in = data.cals_in
      cals_out = data.cals_out
      cal_neg = data.cal_neg
      cal_pos = data.cal_pos
      weight = data.weight
      moods = data.moods
      $('#totalDeficit').text(data.deficit)
      $('#dailyDeficit').text(data.daily)
      $('#weeklyDeficit').text(data.weekly)
      $('#bmr').text(data.bmr)
      calorieIntakeGraph();
      calorieWeightGraph();
      // $("#loading-alert").hide();
      // $("#success-alert").show();
      // $("#success-alert").fadeOut(3250);
    },
    error: function(error_data){
      console.log("error")
      // $("#loading-alert").hide();
    }
  });

  function calorieIntakeGraph(endpoint) {
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

    var data = [trace1, trace2];

    var layout = {
      title: "Calorie Intake",
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
    };

    Plotly.newPlot('calorieIntake', data, layout, {responsive: true})
  };

  function calorieWeightGraph(endpoint) {
    var trace1 = {
      x: days,
      y: cal_neg,
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
      y: cal_pos,
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

    var trace4 = {
      x: days,
      y: moods,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Mood',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(34,139,34)",
        "width": 2
      },
      yaxis: 'y3',
    };

    var data = [trace1, trace2, trace3, trace4];

    var layout = {
      title: "Net Calories",
      barmode: 'stack',
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
      },
      yaxis3: {
        title: 'Mood',
        overlaying: 'y',
        autorange: true,
        side: 'left'
      }
    };

    Plotly.newPlot('calorieWeight', data, layout, {responsive: true})
  }
});
