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
Template.enviroment.helpers({
    envName: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return envName;
    },
    instancesCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'instance'}).count();
    },
    vservicesCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'vservice'}).count();
    },
    hostsCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'host'}).count();
    },
    vconnectorsCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'vconnector'}).count();
    },
    projectsCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'project'}).count();
    },
    regoinsCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'region'}).count();
    },
    regoins: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'region'});
    },
    projects: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.find({environment: envName,type:'project'});
    },

    regionslastScanned: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.findOne({environment: envName,type:'region'}).last_scanned;
    },
    projectslastScanned: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Inventory.findOne({environment: envName,type:'project'}).last_scanned;
    },
    notificationsCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Messages.find({environment: envName,level:'notify'}).count();
    },
    warningsCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Messages.find({environment: envName,level:'warn'}).count();
    },
    errorsCount: function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        return Messages.find({environment: envName,level:'error'}).count();
    },

});
