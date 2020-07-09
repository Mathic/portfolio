$(document).ready(function(){
  var ul = document.getElementById('chartChooser');
  var target = '';
  var climateLabels = []
  var climateData1 = climateData2 = []

  if(target == '') {
    callAjax('api/chart/year_avg_temp', yearlyAvgTemp);
    $(document.getElementById('api/chart/year_avg_temp')).addClass('active')
  }

  ul.onclick = function(event) {
    target = event.target.id;
    var a = document.getElementById(target);
    $(a).addClass('active').parent().siblings().children().removeClass('active');

    switch(target) {
      case 'api/chart/year_avg_temp':
        callAjax(target, yearlyAvgTemp);
        break;
      case 'api/chart/ottawa_seasonal':
        callAjax(target, ottawaSeasonal);
        break;
      case 'api/chart/victoria_seasonal':
        callAjax(target, victoriaSeasonal);
        break;
      case 'api/chart/ottawa_monthly':
        callAjax(target, ottawaMonthly);
        break;
      case 'api/chart/victoria_monthly':
        callAjax(target, victoriaMonthly);
        break;
    };
  };

  function callAjax(endpoint, callFunction) {
    $("#loading-alert").show();
    $.ajax({
      method: "GET",
      url: endpoint,
      success: function(data){
        climateLabels = data.climate_labels
        climateData1 = data.climate_data1
        climateData2 = data.climate_data2

        if(data.climate_data3 !== undefined) {
          climateData3 = data.climate_data3
          climateData4 = data.climate_data4
        }

        ottawaAverage = data.ottawa_average
        victoriaAverage = data.victoria_average

        callFunction();
        $("#loading-alert").hide();
        $("#success-alert").show();
        $("#success-alert").fadeOut(3250);
      },
      error: function(error_data){
        console.log("error")
      }
    });
  };

  function yearlyAvgTemp(){
    var trace1 = {
      x: climateLabels,
      y: climateData1,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Ottawa',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(221, 48, 17)",
        "width": 2
      },
    }

    var trace3 = {
      x: climateLabels,
      y: climateData2,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Victoria',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(255,140,0)",
        "width": 2
      },
    }

    var data = [trace1, trace3];

    var layout = {
      title: "Yearly average temperature compared to the 1926-2018 Ottawa average (at " + ottawaAverage + "°C) and the 1926-2018 Victoria average (at " + victoriaAverage + "°C)",
      legend: {
        title: 'Year',
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Temperature difference (°C)',
        rangemode: 'nonnegative',
        range: [-2.5, 2.5],
        nticks: 5,
      }
    };

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };

  function yearlyAvgPrec(){
    var trace2 = {
      x: climateLabels,
      y: climateData1,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Ottawa',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(48, 41, 173)",
        "width": 2
      },
    }

    var trace4 = {
      x: climateLabels,
      y: climateData2,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Victoria',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(100,118,248)",
        "width": 2
      },
    }

    var data = [trace2, trace4];

    var layout = {
      title: "Yearly average precipitation in mm",
      legend: {
        title: 'Year',
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Precipitation (mm)',
        side: 'left',
        overlaying: 'y',
        range: [0, 140],
        nticks: 11,
      }
    };

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };

  function ottawaSeasonal(){
    plotlySeasonal("Ottawa Seasonal Average Precipitation 1926-2018");
  };

  function victoriaSeasonal(){
    plotlySeasonal("Victoria Seasonal Average Precipitation 1926-2018");
  };

  function ottawaMonthly(){
    plotlyClimateDiagram("Ottawa Climate Diagram - monthly averages from 1926-2018");
  };

  function victoriaMonthly(){
    plotlyClimateDiagram("Victoria Climate Diagram - monthly averages from 1926-2018");
  };

  function plotlyClimateDiagram(title){
    var trace1 = {
      x: climateLabels,
      y: climateData1,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Temperature',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(221, 48, 17)",
        "width": 2
      },
    }

    var trace2 = {
      x: climateLabels,
      y: climateData2,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Precipitation',
      yaxis: 'y2',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(48, 41, 173)",
        "width": 2
      },
    }

    var data = [trace1, trace2];

    var layout = {
      title: title,
      legend: {
        title: 'Month',
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Temperature (C)',
        rangemode: 'nonnegative',
        range: [-20, 80],
        nticks: 11,
      },
      yaxis2: {
        title: 'Precipitation (mm)',
        side: 'right',
        overlaying: 'y',
        range: [-40, 160],
        nticks: 11,
      }
    };

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  };

  function plotlySeasonal(title) {
    var trace1 = {
      x: climateLabels,
      y: climateData1,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Winter',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(158,202,225)",
        "width": 2
      },
    }

    var trace2 = {
      x: climateLabels,
      y: climateData2,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Spring',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(107,174,214)",
        "width": 2
      },
    }

    var trace3 = {
      x: climateLabels,
      y: climateData3,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Summer',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(49,130,189)",
        "width": 2
      },
    }

    var trace4 = {
      x: climateLabels,
      y: climateData4,
      type: 'scatter',
      mode: 'lines+markers',
      name: 'Fall',
      marker: {
        size: 8,
        "dash": "solid",
        "color": "rgb(8,81,156)",
        "width": 2
      },
    }

    var data = [trace1, trace2, trace3, trace4];

    var layout = {
      title: title,
      legend: {
        title: 'Year',
        x: 0.25,
        y: 1
      },
      yaxis: {
        title: 'Precipitation (mm)',
        side: 'left',
        overlaying: 'y',
        range: [0, 200],
        nticks: 11,
      }
    };

    Plotly.newPlot('plotlyChart', data, layout, {responsive: true})
  }
});
