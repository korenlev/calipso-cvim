/* Created by oashery on 3/2/2016. Modified by sisakov on 9/7/2016*/
import * as R from 'ramda';
import { Environments } from '/imports/api/environments/environments';

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

Router.route('/scans-list', function () {
  this.render('ScansList');
}, { });

Router.route('/link-types-list', function () {
  this.render('LinkTypesList');
}, { });

Router.route('/link-type', function () {
  this.render('LinkType');
}, { });

Router.route('/clique-types-list', function () {
  this.render('CliqueTypesList');
}, { });

Router.route('/clique-type', function () {
  this.render('CliqueType');
}, { });

Router.route('/clique-constraints-list', function () {
  this.render('CliqueConstraintsList');
}, { });

Router.route('/clique-constraint', function () {
  this.render('CliqueConstraint');
}, { });

Router.route('/messages-list', function () {
  this.render('MessagesList');
}, { });

Router.route('/message', function () {
  let that = this;
  let params = that.params;
  let query = params.query;

  this.render('Message', {
    data: function () {
      return {
        id: query.id,
        action: query.action
      };
    }
  });
}, { });

Router.route('/user-list', function () {
  this.render('UserList');
}, { });

Router.route('/user', function () {
  this.render('User');
}, { });

Router.route('/scanning-request', function () {
  this.render('ScanningRequest');
}, {
  name: 'scanning-request'
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
    if (this.ready()){ 
      this.render('RegionDashboard', {
        data: function () {
          return {
            id_path: this.params.query.id_path
          };
        }
      }); 
    }
    else { this.render('loading'); }
  }
});

Router.route('project', {
  name: 'project',
  path: '/project',
  action: function () {
    if (this.ready()){ 
      this.render('ProjectDashboard', {
        data: function () {
          return {
            id_path: this.params.query.id_path
          };
        }
      }); 
    }
    else { this.render('loading'); }
  }
});

Router.route('zone', {
  name: 'zone',
  path: '/zone',
  action: function () {
    if (this.ready()){ 
      this.render('ZoneDashboard', {
        data: function () {
          return {
            id_path: this.params.query.id_path
          };
        }
      }); 
    } 
    else { this.render('loading'); }
  }
});

Router.route('host', {
  name: 'host',
  path: '/host',
  action: function () {
    if (this.ready()){ 
      this.render('HostDashboard', {
        data: function () {
          return {
            id_path: this.params.query.id_path
          };
        }
      }); 
    }
    else{ this.render('loading'); }
  }
});

Router.route('aggregate', {
  name: 'aggregate',
  path: '/aggregate',
  action: function () {
    if (this.ready()){ 
      this.render('AggregateDashboard', {
        data: function () {
          return {
            id_path: this.params.query.id_path
          };
        }
      }); 
    }
    else{ this.render('loading'); }
  }
});


Router.route('migrateEnvToUserId', {
  name: 'migrateEnvToUserId',
  where: 'server',
  action: function () {
    console.log('migrate env to user id');

    //let request = this.request;
    let response = this.response;

    let envs = Environments.find({}).fetch();
    R.forEach((env) => {
      console.log('found env: ' + env.name + ' ' + R.toString(env._id));

      let user = Meteor.users.findOne({ username: env.user }); 
      if (R.isNil(user)) { 
        console.log('not migrated: ' + env.name);    
        return;
      }
      console.log('found user: ' + user._id + ' ' + user.username);    

      try {
        let result = Environments.update(
          { _id : env._id },
          {
            $set: {
              user: user._id
            }
          });
        console.log('result', R.toString(result));
        console.log('migrated: ' + env.name);    
      } catch(e) {
        console.log('exception', R.toString(e));
      }

    }, envs);

    response.end('migration end');
  }
});
