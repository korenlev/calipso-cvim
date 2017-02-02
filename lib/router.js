/* Created by oashery on 3/2/2016. Modified by sisakov on 9/7/2016*/

if (Meteor.isClient){
  Accounts.onLogin(function () {
    Router.go('/dashboard');
  });

  Accounts.onLogout(function () {
    Router.go('/');
  });
}

Router.configure({
  layoutTemplate: 'main',
  loadingTemplate: 'loading'
});

Router.route('/', {
  name: 'landing',
  path: '/',
  action: function () {
    if (Meteor.userId()) {
      Router.go('/dashboard');
    }
    if (this.ready())
      this.layout('landing');
    else
        this.render('loading');
  }
});

Router.route('home', {
  path: '/home',
  /* refactor to component. home not in use ?
  waitOn: function () {
      return Meteor.subscribe('inventory');
  },
  */
  action: function () {
    if (this.ready()){

      this.state.set('envName', this.params.query.env);
      /*
                  if(query){
                          //return Inventory.find({$where: "this.id_path.match('^/WebEX-Mirantis@Cisco/')"});
                          console.log(query);
                          this.render('home', {
                              data: function () {
                                  return Inventory.find({environment: query, parent_id: query});
                              }
                          });
                          //
                  }
      */

  // if the sub handle returned from waitOn ready() method returns
  // true then we're ready to go ahead and render the page.
      this.render('home');

    }
    else{
      this.render('loading');
    }
  }
});

Router.route('getstarted', {
  name: 'getstarted',
  path: '/getstarted'
});

Router.route('/wizard', function () {
  this.state.set('env', null);
  Session.set('wizardEnv', null);
  this.render('EnvironmentWizard');
});

Router.route('/wizard/:env', function () {
  this.state.set('env', this.params.env);
  Session.set('wizardEnv', this.params.env);
  this.render('EnvironmentWizard');
});

Router.route('/scanning-request', function () {
  this.render('ScanningRequest');
}, {
  name: 'scanning-request.insert'
});

Router.route('dashboard', {
  name: 'dashboard',
  path: '/dashboard',
  /* eyaltask
  waitOn: function () {
          return Meteor.subscribe('inventory');
  },
  */
  action: function () {
    if (this.ready()){
      this.render('dashboard');

    }
    else{
      this.render('loading');
    }
  }
});

Router.route('enviroment', {
  name: 'enviroment',
  path: '/enviroment',
  /*
  waitOn: function () {
      if(this.params.query.env){
          return Meteor.subscribe('inventoryByEnv',this.params.query.env);
      }
      else{
          return Meteor.subscribe('inventory');
      }

  },
  */
  action: function () {
    if (this.ready()){

      this.state.set('envName', this.params.query.env);
      if(this.params.query.graph == 'true'){
        Session.set('envGraph', this.params.query.graph);
      }
      else{
        Session.set('envGraph', 'false');
      }

      this.render('Environment');

    }
    else{
      this.render('loading');
    }
  }
});

Router.route('region', {
  name: 'region',
  path: '/region',
  action: function () {
    if (this.ready()){ this.render('RegionDashboard'); }
    else{ this.render('loading'); }
  }
});

Router.route('project', {
  name: 'project',
  path: '/project',
  action: function () {
    if (this.ready()){ this.render('ProjectDashboard'); }
    else{ this.render('loading'); }
  }
});

Router.route('zone', {
  name: 'zone',
  path: '/zone',
  action: function () {
    if (this.ready()){ this.render('ZoneDashboard'); }
    else{ this.render('loading'); }
  }
});

Router.route('host', {
  name: 'host',
  path: '/host',
  action: function () {
    if (this.ready()){ this.render('HostDashboard'); }
    else{ this.render('loading'); }
  }
});

Router.route('aggregate', {
  name: 'aggregate',
  path: '/aggregate',
  action: function () {
    if (this.ready()){ this.render('AggregateDashboard'); }
    else{ this.render('loading'); }
  }
});

// Router.route('d3plusgraph', {
//     path: '/d3plus'
// });

// Router.route('threeTest', {
//     path: '/three',
// });

// Router.route('threeTest2', {
//     path: '/three2',
// });
