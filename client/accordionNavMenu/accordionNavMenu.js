/*
  Template Component: accordionNavMenu
 */

(function () {

Template.accordionNavMenu.rendered = function () {
  /* accordion menu plugin*/
  ;(function($, window, document, undefined) {
    var pluginName = "accordion";
    var defaults = {
      speed: 200,
      showDelay: 0,
      hideDelay: 0,
      singleOpen: true,
      clickEffect: true,
      indicator: 'submenu-indicator-minus',
      subMenu: 'submenu',
      event: 'click touchstart' // click, touchstart
    };
    function Plugin(element, options) {
      this.element = element;
      this.settings = $.extend({}, defaults, options);
      this._defaults = defaults;
      this._name = pluginName;
      // todo: refactor remove all plugin. moved to components internal operation.
      // this.init();
    }
    $.extend(Plugin.prototype, {
      init: function() {
        this.openSubmenu();
        this.submenuIndicators();
        if (defaults.clickEffect) {
          this.addClickEffect();
        }
      },
      openSubmenu: function() {
        $(this.element).children("ul").find("li").bind(defaults.event, function(e) {
          e.stopPropagation();
          e.preventDefault();
          var $subMenus = $(this).children("." + defaults.subMenu);
          var $allSubMenus = $(this).find("." + defaults.subMenu);
          if ($subMenus.length > 0) {
            if ($subMenus.css("display") == "none") {
              $subMenus.slideDown(defaults.speed).siblings("a").addClass(defaults.indicator);
              if (defaults.singleOpen) {
                $(this).siblings().find("." + defaults.subMenu).slideUp(defaults.speed)
                    .end().find("a").removeClass(defaults.indicator);
              }
              return false;
            } else {
              $(this).find("." + defaults.subMenu).delay(defaults.hideDelay).slideUp(defaults.speed);
            }
            if ($allSubMenus.siblings("a").hasClass(defaults.indicator)) {
              $allSubMenus.siblings("a").removeClass(defaults.indicator);
            }
          }
          window.location.href = $(this).children("a").attr("href");
        });
      },

      submenuIndicators: function() {
        if ($(this.element)
              .find("." + defaults.subMenu)
                .length > 0) {

          $(this.element)
            .find("." + defaults.subMenu)
            .siblings("a")
              .append("<span class='submenu-indicator'>+</span>");
        }
      },

      addClickEffect: function() {
        var ink, d, x, y;
        $(this.element).find("a").bind("click touchstart", function(e) {
          $(".ink").remove();
          if ($(this).children(".ink").length === 0) {
            $(this).prepend("<span class='ink'></span>");
          }
          ink = $(this).find(".ink");
          ink.removeClass("animate-ink");
          if (!ink.height() && !ink.width()) {
            d = Math.max($(this).outerWidth(), $(this).outerHeight());
            ink.css({
              height: d,
              width: d
            });
          }
          x = e.pageX - $(this).offset().left - ink.width() / 2;
          y = e.pageY - $(this).offset().top - ink.height() / 2;
          ink.css({
            top: y + 'px',
            left: x + 'px'
          }).addClass("animate-ink");
        });
      }
    });
    $.fn[pluginName] = function(options) {
      this.each(function() {
        if (!$.data(this, "plugin_" + pluginName)) {
          $.data(this, "plugin_" + pluginName, new Plugin(this, options));
        }
      });
      return this;
    };
  })(jQuery, window, document);

  jQuery(document).ready(function($) {
    // refactored to component
    //$("#left-nav-menu").accordion();

    $(".toggleGraph").click(function() {
      $('.mainContentData').toggle();
      $('#dgraphid').toggle();
    });

    /* refactord to component

    $("#aggregate-WebEx-RTP-SSD-Aggregate-node-24").click(function() {
      $('.mainContentData').hide();
      $('#dgraphid').show();

      //$('#dgraphid').css('display','block');
      //$('.flex-box-3 main-layout-no-nav').html('<div id=""></div>');
      Session.set('currNodeId','node-24');
      var graphData = d3Graph.getGraphData('node-24');
      d3Graph.updateNetworkGraph(graphData);
      //$("body").scrollTop(0);
    });
    
    $(".genGraphClick").click(function() {
      //console.log($(this).attr('objid'));
      $('.mainContentData').hide();
      $('#dgraphid').show();
      //$('#dgraphid').css('display','block');
      //$('.flex-box-3 main-layout-no-nav').html('<div id=""></div>');
      Session.set('currNodeId',$(this).attr('objid'));
      var graphData = d3Graph.getGraphDataByClique($(this).attr('objid'));
      d3Graph.updateNetworkGraph(graphData);
    });
    */

    $(".colors a").click(function() {
      if ($(this).attr("class") != "default") {
        $("#left-nav-menu").removeClass();
        $("#left-nav-menu").addClass("menu").addClass($(this).attr("class"));
      } else {
        $("#left-nav-menu").removeClass();
        $("#left-nav-menu").addClass("menu");
      }
    });

    if(Session.get('envGraph')=="true"){
      Meteor.setTimeout(function(){
        $("#aggregate-WebEx-RTP-SSD-Aggregate-node-24").click();
      },1000);

    }
  });
/*
  Meteor.setTimeout(function(){
    var controller = Iron.controller();
    var envGraph = controller.state.get('envGraph');
    if(envGraph=="true"){
      $("#aggregate-WebEx-RTP-SSD-Aggregate-node-24").click();
    }
  },10000)
*/

};

/* 
 * Events
 */

Template.accordionNavMenu.events({
  "click .test": function(event,template){
    console.log("HERE!!!!");
    console.log(event.target.innerText);
  },
});
Template.accordionNavMenu.helpers({
  envName: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return envName;
  },
  test: function(){
    console.log("HERE!!!!");
  }
});

// refactored to accordionTreeNode
/*
Template.accordionNavMenuTreeNodeTemplate.helpers({
  hasClique: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    if(Inventory.find({parent_id: this.id, parent_type:this.type,environment: envName,clique:true,show_in_tree:true}).count() > 0){
      console.log("clique=True");
      return "true";
    }
    else{
      return "false";
    }

  },
  hasChildren: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return Inventory.find({parent_id: this.id, parent_type:this.type,environment: envName,show_in_tree:true}).count() > 0;
  },
  children: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return Inventory.find({parent_id: this.id ,parent_type:this.type,environment: envName,show_in_tree:true});
  }
});
*/

Template.d3graph.rendered = function () {
  d3Graph.creategraphdata();
  //var graphData = getGraphData("node-25");
  //updateNetworkGraph(graphData);
  var initgraph = true;
  Tracker.autorun(function () {
    var nodeId = Session.get('currNodeId');
    if(nodeId){
      var graphData = d3Graph.getGraphDataByClique(nodeId);
      if(!initgraph){
        //d3Graph.start();
        d3Graph.updateNetworkGraph(graphData);
      }
    }
    initgraph = false;
  });

};

})();
