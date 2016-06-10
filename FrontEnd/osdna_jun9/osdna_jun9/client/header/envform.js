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

    "click .envList": function(event,template){
        event.preventDefault();
        menuTree.init();
        Router.go('home',{_id:1},{query: 'env='+event.target.innerText});
        Meteor.setTimeout( function(){
            window.location.reload();
        },100);
    },
};

Template.envForm.helpers({
    selected:function(){
        var controller = Iron.controller();
        var envName = controller.state.get('envName');
        if(envName == this.name){
            console.log(this.name + 'selected');
            return 'selected';
        }
    },

    envList:function(){
        //return Environments.find({type:"environment"});
        return Environments.find({});
    },
});