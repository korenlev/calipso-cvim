Template.wizard.rendered = function(){
  
  $('.btnNext').click(function(){
    $('.nav-tabs > .active').next('li').find('a').trigger('click');
  });

  $('.btnPrevious').click(function(){
    $('.nav-tabs > .active').prev('li').find('a').trigger('click');
  });
  
};


Template.wizard.helpers({
  updateRecipeId : function () {
    return this._id;
  },
  user : function () {
    return Meteor.user().username;
  }
});

Template.wizard.events({
  'click .toast' : function () {
    toastr.success('Have fun storming the castle!', 'Open Stack server says')
  },
  'click .fa-trash' : function () {
    Meteor.call('deleteRecipe', this._id);
  }
});
