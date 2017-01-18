/*
 * Template Component: envForm
 */

import { Environments } from '/imports/api/environments/environments';

(function () {

/*
 * Lifecycle methods
 */

Template.envForm.onCreated(function () {
  var instance = this;

  instance.autorun(function() {
    instance.subscribe("environments_config");
  });
});

/*
 * Events
 */  

Template.envForm.events = {
    // "change #envList": function(event,template){
    //     //console.log(event.target.value);
    //     //Session.set("currEnv",event.target.value);
    //     event.preventDefault();
    //     menuTree.init();
    //     Router.go('home',{_id:1},{query: 'env='+event.target.value});
    //     Meteor.setTimeout( function(){
    //         window.location.reload();
    //     },100);


    //     //Router.go('/home?'+'env='+event.target.value);
    //     //window.location.reload();
    //     //$( '#menu' ).multilevelpushmenu( 'redraw' );
    //     //menuTree.init();
    // },

    //"click .envList": function(event,template){
        //event.preventDefault();
        //menuTree.init();
        //Router.go('enviroment',{_id:1},{query: 'env='+event.target.innerText});

    //},
};

/*
 * Helpers
 */   

Template.envForm.helpers({
    envName: function () {
        var controller = Iron.controller();
        var envName = controller.state.get('envName') || "My Environments";

        return envName;
    },
    envList: function () {
        //return Environments.find({type:"environment"});
        return Environments.find({});
    },
});

})();
