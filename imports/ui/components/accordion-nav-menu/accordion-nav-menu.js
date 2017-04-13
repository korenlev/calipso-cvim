/*
  Template Component: accordionNavMenu
 */

/* eslint indent: "off" */

import * as R from 'ramda';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';
//import { Tracker } from 'meteor/tracker';
//import { Session } from 'meteor/session';
import { InventoryTreeNodeBehavior } from '/imports/ui/lib/inventory-tree-node-behavior';
//import { Inventory } from '/imports/api/inventories/inventories';
import { SimpleSchema } from 'meteor/aldeed:simple-schema';

import '/imports/ui/components/tree-node/tree-node';
import '/imports/ui/components/accordionTreeNode/accordionTreeNode';
import '/imports/ui/components/d3graph/d3graph';

import { store } from '/imports/ui/store/store'; import { setCurrentNodeFromTreeControl } from '/imports/ui/actions/navigation';
import { 
  resetEnvTreeNodeChildren, 
  addUpdateEnvTreeNode,
  startOpenEnvTreeNode,
  endOpenEnvTreeNode,
  startCloseEnvTreeNode,
  endCloseEnvTreeNode,
} from '/imports/ui/actions/environment-panel.actions';

import './accordion-nav-menu.html';

Template.accordionNavMenu.onCreated(function () {
  let instance = this;

  instance.state = new ReactiveDict();
  instance.state.setDefault ({
    selectedNode: null,
    rootNode: null,
    mainNode: null
  });

  instance.autorun(function () {
    let data = Template.currentData();

    new SimpleSchema({
      envName: { type: String },
      childNodeRequested: { type: Object, blackbox: true, optional: true },
      onNodeClick: { type: Function },
      onToggleGraphReq: { type: Function }
    }).validate(data);

    instance.subscribe('inventory?id', data.envName);

    let rootNode = {
      id: data.envName,
      type: 'environment',
      name: data.envName,
      environment: data.envName
    };
    instance.state.set('rootNode', rootNode);
  });

  instance.storeUnsubscribe = store.subscribe(() => {
    let state = store.getState();
    let nodeChain = state.api.navigation.current;
    let selectedNode = null;
    if (nodeChain.length > 1) {
      selectedNode = R.slice(1, Infinity, nodeChain);
    }
    instance.state.set('selectedNode', selectedNode);

    let mainNode = store.getState().components.environmentPanel.treeNode;
    instance.state.set('mainNode', mainNode);
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

    /*
    $('.toggleGraph').click(function() {
      $('.mainContentData').toggle();
      $('#dgraphid').toggle();
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
  'click .sm-toggle-graph-button': function (_event, _instance) {
    let data = Template.currentData();
    data.onToggleGraphReq();
  }
});

/*
 * Helpers
 */

Template.accordionNavMenu.helpers({
  rootNode: function () {
    let instance = Template.instance();
    return instance.state.get('rootNode');
  },

  mainNode: function () {
    let instance = Template.instance();
    return instance.state.get('mainNode');
  },

  createNodeArgs: function (node) {
    let instance = Template.instance();
    let selectedNode = instance.state.get('selectedNode');
    let onNodeClick = Template.currentData().onNodeClick;

    return {
      node: node,
      showOpen: true,
      selectedNode: selectedNode,
      onClick: function (childNode) {
        store.dispatch(setCurrentNodeFromTreeControl(childNode));
        onNodeClick(childNode);
        },
    };
  },

  argsTreeNode: function (node) {
    //let instance = Template.instance();
    //let treeNode = store.getState().components.environmentPanel.treeNode;

    return {
      behavior: InventoryTreeNodeBehavior,
      showDetailsLine: false,
      openState: node.openState,
      node: node.nodeInfo,
      children: node.children,
      onResetChildren: function (nodePath) {
        store.dispatch(resetEnvTreeNodeChildren(R.tail(nodePath)));
      },
      onChildRead: function (nodePath, childNode) {
        store.dispatch(addUpdateEnvTreeNode(R.tail(nodePath), childNode));
      },
      onStartOpenReq: (nodePath) => {
        store.dispatch(startOpenEnvTreeNode(R.tail(nodePath)));
      },
      onOpeningDone: (nodePath) => {
        store.dispatch(endOpenEnvTreeNode(R.tail(nodePath)));
      },
      onStartCloseReq: (nodePath) => {
        store.dispatch(startCloseEnvTreeNode(R.tail(nodePath)));
      },
      onClosingDone: (nodePath) => {
        store.dispatch(endCloseEnvTreeNode(R.tail(nodePath)));
      },
    };
  }
});
