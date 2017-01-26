/*
 * Template Component: ListInfoBox 
 */
    
//import { Meteor } from 'meteor/meteor'; 
import { Template } from 'meteor/templating';
//import { ReactiveDict } from 'meteor/reactive-dict';
import * as R from 'ramda';
        
import './list-info-box.html';     
    
/*  
 * Lifecycles
 */   
  
Template.ListInfoBox.onCreated(function() {
});  

/*
Template.ListInfoBox.rendered = function() {
};  
*/

/*
 * Events
 */

Template.ListInfoBox.events({
});
   
/*  
 * Helpers
 */

Template.ListInfoBox.helpers({    
  itemsCount: function () {
    let instance = Template.instance();
    return instance.data.list.count();
  },

  argsSelect: function (list, listItemFormat) {
    let instance = Template.instance();

    let options = R.map((listItem) => {
      return { 
        label: listItem[listItemFormat.label], 
        value: listItem[listItemFormat.value] 
      };
    }, list.fetch());

    return {
      values: [],
      options: options,
      setModel: function (val) {
        instance.data.onItemSelected(val);
      }
    };
  }
});


