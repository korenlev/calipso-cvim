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
            this.render('landing');
        else
            this.render('loading');
    }
});

Router.route('home', {
    path: '/home',
    waitOn: function () {
        return Meteor.subscribe('inventory');
    },
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

Router.route('wizard', {
    name: 'wizard',
    path: '/wizard'
});

Router.route('dashboard', {
    name: 'dashboard',
    path: '/dashboard'
});

Router.route('enviroment', {
    name: 'enviroment',
    path: '/enviroment'
});

Router.route('region', {
    name: 'region',
    path: '/region'
});

Router.route('project', {
    name: 'project',
    path: '/project'
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