/*
  Template Component: accordionNavMenu
 */

/* eslint indent: "off" */

import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
//import { Tracker } from 'meteor/tracker';
//import { Session } from 'meteor/session';

import '/client/imports/accordionTreeNode/accordionTreeNode';
import '/imports/ui/components/d3graph/d3graph';

import { store } from '/client/imports/store';
import { setCurrentNodeFromTreeControl } from '/client/imports/actions/navigation';

(function () {

Template.accordionNavMenu.onCreated(function () {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault ({
    selectedNode: null
  });

  instance.autorun(function () {
    let controller = Iron.controller();
    let envName = controller.state.get('envName');

    instance.subscribe('inventory?id', envName);
  });

  instance.storeUnsubscribe = store.subscribe(() => {
    let state = store.getState();
    let nodeChain = state.api.navigation.current;
    let selectedNode = null;
    if (nodeChain.length > 1) {
      selectedNode = R.slice(1, Infinity, nodeChain);
    }
    instance.state.set('selectedNode', selectedNode);
  });

  let selectedNode = null;
  let state = store.getState();
  let nodeChain = state.api.navigation.current;
  if (nodeChain.length > 1) {
      selectedNode = R.slice(1, Infinity, nodeChain);
  } else {
    selectedNode = null;
  }

  instance.state.set('selectedNode', selectedNode);
});


Template.accordionNavMenu.rendered = function () {
  /* accordion menu plugin*/
  (function($, window//, document//, undefined
  ) {
    var pluginName = 'accordion';
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
        $(this.element).children('ul').find('li').bind(defaults.event, function(e) {
          e.stopPropagation();
          e.preventDefault();
          var $subMenus = $(this).children('.' + defaults.subMenu);
          var $allSubMenus = $(this).find('.' + defaults.subMenu);
          if ($subMenus.length > 0) {
            if ($subMenus.css('display') == 'none') {
              $subMenus.slideDown(defaults.speed).siblings('a').addClass(defaults.indicator);
              if (defaults.singleOpen) {
                $(this).siblings().find('.' + defaults.subMenu).slideUp(defaults.speed)
                    .end().find('a').removeClass(defaults.indicator);
              }
              return false;
            } else {
              $(this).find('.' + defaults.subMenu).delay(defaults.hideDelay).slideUp(defaults.speed);
            }
            if ($allSubMenus.siblings('a').hasClass(defaults.indicator)) {
              $allSubMenus.siblings('a').removeClass(defaults.indicator);
            }
          }
          window.location.href = $(this).children('a').attr('href');
        });
      },

      submenuIndicators: function() {
        if ($(this.element)
              .find('.' + defaults.subMenu)
                .length > 0) {

          $(this.element)
            .find('.' + defaults.subMenu)
            .siblings('a')
              .append('<span class="submenu-indicator">+</span>');
        }
      },

      addClickEffect: function() {
        var ink, d, x, y;
        $(this.element).find('a').bind('click touchstart', function(e) {
          $('.ink').remove();
          if ($(this).children('.ink').length === 0) {
            $(this).prepend('<span class="ink"></span>');
          }
          ink = $(this).find('.ink');
          ink.removeClass('animate-ink');
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
          }).addClass('animate-ink');
        });
      }
    });
    $.fn[pluginName] = function(options) {
      this.each(function() {
        if (!$.data(this, 'plugin_' + pluginName)) {
          $.data(this, 'plugin_' + pluginName, new Plugin(this, options));
        }
      });
      return this;
    };
  })(jQuery, window, document);

  jQuery(document).ready(function($) {
    // refactored to component
    //$("#left-nav-menu").accordion();

    $('.toggleGraph').click(function() {
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

    $('.colors a').click(function() {
      if ($(this).attr('class') != 'default') {
        $('#left-nav-menu').removeClass();
        $('#left-nav-menu').addClass('menu').addClass($(this).attr('class'));
      } else {
        $('#left-nav-menu').removeClass();
        $('#left-nav-menu').addClass('menu');
      }
    });

    /* refactored to component environment
    if(Session.get('envGraph')=="true"){
      Meteor.setTimeout(function(){
        $("#aggregate-WebEx-RTP-SSD-Aggregate-node-24").click();
      },1000);

    }
    */
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


Template.accordionNavMenu.onDestroyed(function () {
  let instance = this;
  instance.storeUnsubscribe();
});

/*
 * Events
 */

Template.accordionNavMenu.events({
});

/*
 * Helpers
 */

Template.accordionNavMenu.helpers({
  envName: function(){
    var controller = Iron.controller();
    var envName = controller.state.get('envName');
    return envName;
  },

  rootNode: function () {
    var controller = Iron.controller();
    var envName = controller.state.get('envName');

    return {
      id: envName,
      type: 'environment',
      name: envName
    };
    //return Inventory.findOne({ id: envName });
  },

  createNodeArgs: function (node) {
    let instance = Template.instance();
    let selectedNode = instance.state.get('selectedNode');

    return {
      node: node,
      showOpen: true,
      selectedNode: selectedNode,
      onClick: function (childNode) {
        store.dispatch(setCurrentNodeFromTreeControl(childNode));
        },
    };
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

})();
