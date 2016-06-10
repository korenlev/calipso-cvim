Template.enviroment.rendered = function(){

  $.getScript('https://www.gstatic.com/charts/loader.js', function() {
    google.charts.load('current', {'packages':['gauge', 'line']});
  google.charts.setOnLoadCallback(drawLine);
    

  function drawLine() {
      var data = new google.visualization.DataTable();
      data.addColumn('number', 'Traffic Webex');
      data.addColumn('number', 'Traffic metapod');
      data.addColumn('number', 'Some other Traffic');
      data.addColumn('number', 'Some other Traffic');

      data.addRows([
        [1,  37.8, 80.8, 41.8],
        [2,  30.9, 69.5, 32.4],
        [3,  25.4,   57, 25.7],
        [4,  11.7, 18.8, 32.5],
        [5,  11.9, 25.6, 10.4],
        [6,   68.8, 13.6,  27.7],
        [7,   7.6, 42.3,  9.6],
        [8,  12.3, 29.2, 10.6],
        [9,  16.9, 42.9, 14.8]
      ]);

  var options = {
    chart: {
      title: 'Network traffic throughput',
      subtitle: 'in Mbps'
    }
  };

  var chart = new google.charts.Line(document.getElementById('curve_chart'));

  chart.draw(data, options);
  }
  });

}