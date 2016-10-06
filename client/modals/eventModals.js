Template.eventModals.helpers({
    messagesNotifications : function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        if(envName != undefined){
            return Messages.find({level:'notify',environment: envName});
        }
    },
    messagesWarnings : function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        if(envName != undefined){
            return Messages.find({level:'warn',environment: envName});
        }
    },
    messagesErrors : function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        if(envName != undefined){
            return Messages.find({level:'error',environment: envName});
        }
    },
    messagesNotificationsGlobal : function(){
        return Messages.find({level:'notify'});
    },
    messagesWarningsGlobal : function(){
        return Messages.find({level:'warn'});
    },
    messagesErrorsGlobal : function(){
        return Messages.find({level:'error'});
    },
});