Template.project.helpers({
    getProjectName: function () {
        return Session.get('projectName') || "No Project";
    }
});


Template.project.rendered = function(){


}