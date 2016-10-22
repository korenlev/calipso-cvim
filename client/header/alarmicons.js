/*
 * Template Component: alarmIcons
 */

import '/imports/ui/components/breadcrumb/breadcrumb';

(function () {

/*
 * Lifecycle
 */
 
Template.alarmIcons.onCreated(function () {
  let instance = this;

  instance.autorun(function () {
    instance.subscribe('messages?level', 'notify');
    instance.subscribe('messages?level', 'warn');
    instance.subscribe('messages?level', 'error');
  });
});

/*
 * Helpers
 */  

Template.alarmIcons.helpers({
    notificationsCount: function(){
        return Messages.find({level:'notify'}).count();
    },
    warningsCount: function(){
        return Messages.find({level:'warn'}).count();
    },
    errorsCount: function(){
        return Messages.find({level:'error'}).count();
    },
});

})();
