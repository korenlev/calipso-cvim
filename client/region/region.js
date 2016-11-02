import '/imports/ui/components/accordionNavMenu/accordionNavMenu';

Template.region.rendered = function(){


}
Template.region.helpers({
   getRegionName: function () {
       return Session.get('regionName') || "No Region";
   },
});
