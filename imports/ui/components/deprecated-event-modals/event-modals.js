/////////////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2017 Koren Lev (Cisco Systems), Yaron Yogev (Cisco Systems) and others /
//                                                                                      /
// All rights reserved. This program and the accompanying materials                     /
// are made available under the terms of the Apache License, Version 2.0                /
// which accompanies this distribution, and is available at                             /
// http://www.apache.org/licenses/LICENSE-2.0                                           /
/////////////////////////////////////////////////////////////////////////////////////////
/*
 * Template Component: eventModals
 */

import { Template } from 'meteor/templating';
import { Messages } from '/imports/api/messages/messages';

import './event-modals.html';

/*
 * Lifecycle
 */

Template.eventModals.onCreated(function () {
  let instance = this;

  instance.autorun(function () {
    // global messages
    instance.subscribe('messages?level', 'notify');
    instance.subscribe('messages?level', 'warn');
    instance.subscribe('messages?level', 'error');
    // per environment messages: since we have global, no need.
  });
});

/*
 * Helpers
 */

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
