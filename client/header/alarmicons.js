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