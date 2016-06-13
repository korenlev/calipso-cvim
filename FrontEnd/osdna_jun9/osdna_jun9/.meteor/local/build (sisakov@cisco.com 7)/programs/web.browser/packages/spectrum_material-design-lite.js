//////////////////////////////////////////////////////////////////////////
//                                                                      //
// This is a generated file. You can view the original                  //
// source in your browser if your browser supports source maps.         //
// Source maps are supported by all recent versions of Chrome, Safari,  //
// and Firefox, and by Internet Explorer 11.                            //
//                                                                      //
//////////////////////////////////////////////////////////////////////////


(function () {

/* Imports */
var Meteor = Package.meteor.Meteor;
var global = Package.meteor.global;
var meteorEnv = Package.meteor.meteorEnv;

(function(){

///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                           //
// packages/spectrum_material-design-lite/packages/spectrum_material-design-lite.js                          //
//                                                                                                           //
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                             //
(function(){                                                                                                 // 1
                                                                                                             // 2
///////////////////////////////////////////////////////////////////////////////////////////////////////      // 3
//                                                                                                   //      // 4
// packages/spectrum:material-design-lite/material.js                                                //      // 5
//                                                                                                   //      // 6
///////////////////////////////////////////////////////////////////////////////////////////////////////      // 7
                                                                                                     //      // 8
/**                                                                                                  // 1    // 9
 * @license                                                                                          // 2    // 10
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 3    // 11
 *                                                                                                   // 4    // 12
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 5    // 13
 * you may not use this file except in compliance with the License.                                  // 6    // 14
 * You may obtain a copy of the License at                                                           // 7    // 15
 *                                                                                                   // 8    // 16
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 9    // 17
 *                                                                                                   // 10   // 18
 * Unless required by applicable law or agreed to in writing, software                               // 11   // 19
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 12   // 20
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 13   // 21
 * See the License for the specific language governing permissions and                               // 14   // 22
 * limitations under the License.                                                                    // 15   // 23
 */                                                                                                  // 16   // 24
                                                                                                     // 17   // 25
/**                                                                                                  // 18   // 26
 * A component handler interface using the revealing module design pattern.                          // 19   // 27
 * More details on this pattern design here:                                                         // 20   // 28
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 21   // 29
 * @author Jason Mayes.                                                                              // 22   // 30
 */                                                                                                  // 23   // 31
/* exported componentHandler */                                                                      // 24   // 32
var componentHandler = (function() {                                                                 // 25   // 33
  'use strict';                                                                                      // 26   // 34
                                                                                                     // 27   // 35
  var registeredComponents_ = [];                                                                    // 28   // 36
  var createdComponents_ = [];                                                                       // 29   // 37
  var downgradeMethod_ = 'mdlDowngrade_';                                                            // 30   // 38
  var componentConfigProperty_ = 'mdlComponentConfigInternal_';                                      // 31   // 39
                                                                                                     // 32   // 40
  /**                                                                                                // 33   // 41
   * Searches registered components for a class we are interested in using.                          // 34   // 42
   * Optionally replaces a match with passed object if specified.                                    // 35   // 43
   * @param {string} name The name of a class we want to use.                                        // 36   // 44
   * @param {object} optReplace Optional object to replace match with.                               // 37   // 45
   * @return {object | false}                                                                        // 38   // 46
   * @private                                                                                        // 39   // 47
   */                                                                                                // 40   // 48
  function findRegisteredClass_(name, optReplace) {                                                  // 41   // 49
    for (var i = 0; i < registeredComponents_.length; i++) {                                         // 42   // 50
      if (registeredComponents_[i].className === name) {                                             // 43   // 51
        if (optReplace !== undefined) {                                                              // 44   // 52
          registeredComponents_[i] = optReplace;                                                     // 45   // 53
        }                                                                                            // 46   // 54
        return registeredComponents_[i];                                                             // 47   // 55
      }                                                                                              // 48   // 56
    }                                                                                                // 49   // 57
    return false;                                                                                    // 50   // 58
  }                                                                                                  // 51   // 59
                                                                                                     // 52   // 60
  /**                                                                                                // 53   // 61
   * Searches existing DOM for elements of our component type and upgrades them                      // 54   // 62
   * if they have not already been upgraded.                                                         // 55   // 63
   * @param {string} jsClass the programatic name of the element class we need                       // 56   // 64
   * to create a new instance of.                                                                    // 57   // 65
   * @param {string} cssClass the name of the CSS class elements of this type                        // 58   // 66
   * will have.                                                                                      // 59   // 67
   */                                                                                                // 60   // 68
  function upgradeDomInternal(jsClass, cssClass) {                                                   // 61   // 69
    if (jsClass === undefined && cssClass === undefined) {                                           // 62   // 70
      for (var i = 0; i < registeredComponents_.length; i++) {                                       // 63   // 71
        upgradeDomInternal(registeredComponents_[i].className,                                       // 64   // 72
            registeredComponents_[i].cssClass);                                                      // 65   // 73
      }                                                                                              // 66   // 74
    } else {                                                                                         // 67   // 75
      if (cssClass === undefined) {                                                                  // 68   // 76
        var registeredClass = findRegisteredClass_(jsClass);                                         // 69   // 77
        if (registeredClass) {                                                                       // 70   // 78
          cssClass = registeredClass.cssClass;                                                       // 71   // 79
        }                                                                                            // 72   // 80
      }                                                                                              // 73   // 81
                                                                                                     // 74   // 82
      var elements = document.querySelectorAll('.' + cssClass);                                      // 75   // 83
      for (var n = 0; n < elements.length; n++) {                                                    // 76   // 84
        upgradeElementInternal(elements[n], jsClass);                                                // 77   // 85
      }                                                                                              // 78   // 86
    }                                                                                                // 79   // 87
  }                                                                                                  // 80   // 88
                                                                                                     // 81   // 89
  /**                                                                                                // 82   // 90
   * Upgrades a specific element rather than all in the DOM.                                         // 83   // 91
   * @param {HTMLElement} element The element we wish to upgrade.                                    // 84   // 92
   * @param {string} jsClass The name of the class we want to upgrade                                // 85   // 93
   * the element to.                                                                                 // 86   // 94
   */                                                                                                // 87   // 95
  function upgradeElementInternal(element, jsClass) {                                                // 88   // 96
    // Only upgrade elements that have not already been upgraded.                                    // 89   // 97
    var dataUpgraded = element.getAttribute('data-upgraded');                                        // 90   // 98
                                                                                                     // 91   // 99
    if (dataUpgraded === null || dataUpgraded.indexOf(jsClass) === -1) {                             // 92   // 100
      // Upgrade element.                                                                            // 93   // 101
      if (dataUpgraded === null) {                                                                   // 94   // 102
        dataUpgraded = '';                                                                           // 95   // 103
      }                                                                                              // 96   // 104
      element.setAttribute('data-upgraded', dataUpgraded + ',' + jsClass);                           // 97   // 105
      var registeredClass = findRegisteredClass_(jsClass);                                           // 98   // 106
      if (registeredClass) {                                                                         // 99   // 107
        // new                                                                                       // 100  // 108
        var instance = new registeredClass.classConstructor(element);                                // 101  // 109
        instance[componentConfigProperty_] = registeredClass;                                        // 102  // 110
        createdComponents_.push(instance);                                                           // 103  // 111
        // Call any callbacks the user has registered with this component type.                      // 104  // 112
        registeredClass.callbacks.forEach(function(callback) {                                       // 105  // 113
          callback(element);                                                                         // 106  // 114
        });                                                                                          // 107  // 115
                                                                                                     // 108  // 116
        if (registeredClass.widget) {                                                                // 109  // 117
          // Assign per element instance for control over API                                        // 110  // 118
          element[jsClass] = instance;                                                               // 111  // 119
        }                                                                                            // 112  // 120
      } else {                                                                                       // 113  // 121
        throw 'Unable to find a registered component for the given class.';                          // 114  // 122
      }                                                                                              // 115  // 123
                                                                                                     // 116  // 124
      var ev = document.createEvent('Events');                                                       // 117  // 125
      ev.initEvent('mdl-componentupgraded', true, true);                                             // 118  // 126
      element.dispatchEvent(ev);                                                                     // 119  // 127
    }                                                                                                // 120  // 128
  }                                                                                                  // 121  // 129
                                                                                                     // 122  // 130
  /**                                                                                                // 123  // 131
   * Registers a class for future use and attempts to upgrade existing DOM.                          // 124  // 132
   * @param {object} config An object containing:                                                    // 125  // 133
   * {constructor: Constructor, classAsString: string, cssClass: string}                             // 126  // 134
   */                                                                                                // 127  // 135
  function registerInternal(config) {                                                                // 128  // 136
    var newConfig = {                                                                                // 129  // 137
      'classConstructor': config.constructor,                                                        // 130  // 138
      'className': config.classAsString,                                                             // 131  // 139
      'cssClass': config.cssClass,                                                                   // 132  // 140
      'widget': config.widget === undefined ? true : config.widget,                                  // 133  // 141
      'callbacks': []                                                                                // 134  // 142
    };                                                                                               // 135  // 143
                                                                                                     // 136  // 144
    registeredComponents_.forEach(function(item) {                                                   // 137  // 145
      if (item.cssClass === newConfig.cssClass) {                                                    // 138  // 146
        throw 'The provided cssClass has already been registered.';                                  // 139  // 147
      }                                                                                              // 140  // 148
      if (item.className === newConfig.className) {                                                  // 141  // 149
        throw 'The provided className has already been registered';                                  // 142  // 150
      }                                                                                              // 143  // 151
    });                                                                                              // 144  // 152
                                                                                                     // 145  // 153
    if (config.constructor.prototype                                                                 // 146  // 154
        .hasOwnProperty(componentConfigProperty_)) {                                                 // 147  // 155
      throw 'MDL component classes must not have ' + componentConfigProperty_ +                      // 148  // 156
          ' defined as a property.';                                                                 // 149  // 157
    }                                                                                                // 150  // 158
                                                                                                     // 151  // 159
    var found = findRegisteredClass_(config.classAsString, newConfig);                               // 152  // 160
                                                                                                     // 153  // 161
    if (!found) {                                                                                    // 154  // 162
      registeredComponents_.push(newConfig);                                                         // 155  // 163
    }                                                                                                // 156  // 164
  }                                                                                                  // 157  // 165
                                                                                                     // 158  // 166
  /**                                                                                                // 159  // 167
   * Allows user to be alerted to any upgrades that are performed for a given                        // 160  // 168
   * component type                                                                                  // 161  // 169
   * @param {string} jsClass The class name of the MDL component we wish                             // 162  // 170
   * to hook into for any upgrades performed.                                                        // 163  // 171
   * @param {function} callback The function to call upon an upgrade. This                           // 164  // 172
   * function should expect 1 parameter - the HTMLElement which got upgraded.                        // 165  // 173
   */                                                                                                // 166  // 174
  function registerUpgradedCallbackInternal(jsClass, callback) {                                     // 167  // 175
    var regClass = findRegisteredClass_(jsClass);                                                    // 168  // 176
    if (regClass) {                                                                                  // 169  // 177
      regClass.callbacks.push(callback);                                                             // 170  // 178
    }                                                                                                // 171  // 179
  }                                                                                                  // 172  // 180
                                                                                                     // 173  // 181
  /**                                                                                                // 174  // 182
   * Upgrades all registered components found in the current DOM. This is                            // 175  // 183
   * automatically called on window load.                                                            // 176  // 184
   */                                                                                                // 177  // 185
  function upgradeAllRegisteredInternal() {                                                          // 178  // 186
    for (var n = 0; n < registeredComponents_.length; n++) {                                         // 179  // 187
      upgradeDomInternal(registeredComponents_[n].className);                                        // 180  // 188
    }                                                                                                // 181  // 189
  }                                                                                                  // 182  // 190
                                                                                                     // 183  // 191
  /**                                                                                                // 184  // 192
   * Finds a created component by a given DOM node.                                                  // 185  // 193
   *                                                                                                 // 186  // 194
   * @param {!Element} node                                                                          // 187  // 195
   * @return {*}                                                                                     // 188  // 196
   */                                                                                                // 189  // 197
  function findCreatedComponentByNodeInternal(node) {                                                // 190  // 198
    for (var n = 0; n < createdComponents_.length; n++) {                                            // 191  // 199
      var component = createdComponents_[n];                                                         // 192  // 200
      if (component.element_ === node) {                                                             // 193  // 201
        return component;                                                                            // 194  // 202
      }                                                                                              // 195  // 203
    }                                                                                                // 196  // 204
  }                                                                                                  // 197  // 205
                                                                                                     // 198  // 206
  /**                                                                                                // 199  // 207
   * Check the component for the downgrade method.                                                   // 200  // 208
   * Execute if found.                                                                               // 201  // 209
   * Remove component from createdComponents list.                                                   // 202  // 210
   *                                                                                                 // 203  // 211
   * @param {*} component                                                                            // 204  // 212
   */                                                                                                // 205  // 213
  function deconstructComponentInternal(component) {                                                 // 206  // 214
    if (component &&                                                                                 // 207  // 215
        component[componentConfigProperty_]                                                          // 208  // 216
          .classConstructor.prototype                                                                // 209  // 217
          .hasOwnProperty(downgradeMethod_)) {                                                       // 210  // 218
      component[downgradeMethod_]();                                                                 // 211  // 219
      var componentIndex = createdComponents_.indexOf(component);                                    // 212  // 220
      createdComponents_.splice(componentIndex, 1);                                                  // 213  // 221
                                                                                                     // 214  // 222
      var upgrades = component.element_.dataset.upgraded.split(',');                                 // 215  // 223
      var componentPlace = upgrades.indexOf(                                                         // 216  // 224
          component[componentConfigProperty_].classAsString);                                        // 217  // 225
      upgrades.splice(componentPlace, 1);                                                            // 218  // 226
      component.element_.dataset.upgraded = upgrades.join(',');                                      // 219  // 227
                                                                                                     // 220  // 228
      var ev = document.createEvent('Events');                                                       // 221  // 229
      ev.initEvent('mdl-componentdowngraded', true, true);                                           // 222  // 230
      component.element_.dispatchEvent(ev);                                                          // 223  // 231
    }                                                                                                // 224  // 232
  }                                                                                                  // 225  // 233
                                                                                                     // 226  // 234
  /**                                                                                                // 227  // 235
   * Downgrade either a given node, an array of nodes, or a NodeList.                                // 228  // 236
   *                                                                                                 // 229  // 237
   * @param {*} nodes                                                                                // 230  // 238
   */                                                                                                // 231  // 239
  function downgradeNodesInternal(nodes) {                                                           // 232  // 240
    var downgradeNode = function(node) {                                                             // 233  // 241
      deconstructComponentInternal(findCreatedComponentByNodeInternal(node));                        // 234  // 242
    };                                                                                               // 235  // 243
    if (nodes instanceof Array || nodes instanceof NodeList) {                                       // 236  // 244
      for (var n = 0; n < nodes.length; n++) {                                                       // 237  // 245
        downgradeNode(nodes[n]);                                                                     // 238  // 246
      }                                                                                              // 239  // 247
    } else if (nodes instanceof Node) {                                                              // 240  // 248
      downgradeNode(nodes);                                                                          // 241  // 249
    } else {                                                                                         // 242  // 250
      throw 'Invalid argument provided to downgrade MDL nodes.';                                     // 243  // 251
    }                                                                                                // 244  // 252
  }                                                                                                  // 245  // 253
                                                                                                     // 246  // 254
  // Now return the functions that should be made public with their publicly                         // 247  // 255
  // facing names...                                                                                 // 248  // 256
  return {                                                                                           // 249  // 257
    upgradeDom: upgradeDomInternal,                                                                  // 250  // 258
    upgradeElement: upgradeElementInternal,                                                          // 251  // 259
    upgradeAllRegistered: upgradeAllRegisteredInternal,                                              // 252  // 260
    registerUpgradedCallback: registerUpgradedCallbackInternal,                                      // 253  // 261
    register: registerInternal,                                                                      // 254  // 262
    downgradeElements: downgradeNodesInternal                                                        // 255  // 263
  };                                                                                                 // 256  // 264
})();                                                                                                // 257  // 265
                                                                                                     // 258  // 266
window.addEventListener('load', function() {                                                         // 259  // 267
  'use strict';                                                                                      // 260  // 268
                                                                                                     // 261  // 269
  /**                                                                                                // 262  // 270
   * Performs a "Cutting the mustard" test. If the browser supports the features                     // 263  // 271
   * tested, adds a mdl-js class to the <html> element. It then upgrades all MDL                     // 264  // 272
   * components requiring JavaScript.                                                                // 265  // 273
   */                                                                                                // 266  // 274
  if ('classList' in document.createElement('div') &&                                                // 267  // 275
      'querySelector' in document &&                                                                 // 268  // 276
      'addEventListener' in window && Array.prototype.forEach) {                                     // 269  // 277
    document.documentElement.classList.add('mdl-js');                                                // 270  // 278
    componentHandler.upgradeAllRegistered();                                                         // 271  // 279
  } else {                                                                                           // 272  // 280
    componentHandler.upgradeElement =                                                                // 273  // 281
        componentHandler.register = function() {};                                                   // 274  // 282
  }                                                                                                  // 275  // 283
});                                                                                                  // 276  // 284
                                                                                                     // 277  // 285
// Source: https://github.com/darius/requestAnimationFrame/blob/master/requestAnimationFrame.js      // 278  // 286
// Adapted from https://gist.github.com/paulirish/1579671 which derived from                         // 279  // 287
// http://paulirish.com/2011/requestanimationframe-for-smart-animating/                              // 280  // 288
// http://my.opera.com/emoller/blog/2011/12/20/requestanimationframe-for-smart-er-animating          // 281  // 289
                                                                                                     // 282  // 290
// requestAnimationFrame polyfill by Erik Möller.                                                    // 283  // 291
// Fixes from Paul Irish, Tino Zijdel, Andrew Mao, Klemen Slavič, Darius Bacon                       // 284  // 292
                                                                                                     // 285  // 293
// MIT license                                                                                       // 286  // 294
                                                                                                     // 287  // 295
(function() {                                                                                        // 288  // 296
'use strict';                                                                                        // 289  // 297
                                                                                                     // 290  // 298
if (!Date.now) {                                                                                     // 291  // 299
  Date.now = function() { return new Date().getTime(); };                                            // 292  // 300
}                                                                                                    // 293  // 301
                                                                                                     // 294  // 302
var vendors = ['webkit', 'moz'];                                                                     // 295  // 303
for (var i = 0; i < vendors.length && !window.requestAnimationFrame; ++i) {                          // 296  // 304
  var vp = vendors[i];                                                                               // 297  // 305
  window.requestAnimationFrame = window[vp + 'RequestAnimationFrame'];                               // 298  // 306
  window.cancelAnimationFrame = (window[vp + 'CancelAnimationFrame'] ||                              // 299  // 307
  window[vp + 'CancelRequestAnimationFrame']);                                                       // 300  // 308
}                                                                                                    // 301  // 309
                                                                                                     // 302  // 310
if (/iP(ad|hone|od).*OS 6/.test(window.navigator.userAgent) || !window.requestAnimationFrame || !window.cancelAnimationFrame) {
  var lastTime = 0;                                                                                  // 304  // 312
  window.requestAnimationFrame = function(callback) {                                                // 305  // 313
      var now = Date.now();                                                                          // 306  // 314
      var nextTime = Math.max(lastTime + 16, now);                                                   // 307  // 315
      return setTimeout(function() { callback(lastTime = nextTime); },                               // 308  // 316
                        nextTime - now);                                                             // 309  // 317
    };                                                                                               // 310  // 318
  window.cancelAnimationFrame = clearTimeout;                                                        // 311  // 319
}                                                                                                    // 312  // 320
                                                                                                     // 313  // 321
})();                                                                                                // 314  // 322
                                                                                                     // 315  // 323
                                                                                                     // 316  // 324
/**                                                                                                  // 317  // 325
 * @license                                                                                          // 318  // 326
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 319  // 327
 *                                                                                                   // 320  // 328
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 321  // 329
 * you may not use this file except in compliance with the License.                                  // 322  // 330
 * You may obtain a copy of the License at                                                           // 323  // 331
 *                                                                                                   // 324  // 332
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 325  // 333
 *                                                                                                   // 326  // 334
 * Unless required by applicable law or agreed to in writing, software                               // 327  // 335
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 328  // 336
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 329  // 337
 * See the License for the specific language governing permissions and                               // 330  // 338
 * limitations under the License.                                                                    // 331  // 339
 */                                                                                                  // 332  // 340
                                                                                                     // 333  // 341
/**                                                                                                  // 334  // 342
 * Class constructor for Button MDL component.                                                       // 335  // 343
 * Implements MDL component design pattern defined at:                                               // 336  // 344
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 337  // 345
 * @param {HTMLElement} element The element that will be upgraded.                                   // 338  // 346
 */                                                                                                  // 339  // 347
function MaterialButton(element) {                                                                   // 340  // 348
  'use strict';                                                                                      // 341  // 349
                                                                                                     // 342  // 350
  this.element_ = element;                                                                           // 343  // 351
                                                                                                     // 344  // 352
  // Initialize instance.                                                                            // 345  // 353
  this.init();                                                                                       // 346  // 354
}                                                                                                    // 347  // 355
                                                                                                     // 348  // 356
/**                                                                                                  // 349  // 357
 * Store constants in one place so they can be updated easily.                                       // 350  // 358
 * @enum {string | number}                                                                           // 351  // 359
 * @private                                                                                          // 352  // 360
 */                                                                                                  // 353  // 361
MaterialButton.prototype.Constant_ = {                                                               // 354  // 362
  // None for now.                                                                                   // 355  // 363
};                                                                                                   // 356  // 364
                                                                                                     // 357  // 365
/**                                                                                                  // 358  // 366
 * Store strings for class names defined by this component that are used in                          // 359  // 367
 * JavaScript. This allows us to simply change it in one place should we                             // 360  // 368
 * decide to modify at a later date.                                                                 // 361  // 369
 * @enum {string}                                                                                    // 362  // 370
 * @private                                                                                          // 363  // 371
 */                                                                                                  // 364  // 372
MaterialButton.prototype.CssClasses_ = {                                                             // 365  // 373
  RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                             // 366  // 374
  RIPPLE_CONTAINER: 'mdl-button__ripple-container',                                                  // 367  // 375
  RIPPLE: 'mdl-ripple'                                                                               // 368  // 376
};                                                                                                   // 369  // 377
                                                                                                     // 370  // 378
/**                                                                                                  // 371  // 379
 * Handle blur of element.                                                                           // 372  // 380
 * @param {HTMLElement} element The instance of a button we want to blur.                            // 373  // 381
 * @private                                                                                          // 374  // 382
 */                                                                                                  // 375  // 383
MaterialButton.prototype.blurHandler = function(event) {                                             // 376  // 384
  'use strict';                                                                                      // 377  // 385
                                                                                                     // 378  // 386
  if (event) {                                                                                       // 379  // 387
    this.element_.blur();                                                                            // 380  // 388
  }                                                                                                  // 381  // 389
};                                                                                                   // 382  // 390
                                                                                                     // 383  // 391
// Public methods.                                                                                   // 384  // 392
                                                                                                     // 385  // 393
/**                                                                                                  // 386  // 394
 * Disable button.                                                                                   // 387  // 395
 * @public                                                                                           // 388  // 396
 */                                                                                                  // 389  // 397
MaterialButton.prototype.disable = function() {                                                      // 390  // 398
  'use strict';                                                                                      // 391  // 399
                                                                                                     // 392  // 400
  this.element_.disabled = true;                                                                     // 393  // 401
};                                                                                                   // 394  // 402
                                                                                                     // 395  // 403
/**                                                                                                  // 396  // 404
 * Enable button.                                                                                    // 397  // 405
 * @public                                                                                           // 398  // 406
 */                                                                                                  // 399  // 407
MaterialButton.prototype.enable = function() {                                                       // 400  // 408
  'use strict';                                                                                      // 401  // 409
                                                                                                     // 402  // 410
  this.element_.disabled = false;                                                                    // 403  // 411
};                                                                                                   // 404  // 412
                                                                                                     // 405  // 413
/**                                                                                                  // 406  // 414
 * Initialize element.                                                                               // 407  // 415
 */                                                                                                  // 408  // 416
MaterialButton.prototype.init = function() {                                                         // 409  // 417
  'use strict';                                                                                      // 410  // 418
                                                                                                     // 411  // 419
  if (this.element_) {                                                                               // 412  // 420
    if (this.element_.classList.contains(this.CssClasses_.RIPPLE_EFFECT)) {                          // 413  // 421
      var rippleContainer = document.createElement('span');                                          // 414  // 422
      rippleContainer.classList.add(this.CssClasses_.RIPPLE_CONTAINER);                              // 415  // 423
      this.rippleElement_ = document.createElement('span');                                          // 416  // 424
      this.rippleElement_.classList.add(this.CssClasses_.RIPPLE);                                    // 417  // 425
      rippleContainer.appendChild(this.rippleElement_);                                              // 418  // 426
      this.boundRippleBlurHandler = this.blurHandler.bind(this);                                     // 419  // 427
      this.rippleElement_.addEventListener('mouseup', this.boundRippleBlurHandler);                  // 420  // 428
      this.element_.appendChild(rippleContainer);                                                    // 421  // 429
    }                                                                                                // 422  // 430
    this.boundButtonBlurHandler = this.blurHandler.bind(this);                                       // 423  // 431
    this.element_.addEventListener('mouseup', this.boundButtonBlurHandler);                          // 424  // 432
    this.element_.addEventListener('mouseleave', this.boundButtonBlurHandler);                       // 425  // 433
  }                                                                                                  // 426  // 434
};                                                                                                   // 427  // 435
                                                                                                     // 428  // 436
/**                                                                                                  // 429  // 437
 * Downgrade the element.                                                                            // 430  // 438
 */                                                                                                  // 431  // 439
MaterialButton.prototype.mdlDowngrade_ = function() {                                                // 432  // 440
  'use strict';                                                                                      // 433  // 441
  if (this.rippleElement_) {                                                                         // 434  // 442
    this.rippleElement_.removeEventListener('mouseup', this.boundRippleBlurHandler);                 // 435  // 443
  }                                                                                                  // 436  // 444
  this.element_.removeEventListener('mouseup', this.boundButtonBlurHandler);                         // 437  // 445
  this.element_.removeEventListener('mouseleave', this.boundButtonBlurHandler);                      // 438  // 446
};                                                                                                   // 439  // 447
                                                                                                     // 440  // 448
// The component registers itself. It can assume componentHandler is available                       // 441  // 449
// in the global scope.                                                                              // 442  // 450
componentHandler.register({                                                                          // 443  // 451
  constructor: MaterialButton,                                                                       // 444  // 452
  classAsString: 'MaterialButton',                                                                   // 445  // 453
  cssClass: 'mdl-js-button'                                                                          // 446  // 454
});                                                                                                  // 447  // 455
                                                                                                     // 448  // 456
/**                                                                                                  // 449  // 457
 * @license                                                                                          // 450  // 458
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 451  // 459
 *                                                                                                   // 452  // 460
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 453  // 461
 * you may not use this file except in compliance with the License.                                  // 454  // 462
 * You may obtain a copy of the License at                                                           // 455  // 463
 *                                                                                                   // 456  // 464
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 457  // 465
 *                                                                                                   // 458  // 466
 * Unless required by applicable law or agreed to in writing, software                               // 459  // 467
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 460  // 468
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 461  // 469
 * See the License for the specific language governing permissions and                               // 462  // 470
 * limitations under the License.                                                                    // 463  // 471
 */                                                                                                  // 464  // 472
                                                                                                     // 465  // 473
/**                                                                                                  // 466  // 474
 * Class constructor for Checkbox MDL component.                                                     // 467  // 475
 * Implements MDL component design pattern defined at:                                               // 468  // 476
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 469  // 477
 * @param {HTMLElement} element The element that will be upgraded.                                   // 470  // 478
 */                                                                                                  // 471  // 479
function MaterialCheckbox(element) {                                                                 // 472  // 480
  'use strict';                                                                                      // 473  // 481
                                                                                                     // 474  // 482
  this.element_ = element;                                                                           // 475  // 483
                                                                                                     // 476  // 484
  // Initialize instance.                                                                            // 477  // 485
  this.init();                                                                                       // 478  // 486
}                                                                                                    // 479  // 487
                                                                                                     // 480  // 488
/**                                                                                                  // 481  // 489
 * Store constants in one place so they can be updated easily.                                       // 482  // 490
 * @enum {string | number}                                                                           // 483  // 491
 * @private                                                                                          // 484  // 492
 */                                                                                                  // 485  // 493
MaterialCheckbox.prototype.Constant_ = {                                                             // 486  // 494
  TINY_TIMEOUT: 0.001                                                                                // 487  // 495
};                                                                                                   // 488  // 496
                                                                                                     // 489  // 497
/**                                                                                                  // 490  // 498
 * Store strings for class names defined by this component that are used in                          // 491  // 499
 * JavaScript. This allows us to simply change it in one place should we                             // 492  // 500
 * decide to modify at a later date.                                                                 // 493  // 501
 * @enum {string}                                                                                    // 494  // 502
 * @private                                                                                          // 495  // 503
 */                                                                                                  // 496  // 504
MaterialCheckbox.prototype.CssClasses_ = {                                                           // 497  // 505
  INPUT: 'mdl-checkbox__input',                                                                      // 498  // 506
  BOX_OUTLINE: 'mdl-checkbox__box-outline',                                                          // 499  // 507
  FOCUS_HELPER: 'mdl-checkbox__focus-helper',                                                        // 500  // 508
  TICK_OUTLINE: 'mdl-checkbox__tick-outline',                                                        // 501  // 509
  RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                             // 502  // 510
  RIPPLE_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events',                                       // 503  // 511
  RIPPLE_CONTAINER: 'mdl-checkbox__ripple-container',                                                // 504  // 512
  RIPPLE_CENTER: 'mdl-ripple--center',                                                               // 505  // 513
  RIPPLE: 'mdl-ripple',                                                                              // 506  // 514
  IS_FOCUSED: 'is-focused',                                                                          // 507  // 515
  IS_DISABLED: 'is-disabled',                                                                        // 508  // 516
  IS_CHECKED: 'is-checked',                                                                          // 509  // 517
  IS_UPGRADED: 'is-upgraded'                                                                         // 510  // 518
};                                                                                                   // 511  // 519
                                                                                                     // 512  // 520
/**                                                                                                  // 513  // 521
 * Handle change of state.                                                                           // 514  // 522
 * @param {Event} event The event that fired.                                                        // 515  // 523
 * @private                                                                                          // 516  // 524
 */                                                                                                  // 517  // 525
MaterialCheckbox.prototype.onChange_ = function(event) {                                             // 518  // 526
  'use strict';                                                                                      // 519  // 527
                                                                                                     // 520  // 528
  this.updateClasses_();                                                                             // 521  // 529
};                                                                                                   // 522  // 530
                                                                                                     // 523  // 531
/**                                                                                                  // 524  // 532
 * Handle focus of element.                                                                          // 525  // 533
 * @param {Event} event The event that fired.                                                        // 526  // 534
 * @private                                                                                          // 527  // 535
 */                                                                                                  // 528  // 536
MaterialCheckbox.prototype.onFocus_ = function(event) {                                              // 529  // 537
  'use strict';                                                                                      // 530  // 538
                                                                                                     // 531  // 539
  this.element_.classList.add(this.CssClasses_.IS_FOCUSED);                                          // 532  // 540
};                                                                                                   // 533  // 541
                                                                                                     // 534  // 542
/**                                                                                                  // 535  // 543
 * Handle lost focus of element.                                                                     // 536  // 544
 * @param {Event} event The event that fired.                                                        // 537  // 545
 * @private                                                                                          // 538  // 546
 */                                                                                                  // 539  // 547
MaterialCheckbox.prototype.onBlur_ = function(event) {                                               // 540  // 548
  'use strict';                                                                                      // 541  // 549
                                                                                                     // 542  // 550
  this.element_.classList.remove(this.CssClasses_.IS_FOCUSED);                                       // 543  // 551
};                                                                                                   // 544  // 552
                                                                                                     // 545  // 553
/**                                                                                                  // 546  // 554
 * Handle mouseup.                                                                                   // 547  // 555
 * @param {Event} event The event that fired.                                                        // 548  // 556
 * @private                                                                                          // 549  // 557
 */                                                                                                  // 550  // 558
MaterialCheckbox.prototype.onMouseUp_ = function(event) {                                            // 551  // 559
  'use strict';                                                                                      // 552  // 560
                                                                                                     // 553  // 561
  this.blur_();                                                                                      // 554  // 562
};                                                                                                   // 555  // 563
                                                                                                     // 556  // 564
/**                                                                                                  // 557  // 565
 * Handle class updates.                                                                             // 558  // 566
 * @param {HTMLElement} button The button whose classes we should update.                            // 559  // 567
 * @param {HTMLElement} label The label whose classes we should update.                              // 560  // 568
 * @private                                                                                          // 561  // 569
 */                                                                                                  // 562  // 570
MaterialCheckbox.prototype.updateClasses_ = function() {                                             // 563  // 571
  'use strict';                                                                                      // 564  // 572
                                                                                                     // 565  // 573
  if (this.inputElement_.disabled) {                                                                 // 566  // 574
    this.element_.classList.add(this.CssClasses_.IS_DISABLED);                                       // 567  // 575
  } else {                                                                                           // 568  // 576
    this.element_.classList.remove(this.CssClasses_.IS_DISABLED);                                    // 569  // 577
  }                                                                                                  // 570  // 578
                                                                                                     // 571  // 579
  if (this.inputElement_.checked) {                                                                  // 572  // 580
    this.element_.classList.add(this.CssClasses_.IS_CHECKED);                                        // 573  // 581
  } else {                                                                                           // 574  // 582
    this.element_.classList.remove(this.CssClasses_.IS_CHECKED);                                     // 575  // 583
  }                                                                                                  // 576  // 584
};                                                                                                   // 577  // 585
                                                                                                     // 578  // 586
/**                                                                                                  // 579  // 587
 * Add blur.                                                                                         // 580  // 588
 * @private                                                                                          // 581  // 589
 */                                                                                                  // 582  // 590
MaterialCheckbox.prototype.blur_ = function(event) {                                                 // 583  // 591
  'use strict';                                                                                      // 584  // 592
                                                                                                     // 585  // 593
  // TODO: figure out why there's a focus event being fired after our blur,                          // 586  // 594
  // so that we can avoid this hack.                                                                 // 587  // 595
  window.setTimeout(function() {                                                                     // 588  // 596
    this.inputElement_.blur();                                                                       // 589  // 597
  }.bind(this), this.Constant_.TINY_TIMEOUT);                                                        // 590  // 598
};                                                                                                   // 591  // 599
                                                                                                     // 592  // 600
// Public methods.                                                                                   // 593  // 601
                                                                                                     // 594  // 602
/**                                                                                                  // 595  // 603
 * Disable checkbox.                                                                                 // 596  // 604
 * @public                                                                                           // 597  // 605
 */                                                                                                  // 598  // 606
MaterialCheckbox.prototype.disable = function() {                                                    // 599  // 607
  'use strict';                                                                                      // 600  // 608
                                                                                                     // 601  // 609
  this.inputElement_.disabled = true;                                                                // 602  // 610
  this.updateClasses_();                                                                             // 603  // 611
};                                                                                                   // 604  // 612
                                                                                                     // 605  // 613
/**                                                                                                  // 606  // 614
 * Enable checkbox.                                                                                  // 607  // 615
 * @public                                                                                           // 608  // 616
 */                                                                                                  // 609  // 617
MaterialCheckbox.prototype.enable = function() {                                                     // 610  // 618
  'use strict';                                                                                      // 611  // 619
                                                                                                     // 612  // 620
  this.inputElement_.disabled = false;                                                               // 613  // 621
  this.updateClasses_();                                                                             // 614  // 622
};                                                                                                   // 615  // 623
                                                                                                     // 616  // 624
/**                                                                                                  // 617  // 625
 * Check checkbox.                                                                                   // 618  // 626
 * @public                                                                                           // 619  // 627
 */                                                                                                  // 620  // 628
MaterialCheckbox.prototype.check = function() {                                                      // 621  // 629
  'use strict';                                                                                      // 622  // 630
                                                                                                     // 623  // 631
  this.inputElement_.checked = true;                                                                 // 624  // 632
  this.updateClasses_();                                                                             // 625  // 633
};                                                                                                   // 626  // 634
                                                                                                     // 627  // 635
/**                                                                                                  // 628  // 636
 * Uncheck checkbox.                                                                                 // 629  // 637
 * @public                                                                                           // 630  // 638
 */                                                                                                  // 631  // 639
MaterialCheckbox.prototype.uncheck = function() {                                                    // 632  // 640
  'use strict';                                                                                      // 633  // 641
                                                                                                     // 634  // 642
  this.inputElement_.checked = false;                                                                // 635  // 643
  this.updateClasses_();                                                                             // 636  // 644
};                                                                                                   // 637  // 645
                                                                                                     // 638  // 646
/**                                                                                                  // 639  // 647
 * Initialize element.                                                                               // 640  // 648
 */                                                                                                  // 641  // 649
MaterialCheckbox.prototype.init = function() {                                                       // 642  // 650
  'use strict';                                                                                      // 643  // 651
                                                                                                     // 644  // 652
  if (this.element_) {                                                                               // 645  // 653
    this.inputElement_ = this.element_.querySelector('.' +                                           // 646  // 654
        this.CssClasses_.INPUT);                                                                     // 647  // 655
                                                                                                     // 648  // 656
    var boxOutline = document.createElement('span');                                                 // 649  // 657
    boxOutline.classList.add(this.CssClasses_.BOX_OUTLINE);                                          // 650  // 658
                                                                                                     // 651  // 659
    var tickContainer = document.createElement('span');                                              // 652  // 660
    tickContainer.classList.add(this.CssClasses_.FOCUS_HELPER);                                      // 653  // 661
                                                                                                     // 654  // 662
    var tickOutline = document.createElement('span');                                                // 655  // 663
    tickOutline.classList.add(this.CssClasses_.TICK_OUTLINE);                                        // 656  // 664
                                                                                                     // 657  // 665
    boxOutline.appendChild(tickOutline);                                                             // 658  // 666
                                                                                                     // 659  // 667
    this.element_.appendChild(tickContainer);                                                        // 660  // 668
    this.element_.appendChild(boxOutline);                                                           // 661  // 669
                                                                                                     // 662  // 670
    if (this.element_.classList.contains(this.CssClasses_.RIPPLE_EFFECT)) {                          // 663  // 671
      this.element_.classList.add(this.CssClasses_.RIPPLE_IGNORE_EVENTS);                            // 664  // 672
      this.rippleContainerElement_ = document.createElement('span');                                 // 665  // 673
      this.rippleContainerElement_.classList.add(this.CssClasses_.RIPPLE_CONTAINER);                 // 666  // 674
      this.rippleContainerElement_.classList.add(this.CssClasses_.RIPPLE_EFFECT);                    // 667  // 675
      this.rippleContainerElement_.classList.add(this.CssClasses_.RIPPLE_CENTER);                    // 668  // 676
      this.boundRippleMouseUp = this.onMouseUp_.bind(this);                                          // 669  // 677
      this.rippleContainerElement_.addEventListener('mouseup', this.boundRippleMouseUp);             // 670  // 678
                                                                                                     // 671  // 679
      var ripple = document.createElement('span');                                                   // 672  // 680
      ripple.classList.add(this.CssClasses_.RIPPLE);                                                 // 673  // 681
                                                                                                     // 674  // 682
      this.rippleContainerElement_.appendChild(ripple);                                              // 675  // 683
      this.element_.appendChild(this.rippleContainerElement_);                                       // 676  // 684
    }                                                                                                // 677  // 685
    this.boundInputOnChange = this.onChange_.bind(this);                                             // 678  // 686
    this.boundInputOnFocus = this.onFocus_.bind(this);                                               // 679  // 687
    this.boundInputOnBlur = this.onBlur_.bind(this);                                                 // 680  // 688
    this.boundElementMouseUp = this.onMouseUp_.bind(this);                                           // 681  // 689
    this.inputElement_.addEventListener('change', this.boundInputOnChange);                          // 682  // 690
    this.inputElement_.addEventListener('focus', this.boundInputOnFocus);                            // 683  // 691
    this.inputElement_.addEventListener('blur', this.boundInputOnBlur);                              // 684  // 692
    this.element_.addEventListener('mouseup', this.boundElementMouseUp);                             // 685  // 693
                                                                                                     // 686  // 694
    this.updateClasses_();                                                                           // 687  // 695
    this.element_.classList.add(this.CssClasses_.IS_UPGRADED);                                       // 688  // 696
  }                                                                                                  // 689  // 697
};                                                                                                   // 690  // 698
                                                                                                     // 691  // 699
/*                                                                                                   // 692  // 700
* Downgrade the component.                                                                           // 693  // 701
*/                                                                                                   // 694  // 702
MaterialCheckbox.prototype.mdlDowngrade_ = function() {                                              // 695  // 703
  'use strict';                                                                                      // 696  // 704
  if (this.rippleContainerElement_) {                                                                // 697  // 705
    this.rippleContainerElement_.removeEventListener('mouseup', this.boundRippleMouseUp);            // 698  // 706
  }                                                                                                  // 699  // 707
  this.inputElement_.removeEventListener('change', this.boundInputOnChange);                         // 700  // 708
  this.inputElement_.removeEventListener('focus', this.boundInputOnFocus);                           // 701  // 709
  this.inputElement_.removeEventListener('blur', this.boundInputOnBlur);                             // 702  // 710
  this.element_.removeEventListener('mouseup', this.boundElementMouseUp);                            // 703  // 711
};                                                                                                   // 704  // 712
                                                                                                     // 705  // 713
// The component registers itself. It can assume componentHandler is available                       // 706  // 714
// in the global scope.                                                                              // 707  // 715
componentHandler.register({                                                                          // 708  // 716
  constructor: MaterialCheckbox,                                                                     // 709  // 717
  classAsString: 'MaterialCheckbox',                                                                 // 710  // 718
  cssClass: 'mdl-js-checkbox'                                                                        // 711  // 719
});                                                                                                  // 712  // 720
                                                                                                     // 713  // 721
/**                                                                                                  // 714  // 722
 * @license                                                                                          // 715  // 723
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 716  // 724
 *                                                                                                   // 717  // 725
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 718  // 726
 * you may not use this file except in compliance with the License.                                  // 719  // 727
 * You may obtain a copy of the License at                                                           // 720  // 728
 *                                                                                                   // 721  // 729
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 722  // 730
 *                                                                                                   // 723  // 731
 * Unless required by applicable law or agreed to in writing, software                               // 724  // 732
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 725  // 733
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 726  // 734
 * See the License for the specific language governing permissions and                               // 727  // 735
 * limitations under the License.                                                                    // 728  // 736
 */                                                                                                  // 729  // 737
                                                                                                     // 730  // 738
/**                                                                                                  // 731  // 739
 * Class constructor for icon toggle MDL component.                                                  // 732  // 740
 * Implements MDL component design pattern defined at:                                               // 733  // 741
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 734  // 742
 * @param {HTMLElement} element The element that will be upgraded.                                   // 735  // 743
 */                                                                                                  // 736  // 744
function MaterialIconToggle(element) {                                                               // 737  // 745
  'use strict';                                                                                      // 738  // 746
                                                                                                     // 739  // 747
  this.element_ = element;                                                                           // 740  // 748
                                                                                                     // 741  // 749
  // Initialize instance.                                                                            // 742  // 750
  this.init();                                                                                       // 743  // 751
}                                                                                                    // 744  // 752
                                                                                                     // 745  // 753
/**                                                                                                  // 746  // 754
 * Store constants in one place so they can be updated easily.                                       // 747  // 755
 * @enum {string | number}                                                                           // 748  // 756
 * @private                                                                                          // 749  // 757
 */                                                                                                  // 750  // 758
MaterialIconToggle.prototype.Constant_ = {                                                           // 751  // 759
  TINY_TIMEOUT: 0.001                                                                                // 752  // 760
};                                                                                                   // 753  // 761
                                                                                                     // 754  // 762
/**                                                                                                  // 755  // 763
 * Store strings for class names defined by this component that are used in                          // 756  // 764
 * JavaScript. This allows us to simply change it in one place should we                             // 757  // 765
 * decide to modify at a later date.                                                                 // 758  // 766
 * @enum {string}                                                                                    // 759  // 767
 * @private                                                                                          // 760  // 768
 */                                                                                                  // 761  // 769
MaterialIconToggle.prototype.CssClasses_ = {                                                         // 762  // 770
  INPUT: 'mdl-icon-toggle__input',                                                                   // 763  // 771
  JS_RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                          // 764  // 772
  RIPPLE_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events',                                       // 765  // 773
  RIPPLE_CONTAINER: 'mdl-icon-toggle__ripple-container',                                             // 766  // 774
  RIPPLE_CENTER: 'mdl-ripple--center',                                                               // 767  // 775
  RIPPLE: 'mdl-ripple',                                                                              // 768  // 776
  IS_FOCUSED: 'is-focused',                                                                          // 769  // 777
  IS_DISABLED: 'is-disabled',                                                                        // 770  // 778
  IS_CHECKED: 'is-checked'                                                                           // 771  // 779
};                                                                                                   // 772  // 780
                                                                                                     // 773  // 781
/**                                                                                                  // 774  // 782
 * Handle change of state.                                                                           // 775  // 783
 * @param {Event} event The event that fired.                                                        // 776  // 784
 * @private                                                                                          // 777  // 785
 */                                                                                                  // 778  // 786
MaterialIconToggle.prototype.onChange_ = function(event) {                                           // 779  // 787
  'use strict';                                                                                      // 780  // 788
                                                                                                     // 781  // 789
  this.updateClasses_();                                                                             // 782  // 790
};                                                                                                   // 783  // 791
                                                                                                     // 784  // 792
/**                                                                                                  // 785  // 793
 * Handle focus of element.                                                                          // 786  // 794
 * @param {Event} event The event that fired.                                                        // 787  // 795
 * @private                                                                                          // 788  // 796
 */                                                                                                  // 789  // 797
MaterialIconToggle.prototype.onFocus_ = function(event) {                                            // 790  // 798
  'use strict';                                                                                      // 791  // 799
                                                                                                     // 792  // 800
  this.element_.classList.add(this.CssClasses_.IS_FOCUSED);                                          // 793  // 801
};                                                                                                   // 794  // 802
                                                                                                     // 795  // 803
/**                                                                                                  // 796  // 804
 * Handle lost focus of element.                                                                     // 797  // 805
 * @param {Event} event The event that fired.                                                        // 798  // 806
 * @private                                                                                          // 799  // 807
 */                                                                                                  // 800  // 808
MaterialIconToggle.prototype.onBlur_ = function(event) {                                             // 801  // 809
  'use strict';                                                                                      // 802  // 810
                                                                                                     // 803  // 811
  this.element_.classList.remove(this.CssClasses_.IS_FOCUSED);                                       // 804  // 812
};                                                                                                   // 805  // 813
                                                                                                     // 806  // 814
/**                                                                                                  // 807  // 815
 * Handle mouseup.                                                                                   // 808  // 816
 * @param {Event} event The event that fired.                                                        // 809  // 817
 * @private                                                                                          // 810  // 818
 */                                                                                                  // 811  // 819
MaterialIconToggle.prototype.onMouseUp_ = function(event) {                                          // 812  // 820
  'use strict';                                                                                      // 813  // 821
                                                                                                     // 814  // 822
  this.blur_();                                                                                      // 815  // 823
};                                                                                                   // 816  // 824
                                                                                                     // 817  // 825
/**                                                                                                  // 818  // 826
 * Handle class updates.                                                                             // 819  // 827
 * @param {HTMLElement} button The button whose classes we should update.                            // 820  // 828
 * @param {HTMLElement} label The label whose classes we should update.                              // 821  // 829
 * @private                                                                                          // 822  // 830
 */                                                                                                  // 823  // 831
MaterialIconToggle.prototype.updateClasses_ = function() {                                           // 824  // 832
  'use strict';                                                                                      // 825  // 833
                                                                                                     // 826  // 834
  if (this.inputElement_.disabled) {                                                                 // 827  // 835
    this.element_.classList.add(this.CssClasses_.IS_DISABLED);                                       // 828  // 836
  } else {                                                                                           // 829  // 837
    this.element_.classList.remove(this.CssClasses_.IS_DISABLED);                                    // 830  // 838
  }                                                                                                  // 831  // 839
                                                                                                     // 832  // 840
  if (this.inputElement_.checked) {                                                                  // 833  // 841
    this.element_.classList.add(this.CssClasses_.IS_CHECKED);                                        // 834  // 842
  } else {                                                                                           // 835  // 843
    this.element_.classList.remove(this.CssClasses_.IS_CHECKED);                                     // 836  // 844
  }                                                                                                  // 837  // 845
};                                                                                                   // 838  // 846
                                                                                                     // 839  // 847
/**                                                                                                  // 840  // 848
 * Add blur.                                                                                         // 841  // 849
 * @private                                                                                          // 842  // 850
 */                                                                                                  // 843  // 851
MaterialIconToggle.prototype.blur_ = function(event) {                                               // 844  // 852
  'use strict';                                                                                      // 845  // 853
                                                                                                     // 846  // 854
  // TODO: figure out why there's a focus event being fired after our blur,                          // 847  // 855
  // so that we can avoid this hack.                                                                 // 848  // 856
  window.setTimeout(function() {                                                                     // 849  // 857
    this.inputElement_.blur();                                                                       // 850  // 858
  }.bind(this), this.Constant_.TINY_TIMEOUT);                                                        // 851  // 859
};                                                                                                   // 852  // 860
                                                                                                     // 853  // 861
// Public methods.                                                                                   // 854  // 862
                                                                                                     // 855  // 863
/**                                                                                                  // 856  // 864
 * Disable icon toggle.                                                                              // 857  // 865
 * @public                                                                                           // 858  // 866
 */                                                                                                  // 859  // 867
MaterialIconToggle.prototype.disable = function() {                                                  // 860  // 868
  'use strict';                                                                                      // 861  // 869
                                                                                                     // 862  // 870
  this.inputElement_.disabled = true;                                                                // 863  // 871
  this.updateClasses_();                                                                             // 864  // 872
};                                                                                                   // 865  // 873
                                                                                                     // 866  // 874
/**                                                                                                  // 867  // 875
 * Enable icon toggle.                                                                               // 868  // 876
 * @public                                                                                           // 869  // 877
 */                                                                                                  // 870  // 878
MaterialIconToggle.prototype.enable = function() {                                                   // 871  // 879
  'use strict';                                                                                      // 872  // 880
                                                                                                     // 873  // 881
  this.inputElement_.disabled = false;                                                               // 874  // 882
  this.updateClasses_();                                                                             // 875  // 883
};                                                                                                   // 876  // 884
                                                                                                     // 877  // 885
/**                                                                                                  // 878  // 886
 * Check icon toggle.                                                                                // 879  // 887
 * @public                                                                                           // 880  // 888
 */                                                                                                  // 881  // 889
MaterialIconToggle.prototype.check = function() {                                                    // 882  // 890
  'use strict';                                                                                      // 883  // 891
                                                                                                     // 884  // 892
  this.inputElement_.checked = true;                                                                 // 885  // 893
  this.updateClasses_();                                                                             // 886  // 894
};                                                                                                   // 887  // 895
                                                                                                     // 888  // 896
/**                                                                                                  // 889  // 897
 * Uncheck icon toggle.                                                                              // 890  // 898
 * @public                                                                                           // 891  // 899
 */                                                                                                  // 892  // 900
MaterialIconToggle.prototype.uncheck = function() {                                                  // 893  // 901
  'use strict';                                                                                      // 894  // 902
                                                                                                     // 895  // 903
  this.inputElement_.checked = false;                                                                // 896  // 904
  this.updateClasses_();                                                                             // 897  // 905
};                                                                                                   // 898  // 906
                                                                                                     // 899  // 907
/**                                                                                                  // 900  // 908
 * Initialize element.                                                                               // 901  // 909
 */                                                                                                  // 902  // 910
MaterialIconToggle.prototype.init = function() {                                                     // 903  // 911
  'use strict';                                                                                      // 904  // 912
                                                                                                     // 905  // 913
  if (this.element_) {                                                                               // 906  // 914
    this.inputElement_ =                                                                             // 907  // 915
        this.element_.querySelector('.' + this.CssClasses_.INPUT);                                   // 908  // 916
                                                                                                     // 909  // 917
    if (this.element_.classList.contains(this.CssClasses_.JS_RIPPLE_EFFECT)) {                       // 910  // 918
      this.element_.classList.add(this.CssClasses_.RIPPLE_IGNORE_EVENTS);                            // 911  // 919
      this.rippleContainerElement_ = document.createElement('span');                                 // 912  // 920
      this.rippleContainerElement_.classList.add(this.CssClasses_.RIPPLE_CONTAINER);                 // 913  // 921
      this.rippleContainerElement_.classList.add(this.CssClasses_.JS_RIPPLE_EFFECT);                 // 914  // 922
      this.rippleContainerElement_.classList.add(this.CssClasses_.RIPPLE_CENTER);                    // 915  // 923
      this.boundRippleMouseUp = this.onMouseUp_.bind(this);                                          // 916  // 924
      this.rippleContainerElement_.addEventListener('mouseup', this.boundRippleMouseUp);             // 917  // 925
                                                                                                     // 918  // 926
      var ripple = document.createElement('span');                                                   // 919  // 927
      ripple.classList.add(this.CssClasses_.RIPPLE);                                                 // 920  // 928
                                                                                                     // 921  // 929
      this.rippleContainerElement_.appendChild(ripple);                                              // 922  // 930
      this.element_.appendChild(this.rippleContainerElement_);                                       // 923  // 931
    }                                                                                                // 924  // 932
                                                                                                     // 925  // 933
    this.boundInputOnChange = this.onChange_.bind(this);                                             // 926  // 934
    this.boundInputOnFocus = this.onFocus_.bind(this);                                               // 927  // 935
    this.boundInputOnBlur = this.onBlur_.bind(this);                                                 // 928  // 936
    this.boundElementOnMouseUp = this.onMouseUp_.bind(this);                                         // 929  // 937
    this.inputElement_.addEventListener('change', this.boundInputOnChange);                          // 930  // 938
    this.inputElement_.addEventListener('focus', this.boundInputOnFocus);                            // 931  // 939
    this.inputElement_.addEventListener('blur', this.boundInputOnBlur);                              // 932  // 940
    this.element_.addEventListener('mouseup', this.boundElementOnMouseUp);                           // 933  // 941
                                                                                                     // 934  // 942
    this.updateClasses_();                                                                           // 935  // 943
    this.element_.classList.add('is-upgraded');                                                      // 936  // 944
  }                                                                                                  // 937  // 945
};                                                                                                   // 938  // 946
                                                                                                     // 939  // 947
/*                                                                                                   // 940  // 948
* Downgrade the component                                                                            // 941  // 949
*/                                                                                                   // 942  // 950
MaterialIconToggle.prototype.mdlDowngrade_ = function() {                                            // 943  // 951
  'use strict';                                                                                      // 944  // 952
  if (this.rippleContainerElement_) {                                                                // 945  // 953
    this.rippleContainerElement_.removeEventListener('mouseup', this.boundRippleMouseUp);            // 946  // 954
  }                                                                                                  // 947  // 955
  this.inputElement_.removeEventListener('change', this.boundInputOnChange);                         // 948  // 956
  this.inputElement_.removeEventListener('focus', this.boundInputOnFocus);                           // 949  // 957
  this.inputElement_.removeEventListener('blur', this.boundInputOnBlur);                             // 950  // 958
  this.element_.removeEventListener('mouseup', this.boundElementOnMouseUp);                          // 951  // 959
};                                                                                                   // 952  // 960
                                                                                                     // 953  // 961
// The component registers itself. It can assume componentHandler is available                       // 954  // 962
// in the global scope.                                                                              // 955  // 963
componentHandler.register({                                                                          // 956  // 964
  constructor: MaterialIconToggle,                                                                   // 957  // 965
  classAsString: 'MaterialIconToggle',                                                               // 958  // 966
  cssClass: 'mdl-js-icon-toggle'                                                                     // 959  // 967
});                                                                                                  // 960  // 968
                                                                                                     // 961  // 969
/**                                                                                                  // 962  // 970
 * @license                                                                                          // 963  // 971
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 964  // 972
 *                                                                                                   // 965  // 973
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 966  // 974
 * you may not use this file except in compliance with the License.                                  // 967  // 975
 * You may obtain a copy of the License at                                                           // 968  // 976
 *                                                                                                   // 969  // 977
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 970  // 978
 *                                                                                                   // 971  // 979
 * Unless required by applicable law or agreed to in writing, software                               // 972  // 980
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 973  // 981
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 974  // 982
 * See the License for the specific language governing permissions and                               // 975  // 983
 * limitations under the License.                                                                    // 976  // 984
 */                                                                                                  // 977  // 985
                                                                                                     // 978  // 986
/**                                                                                                  // 979  // 987
 * Class constructor for dropdown MDL component.                                                     // 980  // 988
 * Implements MDL component design pattern defined at:                                               // 981  // 989
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 982  // 990
 * @param {HTMLElement} element The element that will be upgraded.                                   // 983  // 991
 */                                                                                                  // 984  // 992
function MaterialMenu(element) {                                                                     // 985  // 993
  'use strict';                                                                                      // 986  // 994
                                                                                                     // 987  // 995
  this.element_ = element;                                                                           // 988  // 996
                                                                                                     // 989  // 997
  // Initialize instance.                                                                            // 990  // 998
  this.init();                                                                                       // 991  // 999
}                                                                                                    // 992  // 1000
                                                                                                     // 993  // 1001
/**                                                                                                  // 994  // 1002
 * Store constants in one place so they can be updated easily.                                       // 995  // 1003
 * @enum {string | number}                                                                           // 996  // 1004
 * @private                                                                                          // 997  // 1005
 */                                                                                                  // 998  // 1006
MaterialMenu.prototype.Constant_ = {                                                                 // 999  // 1007
  // Total duration of the menu animation.                                                           // 1000
  TRANSITION_DURATION_SECONDS: 0.3,                                                                  // 1001
  // The fraction of the total duration we want to use for menu item animations.                     // 1002
  TRANSITION_DURATION_FRACTION: 0.8,                                                                 // 1003
  // How long the menu stays open after choosing an option (so the user can see                      // 1004
  // the ripple).                                                                                    // 1005
  CLOSE_TIMEOUT: 150                                                                                 // 1006
};                                                                                                   // 1007
                                                                                                     // 1008
/**                                                                                                  // 1009
 * Keycodes, for code readability.                                                                   // 1010
 * @enum {number}                                                                                    // 1011
 * @private                                                                                          // 1012
 */                                                                                                  // 1013
MaterialMenu.prototype.Keycodes_ = {                                                                 // 1014
  ENTER: 13,                                                                                         // 1015
  ESCAPE: 27,                                                                                        // 1016
  SPACE: 32,                                                                                         // 1017
  UP_ARROW: 38,                                                                                      // 1018
  DOWN_ARROW: 40                                                                                     // 1019
};                                                                                                   // 1020
                                                                                                     // 1021
/**                                                                                                  // 1022
 * Store strings for class names defined by this component that are used in                          // 1023
 * JavaScript. This allows us to simply change it in one place should we                             // 1024
 * decide to modify at a later date.                                                                 // 1025
 * @enum {string}                                                                                    // 1026
 * @private                                                                                          // 1027
 */                                                                                                  // 1028
MaterialMenu.prototype.CssClasses_ = {                                                               // 1029
  CONTAINER: 'mdl-menu__container',                                                                  // 1030
  OUTLINE: 'mdl-menu__outline',                                                                      // 1031
  ITEM: 'mdl-menu__item',                                                                            // 1032
  ITEM_RIPPLE_CONTAINER: 'mdl-menu__item-ripple-container',                                          // 1033
  RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                             // 1034
  RIPPLE_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events',                                       // 1035
  RIPPLE: 'mdl-ripple',                                                                              // 1036
  // Statuses                                                                                        // 1037
  IS_UPGRADED: 'is-upgraded',                                                                        // 1038
  IS_VISIBLE: 'is-visible',                                                                          // 1039
  IS_ANIMATING: 'is-animating',                                                                      // 1040
  // Alignment options                                                                               // 1041
  BOTTOM_LEFT: 'mdl-menu--bottom-left',  // This is the default.                                     // 1042
  BOTTOM_RIGHT: 'mdl-menu--bottom-right',                                                            // 1043
  TOP_LEFT: 'mdl-menu--top-left',                                                                    // 1044
  TOP_RIGHT: 'mdl-menu--top-right',                                                                  // 1045
  UNALIGNED: 'mdl-menu--unaligned'                                                                   // 1046
};                                                                                                   // 1047
                                                                                                     // 1048
/**                                                                                                  // 1049
 * Initialize element.                                                                               // 1050
 */                                                                                                  // 1051
MaterialMenu.prototype.init = function() {                                                           // 1052
  'use strict';                                                                                      // 1053
                                                                                                     // 1054
  if (this.element_) {                                                                               // 1055
    // Create container for the menu.                                                                // 1056
    var container = document.createElement('div');                                                   // 1057
    container.classList.add(this.CssClasses_.CONTAINER);                                             // 1058
    this.element_.parentElement.insertBefore(container, this.element_);                              // 1059
    this.element_.parentElement.removeChild(this.element_);                                          // 1060
    container.appendChild(this.element_);                                                            // 1061
    this.container_ = container;                                                                     // 1062
                                                                                                     // 1063
    // Create outline for the menu (shadow and background).                                          // 1064
    var outline = document.createElement('div');                                                     // 1065
    outline.classList.add(this.CssClasses_.OUTLINE);                                                 // 1066
    this.outline_ = outline;                                                                         // 1067
    container.insertBefore(outline, this.element_);                                                  // 1068
                                                                                                     // 1069
    // Find the "for" element and bind events to it.                                                 // 1070
    var forElId = this.element_.getAttribute('for');                                                 // 1071
    var forEl = null;                                                                                // 1072
    if (forElId) {                                                                                   // 1073
      forEl = document.getElementById(forElId);                                                      // 1074
      if (forEl) {                                                                                   // 1075
        this.forElement_ = forEl;                                                                    // 1076
        forEl.addEventListener('click', this.handleForClick_.bind(this));                            // 1077
        forEl.addEventListener('keydown',                                                            // 1078
            this.handleForKeyboardEvent_.bind(this));                                                // 1079
      }                                                                                              // 1080
    }                                                                                                // 1081
                                                                                                     // 1082
    var items = this.element_.querySelectorAll('.' + this.CssClasses_.ITEM);                         // 1083
                                                                                                     // 1084
    for (var i = 0; i < items.length; i++) {                                                         // 1085
      // Add a listener to each menu item.                                                           // 1086
      items[i].addEventListener('click', this.handleItemClick_.bind(this));                          // 1087
      // Add a tab index to each menu item.                                                          // 1088
      items[i].tabIndex = '-1';                                                                      // 1089
      // Add a keyboard listener to each menu item.                                                  // 1090
      items[i].addEventListener('keydown',                                                           // 1091
          this.handleItemKeyboardEvent_.bind(this));                                                 // 1092
    }                                                                                                // 1093
                                                                                                     // 1094
    // Add ripple classes to each item, if the user has enabled ripples.                             // 1095
    if (this.element_.classList.contains(this.CssClasses_.RIPPLE_EFFECT)) {                          // 1096
      this.element_.classList.add(this.CssClasses_.RIPPLE_IGNORE_EVENTS);                            // 1097
                                                                                                     // 1098
      for (i = 0; i < items.length; i++) {                                                           // 1099
        var item = items[i];                                                                         // 1100
                                                                                                     // 1101
        var rippleContainer = document.createElement('span');                                        // 1102
        rippleContainer.classList.add(this.CssClasses_.ITEM_RIPPLE_CONTAINER);                       // 1103
                                                                                                     // 1104
        var ripple = document.createElement('span');                                                 // 1105
        ripple.classList.add(this.CssClasses_.RIPPLE);                                               // 1106
        rippleContainer.appendChild(ripple);                                                         // 1107
                                                                                                     // 1108
        item.appendChild(rippleContainer);                                                           // 1109
        item.classList.add(this.CssClasses_.RIPPLE_EFFECT);                                          // 1110
      }                                                                                              // 1111
    }                                                                                                // 1112
                                                                                                     // 1113
    // Copy alignment classes to the container, so the outline can use them.                         // 1114
    if (this.element_.classList.contains(this.CssClasses_.BOTTOM_LEFT)) {                            // 1115
      this.outline_.classList.add(this.CssClasses_.BOTTOM_LEFT);                                     // 1116
    }                                                                                                // 1117
    if (this.element_.classList.contains(this.CssClasses_.BOTTOM_RIGHT)) {                           // 1118
      this.outline_.classList.add(this.CssClasses_.BOTTOM_RIGHT);                                    // 1119
    }                                                                                                // 1120
    if (this.element_.classList.contains(this.CssClasses_.TOP_LEFT)) {                               // 1121
      this.outline_.classList.add(this.CssClasses_.TOP_LEFT);                                        // 1122
    }                                                                                                // 1123
    if (this.element_.classList.contains(this.CssClasses_.TOP_RIGHT)) {                              // 1124
      this.outline_.classList.add(this.CssClasses_.TOP_RIGHT);                                       // 1125
    }                                                                                                // 1126
    if (this.element_.classList.contains(this.CssClasses_.UNALIGNED)) {                              // 1127
      this.outline_.classList.add(this.CssClasses_.UNALIGNED);                                       // 1128
    }                                                                                                // 1129
                                                                                                     // 1130
    container.classList.add(this.CssClasses_.IS_UPGRADED);                                           // 1131
  }                                                                                                  // 1132
};                                                                                                   // 1133
                                                                                                     // 1134
/**                                                                                                  // 1135
 * Handles a click on the "for" element, by positioning the menu and then                            // 1136
 * toggling it.                                                                                      // 1137
 * @private                                                                                          // 1138
 */                                                                                                  // 1139
MaterialMenu.prototype.handleForClick_ = function(evt) {                                             // 1140
  'use strict';                                                                                      // 1141
                                                                                                     // 1142
  if (this.element_ && this.forElement_) {                                                           // 1143
    var rect = this.forElement_.getBoundingClientRect();                                             // 1144
    var forRect = this.forElement_.parentElement.getBoundingClientRect();                            // 1145
                                                                                                     // 1146
    if (this.element_.classList.contains(this.CssClasses_.UNALIGNED)) {                              // 1147
      // Do not position the menu automatically. Requires the developer to                           // 1148
      // manually specify position.                                                                  // 1149
    } else if (this.element_.classList.contains(                                                     // 1150
        this.CssClasses_.BOTTOM_RIGHT)) {                                                            // 1151
      // Position below the "for" element, aligned to its right.                                     // 1152
      this.container_.style.right = (forRect.right - rect.right) + 'px';                             // 1153
      this.container_.style.top =                                                                    // 1154
          this.forElement_.offsetTop + this.forElement_.offsetHeight + 'px';                         // 1155
    } else if (this.element_.classList.contains(this.CssClasses_.TOP_LEFT)) {                        // 1156
      // Position above the "for" element, aligned to its left.                                      // 1157
      this.container_.style.left = this.forElement_.offsetLeft + 'px';                               // 1158
      this.container_.style.bottom = (forRect.bottom - rect.top) + 'px';                             // 1159
    } else if (this.element_.classList.contains(this.CssClasses_.TOP_RIGHT)) {                       // 1160
      // Position above the "for" element, aligned to its right.                                     // 1161
      this.container_.style.right = (forRect.right - rect.right) + 'px';                             // 1162
      this.container_.style.bottom = (forRect.bottom - rect.top) + 'px';                             // 1163
    } else {                                                                                         // 1164
      // Default: position below the "for" element, aligned to its left.                             // 1165
      this.container_.style.left = this.forElement_.offsetLeft + 'px';                               // 1166
      this.container_.style.top =                                                                    // 1167
          this.forElement_.offsetTop + this.forElement_.offsetHeight + 'px';                         // 1168
    }                                                                                                // 1169
  }                                                                                                  // 1170
                                                                                                     // 1171
  this.toggle(evt);                                                                                  // 1172
};                                                                                                   // 1173
                                                                                                     // 1174
/**                                                                                                  // 1175
 * Handles a keyboard event on the "for" element.                                                    // 1176
 * @private                                                                                          // 1177
 */                                                                                                  // 1178
MaterialMenu.prototype.handleForKeyboardEvent_ = function(evt) {                                     // 1179
  'use strict';                                                                                      // 1180
                                                                                                     // 1181
  if (this.element_ && this.container_ && this.forElement_) {                                        // 1182
    var items = this.element_.querySelectorAll('.' + this.CssClasses_.ITEM +                         // 1183
      ':not([disabled])');                                                                           // 1184
                                                                                                     // 1185
    if (items && items.length > 0 &&                                                                 // 1186
        this.container_.classList.contains(this.CssClasses_.IS_VISIBLE)) {                           // 1187
      if (evt.keyCode === this.Keycodes_.UP_ARROW) {                                                 // 1188
        evt.preventDefault();                                                                        // 1189
        items[items.length - 1].focus();                                                             // 1190
      } else if (evt.keyCode === this.Keycodes_.DOWN_ARROW) {                                        // 1191
        evt.preventDefault();                                                                        // 1192
        items[0].focus();                                                                            // 1193
      }                                                                                              // 1194
    }                                                                                                // 1195
  }                                                                                                  // 1196
};                                                                                                   // 1197
                                                                                                     // 1198
/**                                                                                                  // 1199
 * Handles a keyboard event on an item.                                                              // 1200
 * @private                                                                                          // 1201
 */                                                                                                  // 1202
MaterialMenu.prototype.handleItemKeyboardEvent_ = function(evt) {                                    // 1203
  'use strict';                                                                                      // 1204
                                                                                                     // 1205
  if (this.element_ && this.container_) {                                                            // 1206
    var items = this.element_.querySelectorAll('.' + this.CssClasses_.ITEM +                         // 1207
      ':not([disabled])');                                                                           // 1208
                                                                                                     // 1209
    if (items && items.length > 0 &&                                                                 // 1210
        this.container_.classList.contains(this.CssClasses_.IS_VISIBLE)) {                           // 1211
      var currentIndex = Array.prototype.slice.call(items).indexOf(evt.target);                      // 1212
                                                                                                     // 1213
      if (evt.keyCode === this.Keycodes_.UP_ARROW) {                                                 // 1214
        evt.preventDefault();                                                                        // 1215
        if (currentIndex > 0) {                                                                      // 1216
          items[currentIndex - 1].focus();                                                           // 1217
        } else {                                                                                     // 1218
          items[items.length - 1].focus();                                                           // 1219
        }                                                                                            // 1220
      } else if (evt.keyCode === this.Keycodes_.DOWN_ARROW) {                                        // 1221
        evt.preventDefault();                                                                        // 1222
        if (items.length > currentIndex + 1) {                                                       // 1223
          items[currentIndex + 1].focus();                                                           // 1224
        } else {                                                                                     // 1225
          items[0].focus();                                                                          // 1226
        }                                                                                            // 1227
      } else if (evt.keyCode === this.Keycodes_.SPACE ||                                             // 1228
            evt.keyCode === this.Keycodes_.ENTER) {                                                  // 1229
        evt.preventDefault();                                                                        // 1230
        // Send mousedown and mouseup to trigger ripple.                                             // 1231
        var e = new MouseEvent('mousedown');                                                         // 1232
        evt.target.dispatchEvent(e);                                                                 // 1233
        e = new MouseEvent('mouseup');                                                               // 1234
        evt.target.dispatchEvent(e);                                                                 // 1235
        // Send click.                                                                               // 1236
        evt.target.click();                                                                          // 1237
      } else if (evt.keyCode === this.Keycodes_.ESCAPE) {                                            // 1238
        evt.preventDefault();                                                                        // 1239
        this.hide();                                                                                 // 1240
      }                                                                                              // 1241
    }                                                                                                // 1242
  }                                                                                                  // 1243
};                                                                                                   // 1244
                                                                                                     // 1245
/**                                                                                                  // 1246
 * Handles a click event on an item.                                                                 // 1247
 * @private                                                                                          // 1248
 */                                                                                                  // 1249
MaterialMenu.prototype.handleItemClick_ = function(evt) {                                            // 1250
  'use strict';                                                                                      // 1251
                                                                                                     // 1252
  if (evt.target.getAttribute('disabled') !== null) {                                                // 1253
    evt.stopPropagation();                                                                           // 1254
  } else {                                                                                           // 1255
    // Wait some time before closing menu, so the user can see the ripple.                           // 1256
    this.closing_ = true;                                                                            // 1257
    window.setTimeout(function(evt) {                                                                // 1258
      this.hide();                                                                                   // 1259
      this.closing_ = false;                                                                         // 1260
    }.bind(this), this.Constant_.CLOSE_TIMEOUT);                                                     // 1261
  }                                                                                                  // 1262
};                                                                                                   // 1263
                                                                                                     // 1264
/**                                                                                                  // 1265
 * Calculates the initial clip (for opening the menu) or final clip (for closing                     // 1266
 * it), and applies it. This allows us to animate from or to the correct point,                      // 1267
 * that is, the point it's aligned to in the "for" element.                                          // 1268
 * @private                                                                                          // 1269
 */                                                                                                  // 1270
MaterialMenu.prototype.applyClip_ = function(height, width) {                                        // 1271
  'use strict';                                                                                      // 1272
                                                                                                     // 1273
  if (this.element_.classList.contains(this.CssClasses_.UNALIGNED)) {                                // 1274
    // Do not clip.                                                                                  // 1275
    this.element_.style.clip = null;                                                                 // 1276
  } else if (this.element_.classList.contains(this.CssClasses_.BOTTOM_RIGHT)) {                      // 1277
    // Clip to the top right corner of the menu.                                                     // 1278
    this.element_.style.clip =                                                                       // 1279
        'rect(0 ' + width + 'px ' + '0 ' + width + 'px)';                                            // 1280
  } else if (this.element_.classList.contains(this.CssClasses_.TOP_LEFT)) {                          // 1281
    // Clip to the bottom left corner of the menu.                                                   // 1282
    this.element_.style.clip =                                                                       // 1283
        'rect(' + height + 'px 0 ' + height + 'px 0)';                                               // 1284
  } else if (this.element_.classList.contains(this.CssClasses_.TOP_RIGHT)) {                         // 1285
    // Clip to the bottom right corner of the menu.                                                  // 1286
    this.element_.style.clip = 'rect(' + height + 'px ' + width + 'px ' +                            // 1287
        height + 'px ' + width + 'px)';                                                              // 1288
  } else {                                                                                           // 1289
    // Default: do not clip (same as clipping to the top left corner).                               // 1290
    this.element_.style.clip = null;                                                                 // 1291
  }                                                                                                  // 1292
};                                                                                                   // 1293
                                                                                                     // 1294
/**                                                                                                  // 1295
 * Adds an event listener to clean up after the animation ends.                                      // 1296
 * @private                                                                                          // 1297
 */                                                                                                  // 1298
MaterialMenu.prototype.addAnimationEndListener_ = function() {                                       // 1299
  'use strict';                                                                                      // 1300
                                                                                                     // 1301
  var cleanup = function() {                                                                         // 1302
    this.element_.classList.remove(this.CssClasses_.IS_ANIMATING);                                   // 1303
  }.bind(this);                                                                                      // 1304
                                                                                                     // 1305
  // Remove animation class once the transition is done.                                             // 1306
  this.element_.addEventListener('transitionend', cleanup);                                          // 1307
  this.element_.addEventListener('webkitTransitionEnd', cleanup);                                    // 1308
};                                                                                                   // 1309
                                                                                                     // 1310
/**                                                                                                  // 1311
 * Displays the menu.                                                                                // 1312
 * @public                                                                                           // 1313
 */                                                                                                  // 1314
MaterialMenu.prototype.show = function(evt) {                                                        // 1315
  'use strict';                                                                                      // 1316
                                                                                                     // 1317
  if (this.element_ && this.container_ && this.outline_) {                                           // 1318
    // Measure the inner element.                                                                    // 1319
    var height = this.element_.getBoundingClientRect().height;                                       // 1320
    var width = this.element_.getBoundingClientRect().width;                                         // 1321
                                                                                                     // 1322
    // Apply the inner element's size to the container and outline.                                  // 1323
    this.container_.style.width = width + 'px';                                                      // 1324
    this.container_.style.height = height + 'px';                                                    // 1325
    this.outline_.style.width = width + 'px';                                                        // 1326
    this.outline_.style.height = height + 'px';                                                      // 1327
                                                                                                     // 1328
    var transitionDuration = this.Constant_.TRANSITION_DURATION_SECONDS *                            // 1329
        this.Constant_.TRANSITION_DURATION_FRACTION;                                                 // 1330
                                                                                                     // 1331
    // Calculate transition delays for individual menu items, so that they fade                      // 1332
    // in one at a time.                                                                             // 1333
    var items = this.element_.querySelectorAll('.' + this.CssClasses_.ITEM);                         // 1334
    for (var i = 0; i < items.length; i++) {                                                         // 1335
      var itemDelay = null;                                                                          // 1336
      if (this.element_.classList.contains(this.CssClasses_.TOP_LEFT) ||                             // 1337
          this.element_.classList.contains(this.CssClasses_.TOP_RIGHT)) {                            // 1338
        itemDelay = ((height - items[i].offsetTop - items[i].offsetHeight) /                         // 1339
            height * transitionDuration) + 's';                                                      // 1340
      } else {                                                                                       // 1341
        itemDelay = (items[i].offsetTop / height * transitionDuration) + 's';                        // 1342
      }                                                                                              // 1343
      items[i].style.transitionDelay = itemDelay;                                                    // 1344
    }                                                                                                // 1345
                                                                                                     // 1346
    // Apply the initial clip to the text before we start animating.                                 // 1347
    this.applyClip_(height, width);                                                                  // 1348
                                                                                                     // 1349
    // Wait for the next frame, turn on animation, and apply the final clip.                         // 1350
    // Also make it visible. This triggers the transitions.                                          // 1351
    window.requestAnimationFrame(function() {                                                        // 1352
      this.element_.classList.add(this.CssClasses_.IS_ANIMATING);                                    // 1353
      this.element_.style.clip = 'rect(0 ' + width + 'px ' + height + 'px 0)';                       // 1354
      this.container_.classList.add(this.CssClasses_.IS_VISIBLE);                                    // 1355
    }.bind(this));                                                                                   // 1356
                                                                                                     // 1357
    // Clean up after the animation is complete.                                                     // 1358
    this.addAnimationEndListener_();                                                                 // 1359
                                                                                                     // 1360
    // Add a click listener to the document, to close the menu.                                      // 1361
    var callback = function(e) {                                                                     // 1362
      // Check to see if the document is processing the same event that                              // 1363
      // displayed the menu in the first place. If so, do nothing.                                   // 1364
      // Also check to see if the menu is in the process of closing itself, and                      // 1365
      // do nothing in that case.                                                                    // 1366
      if (e !== evt && !this.closing_) {                                                             // 1367
        document.removeEventListener('click', callback);                                             // 1368
        this.hide();                                                                                 // 1369
      }                                                                                              // 1370
    }.bind(this);                                                                                    // 1371
    document.addEventListener('click', callback);                                                    // 1372
  }                                                                                                  // 1373
};                                                                                                   // 1374
                                                                                                     // 1375
/**                                                                                                  // 1376
 * Hides the menu.                                                                                   // 1377
 * @public                                                                                           // 1378
 */                                                                                                  // 1379
MaterialMenu.prototype.hide = function() {                                                           // 1380
  'use strict';                                                                                      // 1381
                                                                                                     // 1382
  if (this.element_ && this.container_ && this.outline_) {                                           // 1383
    var items = this.element_.querySelectorAll('.' + this.CssClasses_.ITEM);                         // 1384
                                                                                                     // 1385
    // Remove all transition delays; menu items fade out concurrently.                               // 1386
    for (var i = 0; i < items.length; i++) {                                                         // 1387
      items[i].style.transitionDelay = null;                                                         // 1388
    }                                                                                                // 1389
                                                                                                     // 1390
    // Measure the inner element.                                                                    // 1391
    var height = this.element_.getBoundingClientRect().height;                                       // 1392
    var width = this.element_.getBoundingClientRect().width;                                         // 1393
                                                                                                     // 1394
    // Turn on animation, and apply the final clip. Also make invisible.                             // 1395
    // This triggers the transitions.                                                                // 1396
    this.element_.classList.add(this.CssClasses_.IS_ANIMATING);                                      // 1397
    this.applyClip_(height, width);                                                                  // 1398
    this.container_.classList.remove(this.CssClasses_.IS_VISIBLE);                                   // 1399
                                                                                                     // 1400
    // Clean up after the animation is complete.                                                     // 1401
    this.addAnimationEndListener_();                                                                 // 1402
  }                                                                                                  // 1403
};                                                                                                   // 1404
                                                                                                     // 1405
/**                                                                                                  // 1406
 * Displays or hides the menu, depending on current state.                                           // 1407
 * @public                                                                                           // 1408
 */                                                                                                  // 1409
MaterialMenu.prototype.toggle = function(evt) {                                                      // 1410
  'use strict';                                                                                      // 1411
                                                                                                     // 1412
  if (this.container_.classList.contains(this.CssClasses_.IS_VISIBLE)) {                             // 1413
    this.hide();                                                                                     // 1414
  } else {                                                                                           // 1415
    this.show(evt);                                                                                  // 1416
  }                                                                                                  // 1417
};                                                                                                   // 1418
                                                                                                     // 1419
// The component registers itself. It can assume componentHandler is available                       // 1420
// in the global scope.                                                                              // 1421
componentHandler.register({                                                                          // 1422
  constructor: MaterialMenu,                                                                         // 1423
  classAsString: 'MaterialMenu',                                                                     // 1424
  cssClass: 'mdl-js-menu'                                                                            // 1425
});                                                                                                  // 1426
                                                                                                     // 1427
/**                                                                                                  // 1428
 * @license                                                                                          // 1429
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 1430
 *                                                                                                   // 1431
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 1432
 * you may not use this file except in compliance with the License.                                  // 1433
 * You may obtain a copy of the License at                                                           // 1434
 *                                                                                                   // 1435
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 1436
 *                                                                                                   // 1437
 * Unless required by applicable law or agreed to in writing, software                               // 1438
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 1439
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 1440
 * See the License for the specific language governing permissions and                               // 1441
 * limitations under the License.                                                                    // 1442
 */                                                                                                  // 1443
                                                                                                     // 1444
/**                                                                                                  // 1445
 * Class constructor for Progress MDL component.                                                     // 1446
 * Implements MDL component design pattern defined at:                                               // 1447
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 1448
 * @param {HTMLElement} element The element that will be upgraded.                                   // 1449
 */                                                                                                  // 1450
function MaterialProgress(element) {                                                                 // 1451
  'use strict';                                                                                      // 1452
                                                                                                     // 1453
  this.element_ = element;                                                                           // 1454
                                                                                                     // 1455
  // Initialize instance.                                                                            // 1456
  this.init();                                                                                       // 1457
}                                                                                                    // 1458
                                                                                                     // 1459
/**                                                                                                  // 1460
 * Store constants in one place so they can be updated easily.                                       // 1461
 * @enum {string | number}                                                                           // 1462
 * @private                                                                                          // 1463
 */                                                                                                  // 1464
MaterialProgress.prototype.Constant_ = {                                                             // 1465
};                                                                                                   // 1466
                                                                                                     // 1467
/**                                                                                                  // 1468
 * Store strings for class names defined by this component that are used in                          // 1469
 * JavaScript. This allows us to simply change it in one place should we                             // 1470
 * decide to modify at a later date.                                                                 // 1471
 * @enum {string}                                                                                    // 1472
 * @private                                                                                          // 1473
 */                                                                                                  // 1474
MaterialProgress.prototype.CssClasses_ = {                                                           // 1475
  INDETERMINATE_CLASS: 'mdl-progress__indeterminate'                                                 // 1476
};                                                                                                   // 1477
                                                                                                     // 1478
MaterialProgress.prototype.setProgress = function(p) {                                               // 1479
  'use strict';                                                                                      // 1480
                                                                                                     // 1481
  if (this.element_.classList.contains(this.CssClasses_.INDETERMINATE_CLASS)) {                      // 1482
    return;                                                                                          // 1483
  }                                                                                                  // 1484
                                                                                                     // 1485
  this.progressbar_.style.width = p + '%';                                                           // 1486
};                                                                                                   // 1487
                                                                                                     // 1488
MaterialProgress.prototype.setBuffer = function(p) {                                                 // 1489
  'use strict';                                                                                      // 1490
                                                                                                     // 1491
  this.bufferbar_.style.width = p + '%';                                                             // 1492
  this.auxbar_.style.width = (100 - p) + '%';                                                        // 1493
};                                                                                                   // 1494
                                                                                                     // 1495
/**                                                                                                  // 1496
 * Initialize element.                                                                               // 1497
 */                                                                                                  // 1498
MaterialProgress.prototype.init = function() {                                                       // 1499
  'use strict';                                                                                      // 1500
                                                                                                     // 1501
  if (this.element_) {                                                                               // 1502
    var el = document.createElement('div');                                                          // 1503
    el.className = 'progressbar bar bar1';                                                           // 1504
    this.element_.appendChild(el);                                                                   // 1505
    this.progressbar_ = el;                                                                          // 1506
                                                                                                     // 1507
    el = document.createElement('div');                                                              // 1508
    el.className = 'bufferbar bar bar2';                                                             // 1509
    this.element_.appendChild(el);                                                                   // 1510
    this.bufferbar_ = el;                                                                            // 1511
                                                                                                     // 1512
    el = document.createElement('div');                                                              // 1513
    el.className = 'auxbar bar bar3';                                                                // 1514
    this.element_.appendChild(el);                                                                   // 1515
    this.auxbar_ = el;                                                                               // 1516
                                                                                                     // 1517
    this.progressbar_.style.width = '0%';                                                            // 1518
    this.bufferbar_.style.width = '100%';                                                            // 1519
    this.auxbar_.style.width = '0%';                                                                 // 1520
                                                                                                     // 1521
    this.element_.classList.add('is-upgraded');                                                      // 1522
  }                                                                                                  // 1523
};                                                                                                   // 1524
                                                                                                     // 1525
// The component registers itself. It can assume componentHandler is available                       // 1526
// in the global scope.                                                                              // 1527
componentHandler.register({                                                                          // 1528
  constructor: MaterialProgress,                                                                     // 1529
  classAsString: 'MaterialProgress',                                                                 // 1530
  cssClass: 'mdl-js-progress'                                                                        // 1531
});                                                                                                  // 1532
                                                                                                     // 1533
/**                                                                                                  // 1534
 * @license                                                                                          // 1535
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 1536
 *                                                                                                   // 1537
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 1538
 * you may not use this file except in compliance with the License.                                  // 1539
 * You may obtain a copy of the License at                                                           // 1540
 *                                                                                                   // 1541
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 1542
 *                                                                                                   // 1543
 * Unless required by applicable law or agreed to in writing, software                               // 1544
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 1545
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 1546
 * See the License for the specific language governing permissions and                               // 1547
 * limitations under the License.                                                                    // 1548
 */                                                                                                  // 1549
                                                                                                     // 1550
/**                                                                                                  // 1551
 * Class constructor for Radio MDL component.                                                        // 1552
 * Implements MDL component design pattern defined at:                                               // 1553
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 1554
 * @param {HTMLElement} element The element that will be upgraded.                                   // 1555
 */                                                                                                  // 1556
function MaterialRadio(element) {                                                                    // 1557
  'use strict';                                                                                      // 1558
                                                                                                     // 1559
  this.element_ = element;                                                                           // 1560
                                                                                                     // 1561
  // Initialize instance.                                                                            // 1562
  this.init();                                                                                       // 1563
}                                                                                                    // 1564
                                                                                                     // 1565
/**                                                                                                  // 1566
 * Store constants in one place so they can be updated easily.                                       // 1567
 * @enum {string | number}                                                                           // 1568
 * @private                                                                                          // 1569
 */                                                                                                  // 1570
MaterialRadio.prototype.Constant_ = {                                                                // 1571
  TINY_TIMEOUT: 0.001                                                                                // 1572
};                                                                                                   // 1573
                                                                                                     // 1574
/**                                                                                                  // 1575
 * Store strings for class names defined by this component that are used in                          // 1576
 * JavaScript. This allows us to simply change it in one place should we                             // 1577
 * decide to modify at a later date.                                                                 // 1578
 * @enum {string}                                                                                    // 1579
 * @private                                                                                          // 1580
 */                                                                                                  // 1581
MaterialRadio.prototype.CssClasses_ = {                                                              // 1582
  IS_FOCUSED: 'is-focused',                                                                          // 1583
  IS_DISABLED: 'is-disabled',                                                                        // 1584
  IS_CHECKED: 'is-checked',                                                                          // 1585
  IS_UPGRADED: 'is-upgraded',                                                                        // 1586
  JS_RADIO: 'mdl-js-radio',                                                                          // 1587
  RADIO_BTN: 'mdl-radio__button',                                                                    // 1588
  RADIO_OUTER_CIRCLE: 'mdl-radio__outer-circle',                                                     // 1589
  RADIO_INNER_CIRCLE: 'mdl-radio__inner-circle',                                                     // 1590
  RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                             // 1591
  RIPPLE_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events',                                       // 1592
  RIPPLE_CONTAINER: 'mdl-radio__ripple-container',                                                   // 1593
  RIPPLE_CENTER: 'mdl-ripple--center',                                                               // 1594
  RIPPLE: 'mdl-ripple'                                                                               // 1595
};                                                                                                   // 1596
                                                                                                     // 1597
/**                                                                                                  // 1598
 * Handle change of state.                                                                           // 1599
 * @param {Event} event The event that fired.                                                        // 1600
 * @private                                                                                          // 1601
 */                                                                                                  // 1602
MaterialRadio.prototype.onChange_ = function(event) {                                                // 1603
  'use strict';                                                                                      // 1604
                                                                                                     // 1605
  this.updateClasses_(this.btnElement_, this.element_);                                              // 1606
                                                                                                     // 1607
  // Since other radio buttons don't get change events, we need to look for                          // 1608
  // them to update their classes.                                                                   // 1609
  var radios = document.getElementsByClassName(this.CssClasses_.JS_RADIO);                           // 1610
  for (var i = 0; i < radios.length; i++) {                                                          // 1611
    var button = radios[i].querySelector('.' + this.CssClasses_.RADIO_BTN);                          // 1612
    // Different name == different group, so no point updating those.                                // 1613
    if (button.getAttribute('name') === this.btnElement_.getAttribute('name')) {                     // 1614
      this.updateClasses_(button, radios[i]);                                                        // 1615
    }                                                                                                // 1616
  }                                                                                                  // 1617
};                                                                                                   // 1618
                                                                                                     // 1619
/**                                                                                                  // 1620
 * Handle focus.                                                                                     // 1621
 * @param {Event} event The event that fired.                                                        // 1622
 * @private                                                                                          // 1623
 */                                                                                                  // 1624
MaterialRadio.prototype.onFocus_ = function(event) {                                                 // 1625
  'use strict';                                                                                      // 1626
                                                                                                     // 1627
  this.element_.classList.add(this.CssClasses_.IS_FOCUSED);                                          // 1628
};                                                                                                   // 1629
                                                                                                     // 1630
/**                                                                                                  // 1631
 * Handle lost focus.                                                                                // 1632
 * @param {Event} event The event that fired.                                                        // 1633
 * @private                                                                                          // 1634
 */                                                                                                  // 1635
MaterialRadio.prototype.onBlur_ = function(event) {                                                  // 1636
  'use strict';                                                                                      // 1637
                                                                                                     // 1638
  this.element_.classList.remove(this.CssClasses_.IS_FOCUSED);                                       // 1639
};                                                                                                   // 1640
                                                                                                     // 1641
/**                                                                                                  // 1642
 * Handle mouseup.                                                                                   // 1643
 * @param {Event} event The event that fired.                                                        // 1644
 * @private                                                                                          // 1645
 */                                                                                                  // 1646
MaterialRadio.prototype.onMouseup_ = function(event) {                                               // 1647
  'use strict';                                                                                      // 1648
                                                                                                     // 1649
  this.blur_();                                                                                      // 1650
};                                                                                                   // 1651
                                                                                                     // 1652
/**                                                                                                  // 1653
 * Update classes.                                                                                   // 1654
 * @param {HTMLElement} button The button whose classes we should update.                            // 1655
 * @param {HTMLElement} label The label whose classes we should update.                              // 1656
 * @private                                                                                          // 1657
 */                                                                                                  // 1658
MaterialRadio.prototype.updateClasses_ = function(button, label) {                                   // 1659
  'use strict';                                                                                      // 1660
                                                                                                     // 1661
  if (button.disabled) {                                                                             // 1662
    label.classList.add(this.CssClasses_.IS_DISABLED);                                               // 1663
  } else {                                                                                           // 1664
    label.classList.remove(this.CssClasses_.IS_DISABLED);                                            // 1665
  }                                                                                                  // 1666
                                                                                                     // 1667
  if (button.checked) {                                                                              // 1668
    label.classList.add(this.CssClasses_.IS_CHECKED);                                                // 1669
  } else {                                                                                           // 1670
    label.classList.remove(this.CssClasses_.IS_CHECKED);                                             // 1671
  }                                                                                                  // 1672
};                                                                                                   // 1673
                                                                                                     // 1674
/**                                                                                                  // 1675
 * Add blur.                                                                                         // 1676
 * @private                                                                                          // 1677
 */                                                                                                  // 1678
MaterialRadio.prototype.blur_ = function(event) {                                                    // 1679
  'use strict';                                                                                      // 1680
                                                                                                     // 1681
  // TODO: figure out why there's a focus event being fired after our blur,                          // 1682
  // so that we can avoid this hack.                                                                 // 1683
  window.setTimeout(function() {                                                                     // 1684
    this.btnElement_.blur();                                                                         // 1685
  }.bind(this), this.Constant_.TINY_TIMEOUT);                                                        // 1686
};                                                                                                   // 1687
                                                                                                     // 1688
// Public methods.                                                                                   // 1689
                                                                                                     // 1690
/**                                                                                                  // 1691
 * Disable radio.                                                                                    // 1692
 * @public                                                                                           // 1693
 */                                                                                                  // 1694
MaterialRadio.prototype.disable = function() {                                                       // 1695
  'use strict';                                                                                      // 1696
                                                                                                     // 1697
  this.btnElement_.disabled = true;                                                                  // 1698
  this.updateClasses_(this.btnElement_, this.element_);                                              // 1699
};                                                                                                   // 1700
                                                                                                     // 1701
/**                                                                                                  // 1702
 * Enable radio.                                                                                     // 1703
 * @public                                                                                           // 1704
 */                                                                                                  // 1705
MaterialRadio.prototype.enable = function() {                                                        // 1706
  'use strict';                                                                                      // 1707
                                                                                                     // 1708
  this.btnElement_.disabled = false;                                                                 // 1709
  this.updateClasses_(this.btnElement_, this.element_);                                              // 1710
};                                                                                                   // 1711
                                                                                                     // 1712
/**                                                                                                  // 1713
 * Check radio.                                                                                      // 1714
 * @public                                                                                           // 1715
 */                                                                                                  // 1716
MaterialRadio.prototype.check = function() {                                                         // 1717
  'use strict';                                                                                      // 1718
                                                                                                     // 1719
  this.btnElement_.checked = true;                                                                   // 1720
  this.updateClasses_(this.btnElement_, this.element_);                                              // 1721
};                                                                                                   // 1722
                                                                                                     // 1723
/**                                                                                                  // 1724
 * Uncheck radio.                                                                                    // 1725
 * @public                                                                                           // 1726
 */                                                                                                  // 1727
MaterialRadio.prototype.uncheck = function() {                                                       // 1728
  'use strict';                                                                                      // 1729
                                                                                                     // 1730
  this.btnElement_.checked = false;                                                                  // 1731
  this.updateClasses_(this.btnElement_, this.element_);                                              // 1732
};                                                                                                   // 1733
                                                                                                     // 1734
/**                                                                                                  // 1735
 * Initialize element.                                                                               // 1736
 */                                                                                                  // 1737
MaterialRadio.prototype.init = function() {                                                          // 1738
  'use strict';                                                                                      // 1739
                                                                                                     // 1740
  if (this.element_) {                                                                               // 1741
    this.btnElement_ = this.element_.querySelector('.' +                                             // 1742
        this.CssClasses_.RADIO_BTN);                                                                 // 1743
                                                                                                     // 1744
    var outerCircle = document.createElement('span');                                                // 1745
    outerCircle.classList.add(this.CssClasses_.RADIO_OUTER_CIRCLE);                                  // 1746
                                                                                                     // 1747
    var innerCircle = document.createElement('span');                                                // 1748
    innerCircle.classList.add(this.CssClasses_.RADIO_INNER_CIRCLE);                                  // 1749
                                                                                                     // 1750
    this.element_.appendChild(outerCircle);                                                          // 1751
    this.element_.appendChild(innerCircle);                                                          // 1752
                                                                                                     // 1753
    var rippleContainer;                                                                             // 1754
    if (this.element_.classList.contains(                                                            // 1755
        this.CssClasses_.RIPPLE_EFFECT)) {                                                           // 1756
      this.element_.classList.add(                                                                   // 1757
          this.CssClasses_.RIPPLE_IGNORE_EVENTS);                                                    // 1758
      rippleContainer = document.createElement('span');                                              // 1759
      rippleContainer.classList.add(                                                                 // 1760
          this.CssClasses_.RIPPLE_CONTAINER);                                                        // 1761
      rippleContainer.classList.add(this.CssClasses_.RIPPLE_EFFECT);                                 // 1762
      rippleContainer.classList.add(this.CssClasses_.RIPPLE_CENTER);                                 // 1763
      rippleContainer.addEventListener('mouseup', this.onMouseup_.bind(this));                       // 1764
                                                                                                     // 1765
      var ripple = document.createElement('span');                                                   // 1766
      ripple.classList.add(this.CssClasses_.RIPPLE);                                                 // 1767
                                                                                                     // 1768
      rippleContainer.appendChild(ripple);                                                           // 1769
      this.element_.appendChild(rippleContainer);                                                    // 1770
    }                                                                                                // 1771
                                                                                                     // 1772
    this.btnElement_.addEventListener('change', this.onChange_.bind(this));                          // 1773
    this.btnElement_.addEventListener('focus', this.onFocus_.bind(this));                            // 1774
    this.btnElement_.addEventListener('blur', this.onBlur_.bind(this));                              // 1775
    this.element_.addEventListener('mouseup', this.onMouseup_.bind(this));                           // 1776
                                                                                                     // 1777
    this.updateClasses_(this.btnElement_, this.element_);                                            // 1778
    this.element_.classList.add(this.CssClasses_.IS_UPGRADED);                                       // 1779
  }                                                                                                  // 1780
};                                                                                                   // 1781
                                                                                                     // 1782
// The component registers itself. It can assume componentHandler is available                       // 1783
// in the global scope.                                                                              // 1784
componentHandler.register({                                                                          // 1785
  constructor: MaterialRadio,                                                                        // 1786
  classAsString: 'MaterialRadio',                                                                    // 1787
  cssClass: 'mdl-js-radio'                                                                           // 1788
});                                                                                                  // 1789
                                                                                                     // 1790
/**                                                                                                  // 1791
 * @license                                                                                          // 1792
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 1793
 *                                                                                                   // 1794
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 1795
 * you may not use this file except in compliance with the License.                                  // 1796
 * You may obtain a copy of the License at                                                           // 1797
 *                                                                                                   // 1798
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 1799
 *                                                                                                   // 1800
 * Unless required by applicable law or agreed to in writing, software                               // 1801
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 1802
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 1803
 * See the License for the specific language governing permissions and                               // 1804
 * limitations under the License.                                                                    // 1805
 */                                                                                                  // 1806
                                                                                                     // 1807
/**                                                                                                  // 1808
 * Class constructor for Slider MDL component.                                                       // 1809
 * Implements MDL component design pattern defined at:                                               // 1810
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 1811
 * @param {HTMLElement} element The element that will be upgraded.                                   // 1812
 */                                                                                                  // 1813
function MaterialSlider(element) {                                                                   // 1814
  'use strict';                                                                                      // 1815
                                                                                                     // 1816
  this.element_ = element;                                                                           // 1817
  // Browser feature detection.                                                                      // 1818
  this.isIE_ = window.navigator.msPointerEnabled;                                                    // 1819
  // Initialize instance.                                                                            // 1820
  this.init();                                                                                       // 1821
}                                                                                                    // 1822
                                                                                                     // 1823
/**                                                                                                  // 1824
 * Store constants in one place so they can be updated easily.                                       // 1825
 * @enum {string | number}                                                                           // 1826
 * @private                                                                                          // 1827
 */                                                                                                  // 1828
MaterialSlider.prototype.Constant_ = {                                                               // 1829
  // None for now.                                                                                   // 1830
};                                                                                                   // 1831
                                                                                                     // 1832
/**                                                                                                  // 1833
 * Store strings for class names defined by this component that are used in                          // 1834
 * JavaScript. This allows us to simply change it in one place should we                             // 1835
 * decide to modify at a later date.                                                                 // 1836
 * @enum {string}                                                                                    // 1837
 * @private                                                                                          // 1838
 */                                                                                                  // 1839
MaterialSlider.prototype.CssClasses_ = {                                                             // 1840
  IE_CONTAINER: 'mdl-slider__ie-container',                                                          // 1841
  SLIDER_CONTAINER: 'mdl-slider__container',                                                         // 1842
  BACKGROUND_FLEX: 'mdl-slider__background-flex',                                                    // 1843
  BACKGROUND_LOWER: 'mdl-slider__background-lower',                                                  // 1844
  BACKGROUND_UPPER: 'mdl-slider__background-upper',                                                  // 1845
  IS_LOWEST_VALUE: 'is-lowest-value',                                                                // 1846
  IS_UPGRADED: 'is-upgraded'                                                                         // 1847
};                                                                                                   // 1848
                                                                                                     // 1849
/**                                                                                                  // 1850
 * Handle input on element.                                                                          // 1851
 * @param {Event} event The event that fired.                                                        // 1852
 * @private                                                                                          // 1853
 */                                                                                                  // 1854
MaterialSlider.prototype.onInput_ = function(event) {                                                // 1855
  'use strict';                                                                                      // 1856
                                                                                                     // 1857
  this.updateValueStyles_();                                                                         // 1858
};                                                                                                   // 1859
                                                                                                     // 1860
/**                                                                                                  // 1861
 * Handle change on element.                                                                         // 1862
 * @param {Event} event The event that fired.                                                        // 1863
 * @private                                                                                          // 1864
 */                                                                                                  // 1865
MaterialSlider.prototype.onChange_ = function(event) {                                               // 1866
  'use strict';                                                                                      // 1867
                                                                                                     // 1868
  this.updateValueStyles_();                                                                         // 1869
};                                                                                                   // 1870
                                                                                                     // 1871
/**                                                                                                  // 1872
 * Handle mouseup on element.                                                                        // 1873
 * @param {Event} event The event that fired.                                                        // 1874
 * @private                                                                                          // 1875
 */                                                                                                  // 1876
MaterialSlider.prototype.onMouseUp_ = function(event) {                                              // 1877
  'use strict';                                                                                      // 1878
                                                                                                     // 1879
  event.target.blur();                                                                               // 1880
};                                                                                                   // 1881
                                                                                                     // 1882
/**                                                                                                  // 1883
 * Handle mousedown on container element.                                                            // 1884
 * This handler is purpose is to not require the use to click                                        // 1885
 * exactly on the 2px slider element, as FireFox seems to be very                                    // 1886
 * strict about this.                                                                                // 1887
 * @param {Event} event The event that fired.                                                        // 1888
 * @private                                                                                          // 1889
 */                                                                                                  // 1890
MaterialSlider.prototype.onContainerMouseDown_ = function(event) {                                   // 1891
  'use strict';                                                                                      // 1892
                                                                                                     // 1893
  // If this click is not on the parent element (but rather some child)                              // 1894
  // ignore. It may still bubble up.                                                                 // 1895
  if (event.target !== this.element_.parentElement) {                                                // 1896
    return;                                                                                          // 1897
  }                                                                                                  // 1898
                                                                                                     // 1899
  // Discard the original event and create a new event that                                          // 1900
  // is on the slider element.                                                                       // 1901
  event.preventDefault();                                                                            // 1902
  var newEvent = new MouseEvent('mousedown', {                                                       // 1903
    target: event.target,                                                                            // 1904
    buttons: event.buttons,                                                                          // 1905
    clientX: event.clientX,                                                                          // 1906
    clientY: this.element_.getBoundingClientRect().y                                                 // 1907
  });                                                                                                // 1908
  this.element_.dispatchEvent(newEvent);                                                             // 1909
};                                                                                                   // 1910
                                                                                                     // 1911
/**                                                                                                  // 1912
 * Handle updating of values.                                                                        // 1913
 * @param {Event} event The event that fired.                                                        // 1914
 * @private                                                                                          // 1915
 */                                                                                                  // 1916
MaterialSlider.prototype.updateValueStyles_ = function(event) {                                      // 1917
  'use strict';                                                                                      // 1918
                                                                                                     // 1919
  // Calculate and apply percentages to div structure behind slider.                                 // 1920
  var fraction = (this.element_.value - this.element_.min) /                                         // 1921
      (this.element_.max - this.element_.min);                                                       // 1922
                                                                                                     // 1923
  if (fraction === 0) {                                                                              // 1924
    this.element_.classList.add(this.CssClasses_.IS_LOWEST_VALUE);                                   // 1925
  } else {                                                                                           // 1926
    this.element_.classList.remove(this.CssClasses_.IS_LOWEST_VALUE);                                // 1927
  }                                                                                                  // 1928
                                                                                                     // 1929
  if (!this.isIE_) {                                                                                 // 1930
    this.backgroundLower_.style.flex = fraction;                                                     // 1931
    this.backgroundLower_.style.webkitFlex = fraction;                                               // 1932
    this.backgroundUpper_.style.flex = 1 - fraction;                                                 // 1933
    this.backgroundUpper_.style.webkitFlex = 1 - fraction;                                           // 1934
  }                                                                                                  // 1935
};                                                                                                   // 1936
                                                                                                     // 1937
// Public methods.                                                                                   // 1938
                                                                                                     // 1939
/**                                                                                                  // 1940
 * Disable slider.                                                                                   // 1941
 * @public                                                                                           // 1942
 */                                                                                                  // 1943
MaterialSlider.prototype.disable = function() {                                                      // 1944
  'use strict';                                                                                      // 1945
                                                                                                     // 1946
  this.element_.disabled = true;                                                                     // 1947
};                                                                                                   // 1948
                                                                                                     // 1949
/**                                                                                                  // 1950
 * Enable slider.                                                                                    // 1951
 * @public                                                                                           // 1952
 */                                                                                                  // 1953
MaterialSlider.prototype.enable = function() {                                                       // 1954
  'use strict';                                                                                      // 1955
                                                                                                     // 1956
  this.element_.disabled = false;                                                                    // 1957
};                                                                                                   // 1958
                                                                                                     // 1959
/**                                                                                                  // 1960
 * Update slider value.                                                                              // 1961
 * @param {Number} value The value to which to set the control (optional).                           // 1962
 * @public                                                                                           // 1963
 */                                                                                                  // 1964
MaterialSlider.prototype.change = function(value) {                                                  // 1965
  'use strict';                                                                                      // 1966
                                                                                                     // 1967
  if (value) {                                                                                       // 1968
    this.element_.value = value;                                                                     // 1969
  }                                                                                                  // 1970
  this.updateValueStyles_();                                                                         // 1971
};                                                                                                   // 1972
                                                                                                     // 1973
/**                                                                                                  // 1974
 * Initialize element.                                                                               // 1975
 */                                                                                                  // 1976
MaterialSlider.prototype.init = function() {                                                         // 1977
  'use strict';                                                                                      // 1978
                                                                                                     // 1979
  if (this.element_) {                                                                               // 1980
    if (this.isIE_) {                                                                                // 1981
      // Since we need to specify a very large height in IE due to                                   // 1982
      // implementation limitations, we add a parent here that trims it down to                      // 1983
      // a reasonable size.                                                                          // 1984
      var containerIE = document.createElement('div');                                               // 1985
      containerIE.classList.add(this.CssClasses_.IE_CONTAINER);                                      // 1986
      this.element_.parentElement.insertBefore(containerIE, this.element_);                          // 1987
      this.element_.parentElement.removeChild(this.element_);                                        // 1988
      containerIE.appendChild(this.element_);                                                        // 1989
    } else {                                                                                         // 1990
      // For non-IE browsers, we need a div structure that sits behind the                           // 1991
      // slider and allows us to style the left and right sides of it with                           // 1992
      // different colors.                                                                           // 1993
      var container = document.createElement('div');                                                 // 1994
      container.classList.add(this.CssClasses_.SLIDER_CONTAINER);                                    // 1995
      this.element_.parentElement.insertBefore(container, this.element_);                            // 1996
      this.element_.parentElement.removeChild(this.element_);                                        // 1997
      container.appendChild(this.element_);                                                          // 1998
      var backgroundFlex = document.createElement('div');                                            // 1999
      backgroundFlex.classList.add(this.CssClasses_.BACKGROUND_FLEX);                                // 2000
      container.appendChild(backgroundFlex);                                                         // 2001
      this.backgroundLower_ = document.createElement('div');                                         // 2002
      this.backgroundLower_.classList.add(this.CssClasses_.BACKGROUND_LOWER);                        // 2003
      backgroundFlex.appendChild(this.backgroundLower_);                                             // 2004
      this.backgroundUpper_ = document.createElement('div');                                         // 2005
      this.backgroundUpper_.classList.add(this.CssClasses_.BACKGROUND_UPPER);                        // 2006
      backgroundFlex.appendChild(this.backgroundUpper_);                                             // 2007
    }                                                                                                // 2008
                                                                                                     // 2009
    this.boundInputHandler = this.onInput_.bind(this);                                               // 2010
    this.boundChangeHandler = this.onChange_.bind(this);                                             // 2011
    this.boundMouseUpHandler = this.onMouseUp_.bind(this);                                           // 2012
    this.boundContainerMouseDownHandler = this.onContainerMouseDown_.bind(this);                     // 2013
    this.element_.addEventListener('input', this.boundInputHandler);                                 // 2014
    this.element_.addEventListener('change', this.boundChangeHandler);                               // 2015
    this.element_.addEventListener('mouseup', this.boundMouseUpHandler);                             // 2016
    this.element_.parentElement.addEventListener('mousedown', this.boundContainerMouseDownHandler);  // 2017
                                                                                                     // 2018
    this.updateValueStyles_();                                                                       // 2019
    this.element_.classList.add(this.CssClasses_.IS_UPGRADED);                                       // 2020
  }                                                                                                  // 2021
};                                                                                                   // 2022
                                                                                                     // 2023
/*                                                                                                   // 2024
* Downgrade the component                                                                            // 2025
*/                                                                                                   // 2026
MaterialSlider.prototype.mdlDowngrade_ = function() {                                                // 2027
  'use strict';                                                                                      // 2028
  this.element_.removeEventListener('input', this.boundInputHandler);                                // 2029
  this.element_.removeEventListener('change', this.boundChangeHandler);                              // 2030
  this.element_.removeEventListener('mouseup', this.boundMouseUpHandler);                            // 2031
  this.element_.parentElement.removeEventListener('mousedown', this.boundContainerMouseDownHandler);         // 2040
};                                                                                                   // 2033
                                                                                                     // 2034
// The component registers itself. It can assume componentHandler is available                       // 2035
// in the global scope.                                                                              // 2036
componentHandler.register({                                                                          // 2037
  constructor: MaterialSlider,                                                                       // 2038
  classAsString: 'MaterialSlider',                                                                   // 2039
  cssClass: 'mdl-js-slider'                                                                          // 2040
});                                                                                                  // 2041
                                                                                                     // 2042
/**                                                                                                  // 2043
 * @license                                                                                          // 2044
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 2045
 *                                                                                                   // 2046
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 2047
 * you may not use this file except in compliance with the License.                                  // 2048
 * You may obtain a copy of the License at                                                           // 2049
 *                                                                                                   // 2050
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 2051
 *                                                                                                   // 2052
 * Unless required by applicable law or agreed to in writing, software                               // 2053
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 2054
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 2055
 * See the License for the specific language governing permissions and                               // 2056
 * limitations under the License.                                                                    // 2057
 */                                                                                                  // 2058
                                                                                                     // 2059
/**                                                                                                  // 2060
 * Class constructor for Spinner MDL component.                                                      // 2061
 * Implements MDL component design pattern defined at:                                               // 2062
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 2063
 * @param {HTMLElement} element The element that will be upgraded.                                   // 2064
 * @constructor                                                                                      // 2065
 */                                                                                                  // 2066
function MaterialSpinner(element) {                                                                  // 2067
  'use strict';                                                                                      // 2068
                                                                                                     // 2069
  this.element_ = element;                                                                           // 2070
                                                                                                     // 2071
  // Initialize instance.                                                                            // 2072
  this.init();                                                                                       // 2073
}                                                                                                    // 2074
                                                                                                     // 2075
/**                                                                                                  // 2076
 * Store constants in one place so they can be updated easily.                                       // 2077
 * @enum {string | number}                                                                           // 2078
 * @private                                                                                          // 2079
 */                                                                                                  // 2080
MaterialSpinner.prototype.Constant_ = {                                                              // 2081
  MDL_SPINNER_LAYER_COUNT: 4                                                                         // 2082
};                                                                                                   // 2083
                                                                                                     // 2084
/**                                                                                                  // 2085
 * Store strings for class names defined by this component that are used in                          // 2086
 * JavaScript. This allows us to simply change it in one place should we                             // 2087
 * decide to modify at a later date.                                                                 // 2088
 * @enum {string}                                                                                    // 2089
 * @private                                                                                          // 2090
 */                                                                                                  // 2091
MaterialSpinner.prototype.CssClasses_ = {                                                            // 2092
  MDL_SPINNER_LAYER: 'mdl-spinner__layer',                                                           // 2093
  MDL_SPINNER_CIRCLE_CLIPPER: 'mdl-spinner__circle-clipper',                                         // 2094
  MDL_SPINNER_CIRCLE: 'mdl-spinner__circle',                                                         // 2095
  MDL_SPINNER_GAP_PATCH: 'mdl-spinner__gap-patch',                                                   // 2096
  MDL_SPINNER_LEFT: 'mdl-spinner__left',                                                             // 2097
  MDL_SPINNER_RIGHT: 'mdl-spinner__right'                                                            // 2098
};                                                                                                   // 2099
                                                                                                     // 2100
/**                                                                                                  // 2101
* Auxiliary method to create a spinner layer.                                                        // 2102
*/                                                                                                   // 2103
MaterialSpinner.prototype.createLayer = function(index) {                                            // 2104
  'use strict';                                                                                      // 2105
                                                                                                     // 2106
  var layer = document.createElement('div');                                                         // 2107
  layer.classList.add(this.CssClasses_.MDL_SPINNER_LAYER);                                           // 2108
  layer.classList.add(this.CssClasses_.MDL_SPINNER_LAYER + '-' + index);                             // 2109
                                                                                                     // 2110
  var leftClipper = document.createElement('div');                                                   // 2111
  leftClipper.classList.add(this.CssClasses_.MDL_SPINNER_CIRCLE_CLIPPER);                            // 2112
  leftClipper.classList.add(this.CssClasses_.MDL_SPINNER_LEFT);                                      // 2113
                                                                                                     // 2114
  var gapPatch = document.createElement('div');                                                      // 2115
  gapPatch.classList.add(this.CssClasses_.MDL_SPINNER_GAP_PATCH);                                    // 2116
                                                                                                     // 2117
  var rightClipper = document.createElement('div');                                                  // 2118
  rightClipper.classList.add(this.CssClasses_.MDL_SPINNER_CIRCLE_CLIPPER);                           // 2119
  rightClipper.classList.add(this.CssClasses_.MDL_SPINNER_RIGHT);                                    // 2120
                                                                                                     // 2121
  var circleOwners = [leftClipper, gapPatch, rightClipper];                                          // 2122
                                                                                                     // 2123
  for (var i = 0; i < circleOwners.length; i++) {                                                    // 2124
    var circle = document.createElement('div');                                                      // 2125
    circle.classList.add(this.CssClasses_.MDL_SPINNER_CIRCLE);                                       // 2126
    circleOwners[i].appendChild(circle);                                                             // 2127
  }                                                                                                  // 2128
                                                                                                     // 2129
  layer.appendChild(leftClipper);                                                                    // 2130
  layer.appendChild(gapPatch);                                                                       // 2131
  layer.appendChild(rightClipper);                                                                   // 2132
                                                                                                     // 2133
  this.element_.appendChild(layer);                                                                  // 2134
};                                                                                                   // 2135
                                                                                                     // 2136
/**                                                                                                  // 2137
* Stops the spinner animation.                                                                       // 2138
* Public method for users who need to stop the spinner for any reason.                               // 2139
* @public                                                                                            // 2140
*/                                                                                                   // 2141
MaterialSpinner.prototype.stop = function() {                                                        // 2142
  'use strict';                                                                                      // 2143
                                                                                                     // 2144
  this.element_.classList.remove('is-active');                                                       // 2145
};                                                                                                   // 2146
                                                                                                     // 2147
/**                                                                                                  // 2148
* Starts the spinner animation.                                                                      // 2149
* Public method for users who need to manually start the spinner for any reason                      // 2150
* (instead of just adding the 'is-active' class to their markup).                                    // 2151
* @public                                                                                            // 2152
*/                                                                                                   // 2153
MaterialSpinner.prototype.start = function() {                                                       // 2154
  'use strict';                                                                                      // 2155
                                                                                                     // 2156
  this.element_.classList.add('is-active');                                                          // 2157
};                                                                                                   // 2158
                                                                                                     // 2159
/**                                                                                                  // 2160
 * Initialize element.                                                                               // 2161
 */                                                                                                  // 2162
MaterialSpinner.prototype.init = function() {                                                        // 2163
  'use strict';                                                                                      // 2164
                                                                                                     // 2165
  if (this.element_) {                                                                               // 2166
    for (var i = 1; i <= this.Constant_.MDL_SPINNER_LAYER_COUNT; i++) {                              // 2167
      this.createLayer(i);                                                                           // 2168
    }                                                                                                // 2169
                                                                                                     // 2170
    this.element_.classList.add('is-upgraded');                                                      // 2171
  }                                                                                                  // 2172
};                                                                                                   // 2173
                                                                                                     // 2174
// The component registers itself. It can assume componentHandler is available                       // 2175
// in the global scope.                                                                              // 2176
componentHandler.register({                                                                          // 2177
  constructor: MaterialSpinner,                                                                      // 2178
  classAsString: 'MaterialSpinner',                                                                  // 2179
  cssClass: 'mdl-js-spinner'                                                                         // 2180
});                                                                                                  // 2181
                                                                                                     // 2182
/**                                                                                                  // 2183
 * @license                                                                                          // 2184
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 2185
 *                                                                                                   // 2186
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 2187
 * you may not use this file except in compliance with the License.                                  // 2188
 * You may obtain a copy of the License at                                                           // 2189
 *                                                                                                   // 2190
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 2191
 *                                                                                                   // 2192
 * Unless required by applicable law or agreed to in writing, software                               // 2193
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 2194
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 2195
 * See the License for the specific language governing permissions and                               // 2196
 * limitations under the License.                                                                    // 2197
 */                                                                                                  // 2198
                                                                                                     // 2199
/**                                                                                                  // 2200
 * Class constructor for Checkbox MDL component.                                                     // 2201
 * Implements MDL component design pattern defined at:                                               // 2202
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 2203
 * @param {HTMLElement} element The element that will be upgraded.                                   // 2204
 */                                                                                                  // 2205
function MaterialSwitch(element) {                                                                   // 2206
  'use strict';                                                                                      // 2207
                                                                                                     // 2208
  this.element_ = element;                                                                           // 2209
                                                                                                     // 2210
  // Initialize instance.                                                                            // 2211
  this.init();                                                                                       // 2212
}                                                                                                    // 2213
                                                                                                     // 2214
/**                                                                                                  // 2215
 * Store constants in one place so they can be updated easily.                                       // 2216
 * @enum {string | number}                                                                           // 2217
 * @private                                                                                          // 2218
 */                                                                                                  // 2219
MaterialSwitch.prototype.Constant_ = {                                                               // 2220
  TINY_TIMEOUT: 0.001                                                                                // 2221
};                                                                                                   // 2222
                                                                                                     // 2223
/**                                                                                                  // 2224
 * Store strings for class names defined by this component that are used in                          // 2225
 * JavaScript. This allows us to simply change it in one place should we                             // 2226
 * decide to modify at a later date.                                                                 // 2227
 * @enum {string}                                                                                    // 2228
 * @private                                                                                          // 2229
 */                                                                                                  // 2230
MaterialSwitch.prototype.CssClasses_ = {                                                             // 2231
  INPUT: 'mdl-switch__input',                                                                        // 2232
  TRACK: 'mdl-switch__track',                                                                        // 2233
  THUMB: 'mdl-switch__thumb',                                                                        // 2234
  FOCUS_HELPER: 'mdl-switch__focus-helper',                                                          // 2235
  RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                             // 2236
  RIPPLE_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events',                                       // 2237
  RIPPLE_CONTAINER: 'mdl-switch__ripple-container',                                                  // 2238
  RIPPLE_CENTER: 'mdl-ripple--center',                                                               // 2239
  RIPPLE: 'mdl-ripple',                                                                              // 2240
  IS_FOCUSED: 'is-focused',                                                                          // 2241
  IS_DISABLED: 'is-disabled',                                                                        // 2242
  IS_CHECKED: 'is-checked'                                                                           // 2243
};                                                                                                   // 2244
                                                                                                     // 2245
/**                                                                                                  // 2246
 * Handle change of state.                                                                           // 2247
 * @param {Event} event The event that fired.                                                        // 2248
 * @private                                                                                          // 2249
 */                                                                                                  // 2250
MaterialSwitch.prototype.onChange_ = function(event) {                                               // 2251
  'use strict';                                                                                      // 2252
                                                                                                     // 2253
  this.updateClasses_();                                                                             // 2254
};                                                                                                   // 2255
                                                                                                     // 2256
/**                                                                                                  // 2257
 * Handle focus of element.                                                                          // 2258
 * @param {Event} event The event that fired.                                                        // 2259
 * @private                                                                                          // 2260
 */                                                                                                  // 2261
MaterialSwitch.prototype.onFocus_ = function(event) {                                                // 2262
  'use strict';                                                                                      // 2263
                                                                                                     // 2264
  this.element_.classList.add(this.CssClasses_.IS_FOCUSED);                                          // 2265
};                                                                                                   // 2266
                                                                                                     // 2267
/**                                                                                                  // 2268
 * Handle lost focus of element.                                                                     // 2269
 * @param {Event} event The event that fired.                                                        // 2270
 * @private                                                                                          // 2271
 */                                                                                                  // 2272
MaterialSwitch.prototype.onBlur_ = function(event) {                                                 // 2273
  'use strict';                                                                                      // 2274
                                                                                                     // 2275
  this.element_.classList.remove(this.CssClasses_.IS_FOCUSED);                                       // 2276
};                                                                                                   // 2277
                                                                                                     // 2278
/**                                                                                                  // 2279
 * Handle mouseup.                                                                                   // 2280
 * @param {Event} event The event that fired.                                                        // 2281
 * @private                                                                                          // 2282
 */                                                                                                  // 2283
MaterialSwitch.prototype.onMouseUp_ = function(event) {                                              // 2284
  'use strict';                                                                                      // 2285
                                                                                                     // 2286
  this.blur_();                                                                                      // 2287
};                                                                                                   // 2288
                                                                                                     // 2289
/**                                                                                                  // 2290
 * Handle class updates.                                                                             // 2291
 * @param {HTMLElement} button The button whose classes we should update.                            // 2292
 * @param {HTMLElement} label The label whose classes we should update.                              // 2293
 * @private                                                                                          // 2294
 */                                                                                                  // 2295
MaterialSwitch.prototype.updateClasses_ = function() {                                               // 2296
  'use strict';                                                                                      // 2297
                                                                                                     // 2298
  if (this.inputElement_.disabled) {                                                                 // 2299
    this.element_.classList.add(this.CssClasses_.IS_DISABLED);                                       // 2300
  } else {                                                                                           // 2301
    this.element_.classList.remove(this.CssClasses_.IS_DISABLED);                                    // 2302
  }                                                                                                  // 2303
                                                                                                     // 2304
  if (this.inputElement_.checked) {                                                                  // 2305
    this.element_.classList.add(this.CssClasses_.IS_CHECKED);                                        // 2306
  } else {                                                                                           // 2307
    this.element_.classList.remove(this.CssClasses_.IS_CHECKED);                                     // 2308
  }                                                                                                  // 2309
};                                                                                                   // 2310
                                                                                                     // 2311
/**                                                                                                  // 2312
 * Add blur.                                                                                         // 2313
 * @private                                                                                          // 2314
 */                                                                                                  // 2315
MaterialSwitch.prototype.blur_ = function(event) {                                                   // 2316
  'use strict';                                                                                      // 2317
                                                                                                     // 2318
  // TODO: figure out why there's a focus event being fired after our blur,                          // 2319
  // so that we can avoid this hack.                                                                 // 2320
  window.setTimeout(function() {                                                                     // 2321
    this.inputElement_.blur();                                                                       // 2322
  }.bind(this), this.Constant_.TINY_TIMEOUT);                                                        // 2323
};                                                                                                   // 2324
                                                                                                     // 2325
// Public methods.                                                                                   // 2326
                                                                                                     // 2327
/**                                                                                                  // 2328
 * Disable switch.                                                                                   // 2329
 * @public                                                                                           // 2330
 */                                                                                                  // 2331
MaterialSwitch.prototype.disable = function() {                                                      // 2332
  'use strict';                                                                                      // 2333
                                                                                                     // 2334
  this.inputElement_.disabled = true;                                                                // 2335
  this.updateClasses_();                                                                             // 2336
};                                                                                                   // 2337
                                                                                                     // 2338
/**                                                                                                  // 2339
 * Enable switch.                                                                                    // 2340
 * @public                                                                                           // 2341
 */                                                                                                  // 2342
MaterialSwitch.prototype.enable = function() {                                                       // 2343
  'use strict';                                                                                      // 2344
                                                                                                     // 2345
  this.inputElement_.disabled = false;                                                               // 2346
  this.updateClasses_();                                                                             // 2347
};                                                                                                   // 2348
                                                                                                     // 2349
/**                                                                                                  // 2350
 * Activate switch.                                                                                  // 2351
 * @public                                                                                           // 2352
 */                                                                                                  // 2353
MaterialSwitch.prototype.on = function() {                                                           // 2354
  'use strict';                                                                                      // 2355
                                                                                                     // 2356
  this.inputElement_.checked = true;                                                                 // 2357
  this.updateClasses_();                                                                             // 2358
};                                                                                                   // 2359
                                                                                                     // 2360
/**                                                                                                  // 2361
 * Deactivate switch.                                                                                // 2362
 * @public                                                                                           // 2363
 */                                                                                                  // 2364
MaterialSwitch.prototype.off = function() {                                                          // 2365
  'use strict';                                                                                      // 2366
                                                                                                     // 2367
  this.inputElement_.checked = false;                                                                // 2368
  this.updateClasses_();                                                                             // 2369
};                                                                                                   // 2370
                                                                                                     // 2371
/**                                                                                                  // 2372
 * Initialize element.                                                                               // 2373
 */                                                                                                  // 2374
MaterialSwitch.prototype.init = function() {                                                         // 2375
  'use strict';                                                                                      // 2376
                                                                                                     // 2377
  if (this.element_) {                                                                               // 2378
    this.inputElement_ = this.element_.querySelector('.' +                                           // 2379
        this.CssClasses_.INPUT);                                                                     // 2380
                                                                                                     // 2381
    var track = document.createElement('div');                                                       // 2382
    track.classList.add(this.CssClasses_.TRACK);                                                     // 2383
                                                                                                     // 2384
    var thumb = document.createElement('div');                                                       // 2385
    thumb.classList.add(this.CssClasses_.THUMB);                                                     // 2386
                                                                                                     // 2387
    var focusHelper = document.createElement('span');                                                // 2388
    focusHelper.classList.add(this.CssClasses_.FOCUS_HELPER);                                        // 2389
                                                                                                     // 2390
    thumb.appendChild(focusHelper);                                                                  // 2391
                                                                                                     // 2392
    this.element_.appendChild(track);                                                                // 2393
    this.element_.appendChild(thumb);                                                                // 2394
                                                                                                     // 2395
    this.boundMouseUpHandler = this.onMouseUp_.bind(this);                                           // 2396
                                                                                                     // 2397
    if (this.element_.classList.contains(                                                            // 2398
        this.CssClasses_.RIPPLE_EFFECT)) {                                                           // 2399
      this.element_.classList.add(                                                                   // 2400
          this.CssClasses_.RIPPLE_IGNORE_EVENTS);                                                    // 2401
      this.rippleContainerElement_ = document.createElement('span');                                 // 2402
      this.rippleContainerElement_.classList.add(                                                    // 2403
          this.CssClasses_.RIPPLE_CONTAINER);                                                        // 2404
      this.rippleContainerElement_.classList.add(this.CssClasses_.RIPPLE_EFFECT);                    // 2405
      this.rippleContainerElement_.classList.add(this.CssClasses_.RIPPLE_CENTER);                    // 2406
      this.rippleContainerElement_.addEventListener('mouseup', this.boundMouseUpHandler);            // 2407
                                                                                                     // 2408
      var ripple = document.createElement('span');                                                   // 2409
      ripple.classList.add(this.CssClasses_.RIPPLE);                                                 // 2410
                                                                                                     // 2411
      this.rippleContainerElement_.appendChild(ripple);                                              // 2412
      this.element_.appendChild(this.rippleContainerElement_);                                       // 2413
    }                                                                                                // 2414
                                                                                                     // 2415
    this.boundChangeHandler = this.onChange_.bind(this);                                             // 2416
    this.boundFocusHandler = this.onFocus_.bind(this);                                               // 2417
    this.boundBlurHandler = this.onBlur_.bind(this);                                                 // 2418
                                                                                                     // 2419
    this.inputElement_.addEventListener('change', this.boundChangeHandler);                          // 2420
    this.inputElement_.addEventListener('focus', this.boundFocusHandler);                            // 2421
    this.inputElement_.addEventListener('blur', this.boundBlurHandler);                              // 2422
    this.element_.addEventListener('mouseup', this.boundMouseUpHandler);                             // 2423
                                                                                                     // 2424
    this.updateClasses_();                                                                           // 2425
    this.element_.classList.add('is-upgraded');                                                      // 2426
  }                                                                                                  // 2427
};                                                                                                   // 2428
                                                                                                     // 2429
/*                                                                                                   // 2430
* Downgrade the component.                                                                           // 2431
*/                                                                                                   // 2432
MaterialSwitch.prototype.mdlDowngrade_ = function() {                                                // 2433
  'use strict';                                                                                      // 2434
  if (this.rippleContainerElement_) {                                                                // 2435
    this.rippleContainerElement_.removeEventListener('mouseup', this.boundMouseUpHandler);           // 2436
  }                                                                                                  // 2437
  this.inputElement_.removeEventListener('change', this.boundChangeHandler);                         // 2438
  this.inputElement_.removeEventListener('focus', this.boundFocusHandler);                           // 2439
  this.inputElement_.removeEventListener('blur', this.boundBlurHandler);                             // 2440
  this.element_.removeEventListener('mouseup', this.boundMouseUpHandler);                            // 2441
};                                                                                                   // 2442
                                                                                                     // 2443
// The component registers itself. It can assume componentHandler is available                       // 2444
// in the global scope.                                                                              // 2445
componentHandler.register({                                                                          // 2446
  constructor: MaterialSwitch,                                                                       // 2447
  classAsString: 'MaterialSwitch',                                                                   // 2448
  cssClass: 'mdl-js-switch'                                                                          // 2449
});                                                                                                  // 2450
                                                                                                     // 2451
/**                                                                                                  // 2452
 * @license                                                                                          // 2453
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 2454
 *                                                                                                   // 2455
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 2456
 * you may not use this file except in compliance with the License.                                  // 2457
 * You may obtain a copy of the License at                                                           // 2458
 *                                                                                                   // 2459
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 2460
 *                                                                                                   // 2461
 * Unless required by applicable law or agreed to in writing, software                               // 2462
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 2463
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 2464
 * See the License for the specific language governing permissions and                               // 2465
 * limitations under the License.                                                                    // 2466
 */                                                                                                  // 2467
                                                                                                     // 2468
/**                                                                                                  // 2469
 * Class constructor for Tabs MDL component.                                                         // 2470
 * Implements MDL component design pattern defined at:                                               // 2471
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 2472
 * @param {HTMLElement} element The element that will be upgraded.                                   // 2473
 */                                                                                                  // 2474
function MaterialTabs(element) {                                                                     // 2475
  'use strict';                                                                                      // 2476
                                                                                                     // 2477
  // Stores the HTML element.                                                                        // 2478
  this.element_ = element;                                                                           // 2479
                                                                                                     // 2480
  // Initialize instance.                                                                            // 2481
  this.init();                                                                                       // 2482
}                                                                                                    // 2483
                                                                                                     // 2484
/**                                                                                                  // 2485
 * Store constants in one place so they can be updated easily.                                       // 2486
 * @enum {string}                                                                                    // 2487
 * @private                                                                                          // 2488
 */                                                                                                  // 2489
MaterialTabs.prototype.Constant_ = {                                                                 // 2490
  // None at the moment.                                                                             // 2491
};                                                                                                   // 2492
                                                                                                     // 2493
/**                                                                                                  // 2494
 * Store strings for class names defined by this component that are used in                          // 2495
 * JavaScript. This allows us to simply change it in one place should we                             // 2496
 * decide to modify at a later date.                                                                 // 2497
 * @enum {string}                                                                                    // 2498
 * @private                                                                                          // 2499
 */                                                                                                  // 2500
MaterialTabs.prototype.CssClasses_ = {                                                               // 2501
  TAB_CLASS: 'mdl-tabs__tab',                                                                        // 2502
  PANEL_CLASS: 'mdl-tabs__panel',                                                                    // 2503
  ACTIVE_CLASS: 'is-active',                                                                         // 2504
  UPGRADED_CLASS: 'is-upgraded',                                                                     // 2505
                                                                                                     // 2506
  MDL_JS_RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                      // 2507
  MDL_RIPPLE_CONTAINER: 'mdl-tabs__ripple-container',                                                // 2508
  MDL_RIPPLE: 'mdl-ripple',                                                                          // 2509
  MDL_JS_RIPPLE_EFFECT_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events'                          // 2510
};                                                                                                   // 2511
                                                                                                     // 2512
/**                                                                                                  // 2513
 * Handle clicks to a tabs component                                                                 // 2514
 * @private                                                                                          // 2515
 */                                                                                                  // 2516
MaterialTabs.prototype.initTabs_ = function(e) {                                                     // 2517
  'use strict';                                                                                      // 2518
                                                                                                     // 2519
  if (this.element_.classList.contains(this.CssClasses_.MDL_JS_RIPPLE_EFFECT)) {                     // 2520
    this.element_.classList.add(                                                                     // 2521
      this.CssClasses_.MDL_JS_RIPPLE_EFFECT_IGNORE_EVENTS);                                          // 2522
  }                                                                                                  // 2523
                                                                                                     // 2524
  // Select element tabs, document panels                                                            // 2525
  this.tabs_ = this.element_.querySelectorAll('.' + this.CssClasses_.TAB_CLASS);                     // 2526
  this.panels_ =                                                                                     // 2527
      this.element_.querySelectorAll('.' + this.CssClasses_.PANEL_CLASS);                            // 2528
                                                                                                     // 2529
  // Create new tabs for each tab element                                                            // 2530
  for (var i = 0; i < this.tabs_.length; i++) {                                                      // 2531
    new MaterialTab(this.tabs_[i], this);                                                            // 2532
  }                                                                                                  // 2533
                                                                                                     // 2534
  this.element_.classList.add(this.CssClasses_.UPGRADED_CLASS);                                      // 2535
};                                                                                                   // 2536
                                                                                                     // 2537
/**                                                                                                  // 2538
 * Reset tab state, dropping active classes                                                          // 2539
 * @private                                                                                          // 2540
 */                                                                                                  // 2541
MaterialTabs.prototype.resetTabState_ = function() {                                                 // 2542
  'use strict';                                                                                      // 2543
                                                                                                     // 2544
  for (var k = 0; k < this.tabs_.length; k++) {                                                      // 2545
    this.tabs_[k].classList.remove(this.CssClasses_.ACTIVE_CLASS);                                   // 2546
  }                                                                                                  // 2547
};                                                                                                   // 2548
                                                                                                     // 2549
/**                                                                                                  // 2550
 * Reset panel state, droping active classes                                                         // 2551
 * @private                                                                                          // 2552
 */                                                                                                  // 2553
MaterialTabs.prototype.resetPanelState_ = function() {                                               // 2554
  'use strict';                                                                                      // 2555
                                                                                                     // 2556
  for (var j = 0; j < this.panels_.length; j++) {                                                    // 2557
    this.panels_[j].classList.remove(this.CssClasses_.ACTIVE_CLASS);                                 // 2558
  }                                                                                                  // 2559
};                                                                                                   // 2560
                                                                                                     // 2561
MaterialTabs.prototype.init = function() {                                                           // 2562
  'use strict';                                                                                      // 2563
                                                                                                     // 2564
  if (this.element_) {                                                                               // 2565
    this.initTabs_();                                                                                // 2566
  }                                                                                                  // 2567
};                                                                                                   // 2568
                                                                                                     // 2569
function MaterialTab(tab, ctx) {                                                                     // 2570
  'use strict';                                                                                      // 2571
                                                                                                     // 2572
  if (tab) {                                                                                         // 2573
    if (ctx.element_.classList.contains(ctx.CssClasses_.MDL_JS_RIPPLE_EFFECT)) {                     // 2574
      var rippleContainer = document.createElement('span');                                          // 2575
      rippleContainer.classList.add(ctx.CssClasses_.MDL_RIPPLE_CONTAINER);                           // 2576
      rippleContainer.classList.add(ctx.CssClasses_.MDL_JS_RIPPLE_EFFECT);                           // 2577
      var ripple = document.createElement('span');                                                   // 2578
      ripple.classList.add(ctx.CssClasses_.MDL_RIPPLE);                                              // 2579
      rippleContainer.appendChild(ripple);                                                           // 2580
      tab.appendChild(rippleContainer);                                                              // 2581
    }                                                                                                // 2582
                                                                                                     // 2583
    tab.addEventListener('click', function(e) {                                                      // 2584
      e.preventDefault();                                                                            // 2585
      var href = tab.href.split('#')[1];                                                             // 2586
      var panel = ctx.element_.querySelector('#' + href);                                            // 2587
      ctx.resetTabState_();                                                                          // 2588
      ctx.resetPanelState_();                                                                        // 2589
      tab.classList.add(ctx.CssClasses_.ACTIVE_CLASS);                                               // 2590
      panel.classList.add(ctx.CssClasses_.ACTIVE_CLASS);                                             // 2591
    });                                                                                              // 2592
                                                                                                     // 2593
  }                                                                                                  // 2594
}                                                                                                    // 2595
                                                                                                     // 2596
// The component registers itself. It can assume componentHandler is available                       // 2597
// in the global scope.                                                                              // 2598
componentHandler.register({                                                                          // 2599
  constructor: MaterialTabs,                                                                         // 2600
  classAsString: 'MaterialTabs',                                                                     // 2601
  cssClass: 'mdl-js-tabs'                                                                            // 2602
});                                                                                                  // 2603
                                                                                                     // 2604
/**                                                                                                  // 2605
 * @license                                                                                          // 2606
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 2607
 *                                                                                                   // 2608
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 2609
 * you may not use this file except in compliance with the License.                                  // 2610
 * You may obtain a copy of the License at                                                           // 2611
 *                                                                                                   // 2612
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 2613
 *                                                                                                   // 2614
 * Unless required by applicable law or agreed to in writing, software                               // 2615
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 2616
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 2617
 * See the License for the specific language governing permissions and                               // 2618
 * limitations under the License.                                                                    // 2619
 */                                                                                                  // 2620
                                                                                                     // 2621
/**                                                                                                  // 2622
 * Class constructor for Textfield MDL component.                                                    // 2623
 * Implements MDL component design pattern defined at:                                               // 2624
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 2625
 * @param {HTMLElement} element The element that will be upgraded.                                   // 2626
 */                                                                                                  // 2627
function MaterialTextfield(element) {                                                                // 2628
  'use strict';                                                                                      // 2629
                                                                                                     // 2630
  this.element_ = element;                                                                           // 2631
  this.maxRows = this.Constant_.NO_MAX_ROWS;                                                         // 2632
  // Initialize instance.                                                                            // 2633
  this.init();                                                                                       // 2634
}                                                                                                    // 2635
                                                                                                     // 2636
/**                                                                                                  // 2637
 * Store constants in one place so they can be updated easily.                                       // 2638
 * @enum {string | number}                                                                           // 2639
 * @private                                                                                          // 2640
 */                                                                                                  // 2641
MaterialTextfield.prototype.Constant_ = {                                                            // 2642
  NO_MAX_ROWS: -1,                                                                                   // 2643
  MAX_ROWS_ATTRIBUTE: 'maxrows'                                                                      // 2644
};                                                                                                   // 2645
                                                                                                     // 2646
/**                                                                                                  // 2647
 * Store strings for class names defined by this component that are used in                          // 2648
 * JavaScript. This allows us to simply change it in one place should we                             // 2649
 * decide to modify at a later date.                                                                 // 2650
 * @enum {string}                                                                                    // 2651
 * @private                                                                                          // 2652
 */                                                                                                  // 2653
MaterialTextfield.prototype.CssClasses_ = {                                                          // 2654
  LABEL: 'mdl-textfield__label',                                                                     // 2655
  INPUT: 'mdl-textfield__input',                                                                     // 2656
  IS_DIRTY: 'is-dirty',                                                                              // 2657
  IS_FOCUSED: 'is-focused',                                                                          // 2658
  IS_DISABLED: 'is-disabled',                                                                        // 2659
  IS_INVALID: 'is-invalid',                                                                          // 2660
  IS_UPGRADED: 'is-upgraded'                                                                         // 2661
};                                                                                                   // 2662
                                                                                                     // 2663
/**                                                                                                  // 2664
 * Handle input being entered.                                                                       // 2665
 * @param {Event} event The event that fired.                                                        // 2666
 * @private                                                                                          // 2667
 */                                                                                                  // 2668
MaterialTextfield.prototype.onKeyDown_ = function(event) {                                           // 2669
  'use strict';                                                                                      // 2670
                                                                                                     // 2671
  var currentRowCount = event.target.value.split('\n').length;                                       // 2672
  if (event.keyCode === 13) {                                                                        // 2673
    if (currentRowCount >= this.maxRows) {                                                           // 2674
      event.preventDefault();                                                                        // 2675
    }                                                                                                // 2676
  }                                                                                                  // 2677
};                                                                                                   // 2678
                                                                                                     // 2679
/**                                                                                                  // 2680
 * Handle focus.                                                                                     // 2681
 * @param {Event} event The event that fired.                                                        // 2682
 * @private                                                                                          // 2683
 */                                                                                                  // 2684
MaterialTextfield.prototype.onFocus_ = function(event) {                                             // 2685
  'use strict';                                                                                      // 2686
                                                                                                     // 2687
  this.element_.classList.add(this.CssClasses_.IS_FOCUSED);                                          // 2688
};                                                                                                   // 2689
                                                                                                     // 2690
/**                                                                                                  // 2691
 * Handle lost focus.                                                                                // 2692
 * @param {Event} event The event that fired.                                                        // 2693
 * @private                                                                                          // 2694
 */                                                                                                  // 2695
MaterialTextfield.prototype.onBlur_ = function(event) {                                              // 2696
  'use strict';                                                                                      // 2697
                                                                                                     // 2698
  this.element_.classList.remove(this.CssClasses_.IS_FOCUSED);                                       // 2699
};                                                                                                   // 2700
                                                                                                     // 2701
/**                                                                                                  // 2702
 * Handle class updates.                                                                             // 2703
 * @param {HTMLElement} button The button whose classes we should update.                            // 2704
 * @param {HTMLElement} label The label whose classes we should update.                              // 2705
 * @private                                                                                          // 2706
 */                                                                                                  // 2707
MaterialTextfield.prototype.updateClasses_ = function() {                                            // 2708
  'use strict';                                                                                      // 2709
                                                                                                     // 2710
  if (this.input_.disabled) {                                                                        // 2711
    this.element_.classList.add(this.CssClasses_.IS_DISABLED);                                       // 2712
  } else {                                                                                           // 2713
    this.element_.classList.remove(this.CssClasses_.IS_DISABLED);                                    // 2714
  }                                                                                                  // 2715
                                                                                                     // 2716
  if (this.input_.validity.valid) {                                                                  // 2717
    this.element_.classList.remove(this.CssClasses_.IS_INVALID);                                     // 2718
  } else {                                                                                           // 2719
    this.element_.classList.add(this.CssClasses_.IS_INVALID);                                        // 2720
  }                                                                                                  // 2721
                                                                                                     // 2722
  if (this.input_.value && this.input_.value.length > 0) {                                           // 2723
    this.element_.classList.add(this.CssClasses_.IS_DIRTY);                                          // 2724
  } else {                                                                                           // 2725
    this.element_.classList.remove(this.CssClasses_.IS_DIRTY);                                       // 2726
  }                                                                                                  // 2727
};                                                                                                   // 2728
                                                                                                     // 2729
// Public methods.                                                                                   // 2730
                                                                                                     // 2731
/**                                                                                                  // 2732
 * Disable text field.                                                                               // 2733
 * @public                                                                                           // 2734
 */                                                                                                  // 2735
MaterialTextfield.prototype.disable = function() {                                                   // 2736
  'use strict';                                                                                      // 2737
                                                                                                     // 2738
  this.input_.disabled = true;                                                                       // 2739
  this.updateClasses_();                                                                             // 2740
};                                                                                                   // 2741
                                                                                                     // 2742
/**                                                                                                  // 2743
 * Enable text field.                                                                                // 2744
 * @public                                                                                           // 2745
 */                                                                                                  // 2746
MaterialTextfield.prototype.enable = function() {                                                    // 2747
  'use strict';                                                                                      // 2748
                                                                                                     // 2749
  this.input_.disabled = false;                                                                      // 2750
  this.updateClasses_();                                                                             // 2751
};                                                                                                   // 2752
                                                                                                     // 2753
/**                                                                                                  // 2754
 * Update text field value.                                                                          // 2755
 * @param {String} value The value to which to set the control (optional).                           // 2756
 * @public                                                                                           // 2757
 */                                                                                                  // 2758
MaterialTextfield.prototype.change = function(value) {                                               // 2759
  'use strict';                                                                                      // 2760
                                                                                                     // 2761
  if (value) {                                                                                       // 2762
    this.input_.value = value;                                                                       // 2763
  }                                                                                                  // 2764
  this.updateClasses_();                                                                             // 2765
};                                                                                                   // 2766
                                                                                                     // 2767
/**                                                                                                  // 2768
 * Initialize element.                                                                               // 2769
 */                                                                                                  // 2770
MaterialTextfield.prototype.init = function() {                                                      // 2771
  'use strict';                                                                                      // 2772
                                                                                                     // 2773
  if (this.element_) {                                                                               // 2774
    this.label_ = this.element_.querySelector('.' + this.CssClasses_.LABEL);                         // 2775
    this.input_ = this.element_.querySelector('.' + this.CssClasses_.INPUT);                         // 2776
                                                                                                     // 2777
    if (this.input_) {                                                                               // 2778
      if (this.input_.hasAttribute(this.Constant_.MAX_ROWS_ATTRIBUTE)) {                             // 2779
        this.maxRows = parseInt(this.input_.getAttribute(                                            // 2780
            this.Constant_.MAX_ROWS_ATTRIBUTE), 10);                                                 // 2781
        if (isNaN(this.maxRows)) {                                                                   // 2782
          this.maxRows = this.Constant_.NO_MAX_ROWS;                                                 // 2783
        }                                                                                            // 2784
      }                                                                                              // 2785
                                                                                                     // 2786
      this.boundUpdateClassesHandler = this.updateClasses_.bind(this);                               // 2787
      this.boundFocusHandler = this.onFocus_.bind(this);                                             // 2788
      this.boundBlurHandler = this.onBlur_.bind(this);                                               // 2789
      this.input_.addEventListener('input', this.boundUpdateClassesHandler);                         // 2790
      this.input_.addEventListener('focus', this.boundFocusHandler);                                 // 2791
      this.input_.addEventListener('blur', this.boundBlurHandler);                                   // 2792
                                                                                                     // 2793
      if (this.maxRows !== this.Constant_.NO_MAX_ROWS) {                                             // 2794
        // TODO: This should handle pasting multi line text.                                         // 2795
        // Currently doesn't.                                                                        // 2796
        this.boundKeyDownHandler = this.onKeyDown_.bind(this);                                       // 2797
        this.input_.addEventListener('keydown', this.boundKeyDownHandler);                           // 2798
      }                                                                                              // 2799
                                                                                                     // 2800
      this.updateClasses_();                                                                         // 2801
      this.element_.classList.add(this.CssClasses_.IS_UPGRADED);                                     // 2802
    }                                                                                                // 2803
  }                                                                                                  // 2804
};                                                                                                   // 2805
                                                                                                     // 2806
/*                                                                                                   // 2807
* Downgrade the component                                                                            // 2808
*/                                                                                                   // 2809
MaterialTextfield.prototype.mdlDowngrade_ = function() {                                             // 2810
  'use strict';                                                                                      // 2811
  this.input_.removeEventListener('input', this.boundUpdateClassesHandler);                          // 2812
  this.input_.removeEventListener('focus', this.boundFocusHandler);                                  // 2813
  this.input_.removeEventListener('blur', this.boundBlurHandler);                                    // 2814
  if (this.boundKeyDownHandler) {                                                                    // 2815
    this.input_.removeEventListener('keydown', this.boundKeyDownHandler);                            // 2816
  }                                                                                                  // 2817
};                                                                                                   // 2818
                                                                                                     // 2819
// The component registers itself. It can assume componentHandler is available                       // 2820
// in the global scope.                                                                              // 2821
componentHandler.register({                                                                          // 2822
  constructor: MaterialTextfield,                                                                    // 2823
  classAsString: 'MaterialTextfield',                                                                // 2824
  cssClass: 'mdl-js-textfield'                                                                       // 2825
});                                                                                                  // 2826
                                                                                                     // 2827
/**                                                                                                  // 2828
 * @license                                                                                          // 2829
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 2830
 *                                                                                                   // 2831
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 2832
 * you may not use this file except in compliance with the License.                                  // 2833
 * You may obtain a copy of the License at                                                           // 2834
 *                                                                                                   // 2835
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 2836
 *                                                                                                   // 2837
 * Unless required by applicable law or agreed to in writing, software                               // 2838
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 2839
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 2840
 * See the License for the specific language governing permissions and                               // 2841
 * limitations under the License.                                                                    // 2842
 */                                                                                                  // 2843
                                                                                                     // 2844
/**                                                                                                  // 2845
 * Class constructor for Tooltip MDL component.                                                      // 2846
 * Implements MDL component design pattern defined at:                                               // 2847
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 2848
 * @param {HTMLElement} element The element that will be upgraded.                                   // 2849
 */                                                                                                  // 2850
function MaterialTooltip(element) {                                                                  // 2851
  'use strict';                                                                                      // 2852
                                                                                                     // 2853
  this.element_ = element;                                                                           // 2854
                                                                                                     // 2855
  // Initialize instance.                                                                            // 2856
  this.init();                                                                                       // 2857
}                                                                                                    // 2858
                                                                                                     // 2859
/**                                                                                                  // 2860
 * Store constants in one place so they can be updated easily.                                       // 2861
 * @enum {string | number}                                                                           // 2862
 * @private                                                                                          // 2863
 */                                                                                                  // 2864
MaterialTooltip.prototype.Constant_ = {                                                              // 2865
  // None for now.                                                                                   // 2866
};                                                                                                   // 2867
                                                                                                     // 2868
/**                                                                                                  // 2869
 * Store strings for class names defined by this component that are used in                          // 2870
 * JavaScript. This allows us to simply change it in one place should we                             // 2871
 * decide to modify at a later date.                                                                 // 2872
 * @enum {string}                                                                                    // 2873
 * @private                                                                                          // 2874
 */                                                                                                  // 2875
MaterialTooltip.prototype.CssClasses_ = {                                                            // 2876
  IS_ACTIVE: 'is-active'                                                                             // 2877
};                                                                                                   // 2878
                                                                                                     // 2879
/**                                                                                                  // 2880
 * Handle mouseenter for tooltip.                                                                    // 2881
 * @param {Event} event The event that fired.                                                        // 2882
 * @private                                                                                          // 2883
 */                                                                                                  // 2884
MaterialTooltip.prototype.handleMouseEnter_ = function(event) {                                      // 2885
  'use strict';                                                                                      // 2886
                                                                                                     // 2887
  event.stopPropagation();                                                                           // 2888
  var props = event.target.getBoundingClientRect();                                                  // 2889
  this.element_.style.left = props.left + (props.width / 2) + 'px';                                  // 2890
  this.element_.style.marginLeft = -1 * (this.element_.offsetWidth / 2) + 'px';                      // 2891
  this.element_.style.top = props.top + props.height + 10 + 'px';                                    // 2892
  this.element_.classList.add(this.CssClasses_.IS_ACTIVE);                                           // 2893
};                                                                                                   // 2894
                                                                                                     // 2895
/**                                                                                                  // 2896
 * Handle mouseleave for tooltip.                                                                    // 2897
 * @param {Event} event The event that fired.                                                        // 2898
 * @private                                                                                          // 2899
 */                                                                                                  // 2900
MaterialTooltip.prototype.handleMouseLeave_ = function(event) {                                      // 2901
  'use strict';                                                                                      // 2902
                                                                                                     // 2903
  event.stopPropagation();                                                                           // 2904
  this.element_.classList.remove(this.CssClasses_.IS_ACTIVE);                                        // 2905
};                                                                                                   // 2906
                                                                                                     // 2907
/**                                                                                                  // 2908
 * Initialize element.                                                                               // 2909
 */                                                                                                  // 2910
MaterialTooltip.prototype.init = function() {                                                        // 2911
  'use strict';                                                                                      // 2912
                                                                                                     // 2913
  if (this.element_) {                                                                               // 2914
    var forElId = this.element_.getAttribute('for');                                                 // 2915
                                                                                                     // 2916
    if (forElId) {                                                                                   // 2917
      this.forElement_ = document.getElementById(forElId);                                           // 2918
    }                                                                                                // 2919
                                                                                                     // 2920
    if (this.forElement_) {                                                                          // 2921
      this.boundMouseEnterHandler = this.handleMouseEnter_.bind(this);                               // 2922
      this.boundMouseLeaveHandler = this.handleMouseLeave_.bind(this);                               // 2923
      this.forElement_.addEventListener('mouseenter', this.boundMouseEnterHandler,                   // 2924
          false);                                                                                    // 2925
      this.forElement_.addEventListener('click', this.boundMouseEnterHandler,                        // 2926
          false);                                                                                    // 2927
      this.forElement_.addEventListener('mouseleave', this.boundMouseLeaveHandler);                  // 2928
    }                                                                                                // 2929
  }                                                                                                  // 2930
};                                                                                                   // 2931
                                                                                                     // 2932
/*                                                                                                   // 2933
* Downgrade the component                                                                            // 2934
*/                                                                                                   // 2935
MaterialTooltip.prototype.mdlDowngrade_ = function() {                                               // 2936
  'use strict';                                                                                      // 2937
  if (this.forElement_) {                                                                            // 2938
    this.forElement_.removeEventListener('mouseenter', this.boundMouseEnterHandler, false);          // 2939
    this.forElement_.removeEventListener('click', this.boundMouseEnterHandler, false);               // 2940
    this.forElement_.removeEventListener('mouseleave', this.boundMouseLeaveHandler);                 // 2941
  }                                                                                                  // 2942
};                                                                                                   // 2943
                                                                                                     // 2944
// The component registers itself. It can assume componentHandler is available                       // 2945
// in the global scope.                                                                              // 2946
componentHandler.register({                                                                          // 2947
  constructor: MaterialTooltip,                                                                      // 2948
  classAsString: 'MaterialTooltip',                                                                  // 2949
  cssClass: 'mdl-tooltip'                                                                            // 2950
});                                                                                                  // 2951
                                                                                                     // 2952
/**                                                                                                  // 2953
 * @license                                                                                          // 2954
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 2955
 *                                                                                                   // 2956
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 2957
 * you may not use this file except in compliance with the License.                                  // 2958
 * You may obtain a copy of the License at                                                           // 2959
 *                                                                                                   // 2960
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 2961
 *                                                                                                   // 2962
 * Unless required by applicable law or agreed to in writing, software                               // 2963
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 2964
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 2965
 * See the License for the specific language governing permissions and                               // 2966
 * limitations under the License.                                                                    // 2967
 */                                                                                                  // 2968
                                                                                                     // 2969
/**                                                                                                  // 2970
 * Class constructor for Layout MDL component.                                                       // 2971
 * Implements MDL component design pattern defined at:                                               // 2972
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 2973
 * @param {HTMLElement} element The element that will be upgraded.                                   // 2974
 */                                                                                                  // 2975
function MaterialLayout(element) {                                                                   // 2976
  'use strict';                                                                                      // 2977
                                                                                                     // 2978
  this.element_ = element;                                                                           // 2979
                                                                                                     // 2980
  // Initialize instance.                                                                            // 2981
  this.init();                                                                                       // 2982
}                                                                                                    // 2983
                                                                                                     // 2984
/**                                                                                                  // 2985
 * Store constants in one place so they can be updated easily.                                       // 2986
 * @enum {string | number}                                                                           // 2987
 * @private                                                                                          // 2988
 */                                                                                                  // 2989
MaterialLayout.prototype.Constant_ = {                                                               // 2990
  MAX_WIDTH: '(max-width: 850px)',                                                                   // 2991
  TAB_SCROLL_PIXELS: 100,                                                                            // 2992
                                                                                                     // 2993
  MENU_ICON: 'menu',                                                                                 // 2994
  CHEVRON_LEFT: 'chevron_left',                                                                      // 2995
  CHEVRON_RIGHT: 'chevron_right'                                                                     // 2996
};                                                                                                   // 2997
                                                                                                     // 2998
/**                                                                                                  // 2999
 * Modes.                                                                                            // 3000
 * @enum {number}                                                                                    // 3001
 * @private                                                                                          // 3002
 */                                                                                                  // 3003
MaterialLayout.prototype.Mode_ = {                                                                   // 3004
  STANDARD: 0,                                                                                       // 3005
  SEAMED: 1,                                                                                         // 3006
  WATERFALL: 2,                                                                                      // 3007
  SCROLL: 3                                                                                          // 3008
};                                                                                                   // 3009
                                                                                                     // 3010
/**                                                                                                  // 3011
 * Store strings for class names defined by this component that are used in                          // 3012
 * JavaScript. This allows us to simply change it in one place should we                             // 3013
 * decide to modify at a later date.                                                                 // 3014
 * @enum {string}                                                                                    // 3015
 * @private                                                                                          // 3016
 */                                                                                                  // 3017
MaterialLayout.prototype.CssClasses_ = {                                                             // 3018
  CONTAINER: 'mdl-layout__container',                                                                // 3019
  HEADER: 'mdl-layout__header',                                                                      // 3020
  DRAWER: 'mdl-layout__drawer',                                                                      // 3021
  CONTENT: 'mdl-layout__content',                                                                    // 3022
  DRAWER_BTN: 'mdl-layout__drawer-button',                                                           // 3023
                                                                                                     // 3024
  ICON: 'material-icons',                                                                            // 3025
                                                                                                     // 3026
  JS_RIPPLE_EFFECT: 'mdl-js-ripple-effect',                                                          // 3027
  RIPPLE_CONTAINER: 'mdl-layout__tab-ripple-container',                                              // 3028
  RIPPLE: 'mdl-ripple',                                                                              // 3029
  RIPPLE_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events',                                       // 3030
                                                                                                     // 3031
  HEADER_SEAMED: 'mdl-layout__header--seamed',                                                       // 3032
  HEADER_WATERFALL: 'mdl-layout__header--waterfall',                                                 // 3033
  HEADER_SCROLL: 'mdl-layout__header--scroll',                                                       // 3034
                                                                                                     // 3035
  FIXED_HEADER: 'mdl-layout--fixed-header',                                                          // 3036
  OBFUSCATOR: 'mdl-layout__obfuscator',                                                              // 3037
                                                                                                     // 3038
  TAB_BAR: 'mdl-layout__tab-bar',                                                                    // 3039
  TAB_CONTAINER: 'mdl-layout__tab-bar-container',                                                    // 3040
  TAB: 'mdl-layout__tab',                                                                            // 3041
  TAB_BAR_BUTTON: 'mdl-layout__tab-bar-button',                                                      // 3042
  TAB_BAR_LEFT_BUTTON: 'mdl-layout__tab-bar-left-button',                                            // 3043
  TAB_BAR_RIGHT_BUTTON: 'mdl-layout__tab-bar-right-button',                                          // 3044
  PANEL: 'mdl-layout__tab-panel',                                                                    // 3045
                                                                                                     // 3046
  HAS_DRAWER: 'has-drawer',                                                                          // 3047
  HAS_TABS: 'has-tabs',                                                                              // 3048
  HAS_SCROLLING_HEADER: 'has-scrolling-header',                                                      // 3049
  CASTING_SHADOW: 'is-casting-shadow',                                                               // 3050
  IS_COMPACT: 'is-compact',                                                                          // 3051
  IS_SMALL_SCREEN: 'is-small-screen',                                                                // 3052
  IS_DRAWER_OPEN: 'is-visible',                                                                      // 3053
  IS_ACTIVE: 'is-active',                                                                            // 3054
  IS_UPGRADED: 'is-upgraded',                                                                        // 3055
  IS_ANIMATING: 'is-animating'                                                                       // 3056
};                                                                                                   // 3057
                                                                                                     // 3058
/**                                                                                                  // 3059
 * Handles scrolling on the content.                                                                 // 3060
 * @private                                                                                          // 3061
 */                                                                                                  // 3062
MaterialLayout.prototype.contentScrollHandler_ = function() {                                        // 3063
  'use strict';                                                                                      // 3064
                                                                                                     // 3065
  if (this.header_.classList.contains(this.CssClasses_.IS_ANIMATING)) {                              // 3066
    return;                                                                                          // 3067
  }                                                                                                  // 3068
                                                                                                     // 3069
  if (this.content_.scrollTop > 0 &&                                                                 // 3070
      !this.header_.classList.contains(this.CssClasses_.IS_COMPACT)) {                               // 3071
    this.header_.classList.add(this.CssClasses_.CASTING_SHADOW);                                     // 3072
    this.header_.classList.add(this.CssClasses_.IS_COMPACT);                                         // 3073
    this.header_.classList.add(this.CssClasses_.IS_ANIMATING);                                       // 3074
  } else if (this.content_.scrollTop <= 0 &&                                                         // 3075
      this.header_.classList.contains(this.CssClasses_.IS_COMPACT)) {                                // 3076
    this.header_.classList.remove(this.CssClasses_.CASTING_SHADOW);                                  // 3077
    this.header_.classList.remove(this.CssClasses_.IS_COMPACT);                                      // 3078
    this.header_.classList.add(this.CssClasses_.IS_ANIMATING);                                       // 3079
  }                                                                                                  // 3080
};                                                                                                   // 3081
                                                                                                     // 3082
/**                                                                                                  // 3083
 * Handles changes in screen size.                                                                   // 3084
 * @private                                                                                          // 3085
 */                                                                                                  // 3086
MaterialLayout.prototype.screenSizeHandler_ = function() {                                           // 3087
  'use strict';                                                                                      // 3088
                                                                                                     // 3089
  if (this.screenSizeMediaQuery_.matches) {                                                          // 3090
    this.element_.classList.add(this.CssClasses_.IS_SMALL_SCREEN);                                   // 3091
  } else {                                                                                           // 3092
    this.element_.classList.remove(this.CssClasses_.IS_SMALL_SCREEN);                                // 3093
    // Collapse drawer (if any) when moving to a large screen size.                                  // 3094
    if (this.drawer_) {                                                                              // 3095
      this.drawer_.classList.remove(this.CssClasses_.IS_DRAWER_OPEN);                                // 3096
    }                                                                                                // 3097
  }                                                                                                  // 3098
};                                                                                                   // 3099
                                                                                                     // 3100
/**                                                                                                  // 3101
 * Handles toggling of the drawer.                                                                   // 3102
 * @param {Element} drawer The drawer container element.                                             // 3103
 * @private                                                                                          // 3104
 */                                                                                                  // 3105
MaterialLayout.prototype.drawerToggleHandler_ = function() {                                         // 3106
  'use strict';                                                                                      // 3107
                                                                                                     // 3108
  this.drawer_.classList.toggle(this.CssClasses_.IS_DRAWER_OPEN);                                    // 3109
};                                                                                                   // 3110
                                                                                                     // 3111
/**                                                                                                  // 3112
 * Handles (un)setting the `is-animating` class                                                      // 3113
 */                                                                                                  // 3114
MaterialLayout.prototype.headerTransitionEndHandler = function() {                                   // 3115
  'use strict';                                                                                      // 3116
                                                                                                     // 3117
  this.header_.classList.remove(this.CssClasses_.IS_ANIMATING);                                      // 3118
};                                                                                                   // 3119
                                                                                                     // 3120
/**                                                                                                  // 3121
 * Handles expanding the header on click                                                             // 3122
 */                                                                                                  // 3123
MaterialLayout.prototype.headerClickHandler = function() {                                           // 3124
  'use strict';                                                                                      // 3125
                                                                                                     // 3126
  if (this.header_.classList.contains(this.CssClasses_.IS_COMPACT)) {                                // 3127
    this.header_.classList.remove(this.CssClasses_.IS_COMPACT);                                      // 3128
    this.header_.classList.add(this.CssClasses_.IS_ANIMATING);                                       // 3129
  }                                                                                                  // 3130
};                                                                                                   // 3131
                                                                                                     // 3132
/**                                                                                                  // 3133
 * Reset tab state, dropping active classes                                                          // 3134
 * @private                                                                                          // 3135
 */                                                                                                  // 3136
MaterialLayout.prototype.resetTabState_ = function(tabBar) {                                         // 3137
  'use strict';                                                                                      // 3138
                                                                                                     // 3139
  for (var k = 0; k < tabBar.length; k++) {                                                          // 3140
    tabBar[k].classList.remove(this.CssClasses_.IS_ACTIVE);                                          // 3141
  }                                                                                                  // 3142
};                                                                                                   // 3143
                                                                                                     // 3144
/**                                                                                                  // 3145
 * Reset panel state, droping active classes                                                         // 3146
 * @private                                                                                          // 3147
 */                                                                                                  // 3148
MaterialLayout.prototype.resetPanelState_ = function(panels) {                                       // 3149
  'use strict';                                                                                      // 3150
                                                                                                     // 3151
  for (var j = 0; j < panels.length; j++) {                                                          // 3152
    panels[j].classList.remove(this.CssClasses_.IS_ACTIVE);                                          // 3153
  }                                                                                                  // 3154
};                                                                                                   // 3155
                                                                                                     // 3156
/**                                                                                                  // 3157
 * Initialize element.                                                                               // 3158
 */                                                                                                  // 3159
MaterialLayout.prototype.init = function() {                                                         // 3160
  'use strict';                                                                                      // 3161
                                                                                                     // 3162
  if (this.element_) {                                                                               // 3163
    var container = document.createElement('div');                                                   // 3164
    container.classList.add(this.CssClasses_.CONTAINER);                                             // 3165
    this.element_.parentElement.insertBefore(container, this.element_);                              // 3166
    this.element_.parentElement.removeChild(this.element_);                                          // 3167
    container.appendChild(this.element_);                                                            // 3168
                                                                                                     // 3169
    var directChildren = this.element_.childNodes;                                                   // 3170
    for (var c = 0; c < directChildren.length; c++) {                                                // 3171
      var child = directChildren[c];                                                                 // 3172
      if (child.classList &&                                                                         // 3173
          child.classList.contains(this.CssClasses_.HEADER)) {                                       // 3174
        this.header_ = child;                                                                        // 3175
      }                                                                                              // 3176
                                                                                                     // 3177
      if (child.classList &&                                                                         // 3178
          child.classList.contains(this.CssClasses_.DRAWER)) {                                       // 3179
        this.drawer_ = child;                                                                        // 3180
      }                                                                                              // 3181
                                                                                                     // 3182
      if (child.classList &&                                                                         // 3183
          child.classList.contains(this.CssClasses_.CONTENT)) {                                      // 3184
        this.content_ = child;                                                                       // 3185
      }                                                                                              // 3186
    }                                                                                                // 3187
                                                                                                     // 3188
    if (this.header_) {                                                                              // 3189
      this.tabBar_ = this.header_.querySelector('.' + this.CssClasses_.TAB_BAR);                     // 3190
    }                                                                                                // 3191
                                                                                                     // 3192
    var mode = this.Mode_.STANDARD;                                                                  // 3193
                                                                                                     // 3194
    // Keep an eye on screen size, and add/remove auxiliary class for styling                        // 3195
    // of small screens.                                                                             // 3196
    this.screenSizeMediaQuery_ = window.matchMedia(this.Constant_.MAX_WIDTH);                        // 3197
    this.screenSizeMediaQuery_.addListener(this.screenSizeHandler_.bind(this));                      // 3198
    this.screenSizeHandler_();                                                                       // 3199
                                                                                                     // 3200
    if (this.header_) {                                                                              // 3201
      if (this.header_.classList.contains(this.CssClasses_.HEADER_SEAMED)) {                         // 3202
        mode = this.Mode_.SEAMED;                                                                    // 3203
      } else if (this.header_.classList.contains(                                                    // 3204
          this.CssClasses_.HEADER_WATERFALL)) {                                                      // 3205
        mode = this.Mode_.WATERFALL;                                                                 // 3206
        this.header_.addEventListener('transitionend',                                               // 3207
          this.headerTransitionEndHandler.bind(this));                                               // 3208
        this.header_.addEventListener('click',                                                       // 3209
          this.headerClickHandler.bind(this));                                                       // 3210
      } else if (this.header_.classList.contains(                                                    // 3211
          this.CssClasses_.HEADER_SCROLL)) {                                                         // 3212
        mode = this.Mode_.SCROLL;                                                                    // 3213
        container.classList.add(this.CssClasses_.HAS_SCROLLING_HEADER);                              // 3214
      }                                                                                              // 3215
                                                                                                     // 3216
      if (mode === this.Mode_.STANDARD) {                                                            // 3217
        this.header_.classList.add(this.CssClasses_.CASTING_SHADOW);                                 // 3218
        if (this.tabBar_) {                                                                          // 3219
          this.tabBar_.classList.add(this.CssClasses_.CASTING_SHADOW);                               // 3220
        }                                                                                            // 3221
      } else if (mode === this.Mode_.SEAMED || mode === this.Mode_.SCROLL) {                         // 3222
        this.header_.classList.remove(this.CssClasses_.CASTING_SHADOW);                              // 3223
        if (this.tabBar_) {                                                                          // 3224
          this.tabBar_.classList.remove(this.CssClasses_.CASTING_SHADOW);                            // 3225
        }                                                                                            // 3226
      } else if (mode === this.Mode_.WATERFALL) {                                                    // 3227
        // Add and remove shadows depending on scroll position.                                      // 3228
        // Also add/remove auxiliary class for styling of the compact version of                     // 3229
        // the header.                                                                               // 3230
        this.content_.addEventListener('scroll',                                                     // 3231
            this.contentScrollHandler_.bind(this));                                                  // 3232
        this.contentScrollHandler_();                                                                // 3233
      }                                                                                              // 3234
    }                                                                                                // 3235
                                                                                                     // 3236
    // Add drawer toggling button to our layout, if we have an openable drawer.                      // 3237
    if (this.drawer_) {                                                                              // 3238
      var drawerButton = document.createElement('div');                                              // 3239
      drawerButton.classList.add(this.CssClasses_.DRAWER_BTN);                                       // 3240
      var drawerButtonIcon = document.createElement('i');                                            // 3241
      drawerButtonIcon.classList.add(this.CssClasses_.ICON);                                         // 3242
      drawerButtonIcon.textContent = this.Constant_.MENU_ICON;                                       // 3243
      drawerButton.appendChild(drawerButtonIcon);                                                    // 3244
      drawerButton.addEventListener('click',                                                         // 3245
          this.drawerToggleHandler_.bind(this));                                                     // 3246
                                                                                                     // 3247
      // Add a class if the layout has a drawer, for altering the left padding.                      // 3248
      // Adds the HAS_DRAWER to the elements since this.header_ may or may                           // 3249
      // not be present.                                                                             // 3250
      this.element_.classList.add(this.CssClasses_.HAS_DRAWER);                                      // 3251
                                                                                                     // 3252
      // If we have a fixed header, add the button to the header rather than                         // 3253
      // the layout.                                                                                 // 3254
      if (this.element_.classList.contains(this.CssClasses_.FIXED_HEADER)) {                         // 3255
        this.header_.insertBefore(drawerButton, this.header_.firstChild);                            // 3256
      } else {                                                                                       // 3257
        this.element_.insertBefore(drawerButton, this.content_);                                     // 3258
      }                                                                                              // 3259
                                                                                                     // 3260
      var obfuscator = document.createElement('div');                                                // 3261
      obfuscator.classList.add(this.CssClasses_.OBFUSCATOR);                                         // 3262
      this.element_.appendChild(obfuscator);                                                         // 3263
      obfuscator.addEventListener('click',                                                           // 3264
          this.drawerToggleHandler_.bind(this));                                                     // 3265
    }                                                                                                // 3266
                                                                                                     // 3267
    // Initialize tabs, if any.                                                                      // 3268
    if (this.header_ && this.tabBar_) {                                                              // 3269
      this.element_.classList.add(this.CssClasses_.HAS_TABS);                                        // 3270
                                                                                                     // 3271
      var tabContainer = document.createElement('div');                                              // 3272
      tabContainer.classList.add(this.CssClasses_.TAB_CONTAINER);                                    // 3273
      this.header_.insertBefore(tabContainer, this.tabBar_);                                         // 3274
      this.header_.removeChild(this.tabBar_);                                                        // 3275
                                                                                                     // 3276
      var leftButton = document.createElement('div');                                                // 3277
      leftButton.classList.add(this.CssClasses_.TAB_BAR_BUTTON);                                     // 3278
      leftButton.classList.add(this.CssClasses_.TAB_BAR_LEFT_BUTTON);                                // 3279
      var leftButtonIcon = document.createElement('i');                                              // 3280
      leftButtonIcon.classList.add(this.CssClasses_.ICON);                                           // 3281
      leftButtonIcon.textContent = this.Constant_.CHEVRON_LEFT;                                      // 3282
      leftButton.appendChild(leftButtonIcon);                                                        // 3283
      leftButton.addEventListener('click', function() {                                              // 3284
        this.tabBar_.scrollLeft -= this.Constant_.TAB_SCROLL_PIXELS;                                 // 3285
      }.bind(this));                                                                                 // 3286
                                                                                                     // 3287
      var rightButton = document.createElement('div');                                               // 3288
      rightButton.classList.add(this.CssClasses_.TAB_BAR_BUTTON);                                    // 3289
      rightButton.classList.add(this.CssClasses_.TAB_BAR_RIGHT_BUTTON);                              // 3290
      var rightButtonIcon = document.createElement('i');                                             // 3291
      rightButtonIcon.classList.add(this.CssClasses_.ICON);                                          // 3292
      rightButtonIcon.textContent = this.Constant_.CHEVRON_RIGHT;                                    // 3293
      rightButton.appendChild(rightButtonIcon);                                                      // 3294
      rightButton.addEventListener('click', function() {                                             // 3295
        this.tabBar_.scrollLeft += this.Constant_.TAB_SCROLL_PIXELS;                                 // 3296
      }.bind(this));                                                                                 // 3297
                                                                                                     // 3298
      tabContainer.appendChild(leftButton);                                                          // 3299
      tabContainer.appendChild(this.tabBar_);                                                        // 3300
      tabContainer.appendChild(rightButton);                                                         // 3301
                                                                                                     // 3302
      // Add and remove buttons depending on scroll position.                                        // 3303
      var tabScrollHandler = function() {                                                            // 3304
        if (this.tabBar_.scrollLeft > 0) {                                                           // 3305
          leftButton.classList.add(this.CssClasses_.IS_ACTIVE);                                      // 3306
        } else {                                                                                     // 3307
          leftButton.classList.remove(this.CssClasses_.IS_ACTIVE);                                   // 3308
        }                                                                                            // 3309
                                                                                                     // 3310
        if (this.tabBar_.scrollLeft <                                                                // 3311
            this.tabBar_.scrollWidth - this.tabBar_.offsetWidth) {                                   // 3312
          rightButton.classList.add(this.CssClasses_.IS_ACTIVE);                                     // 3313
        } else {                                                                                     // 3314
          rightButton.classList.remove(this.CssClasses_.IS_ACTIVE);                                  // 3315
        }                                                                                            // 3316
      }.bind(this);                                                                                  // 3317
                                                                                                     // 3318
      this.tabBar_.addEventListener('scroll', tabScrollHandler);                                     // 3319
      tabScrollHandler();                                                                            // 3320
                                                                                                     // 3321
      if (this.tabBar_.classList.contains(this.CssClasses_.JS_RIPPLE_EFFECT)) {                      // 3322
        this.tabBar_.classList.add(this.CssClasses_.RIPPLE_IGNORE_EVENTS);                           // 3323
      }                                                                                              // 3324
                                                                                                     // 3325
      // Select element tabs, document panels                                                        // 3326
      var tabs = this.tabBar_.querySelectorAll('.' + this.CssClasses_.TAB);                          // 3327
      var panels = this.content_.querySelectorAll('.' + this.CssClasses_.PANEL);                     // 3328
                                                                                                     // 3329
      // Create new tabs for each tab element                                                        // 3330
      for (var i = 0; i < tabs.length; i++) {                                                        // 3331
        new MaterialLayoutTab(tabs[i], tabs, panels, this);                                          // 3332
      }                                                                                              // 3333
    }                                                                                                // 3334
                                                                                                     // 3335
    this.element_.classList.add(this.CssClasses_.IS_UPGRADED);                                       // 3336
  }                                                                                                  // 3337
};                                                                                                   // 3338
                                                                                                     // 3339
function MaterialLayoutTab(tab, tabs, panels, layout) {                                              // 3340
  'use strict';                                                                                      // 3341
                                                                                                     // 3342
  if (tab) {                                                                                         // 3343
    if (layout.tabBar_.classList.contains(                                                           // 3344
        layout.CssClasses_.JS_RIPPLE_EFFECT)) {                                                      // 3345
      var rippleContainer = document.createElement('span');                                          // 3346
      rippleContainer.classList.add(layout.CssClasses_.RIPPLE_CONTAINER);                            // 3347
      rippleContainer.classList.add(layout.CssClasses_.JS_RIPPLE_EFFECT);                            // 3348
      var ripple = document.createElement('span');                                                   // 3349
      ripple.classList.add(layout.CssClasses_.RIPPLE);                                               // 3350
      rippleContainer.appendChild(ripple);                                                           // 3351
      tab.appendChild(rippleContainer);                                                              // 3352
    }                                                                                                // 3353
                                                                                                     // 3354
    tab.addEventListener('click', function(e) {                                                      // 3355
      e.preventDefault();                                                                            // 3356
      var href = tab.href.split('#')[1];                                                             // 3357
      var panel = layout.content_.querySelector('#' + href);                                         // 3358
      layout.resetTabState_(tabs);                                                                   // 3359
      layout.resetPanelState_(panels);                                                               // 3360
      tab.classList.add(layout.CssClasses_.IS_ACTIVE);                                               // 3361
      panel.classList.add(layout.CssClasses_.IS_ACTIVE);                                             // 3362
    });                                                                                              // 3363
                                                                                                     // 3364
  }                                                                                                  // 3365
}                                                                                                    // 3366
                                                                                                     // 3367
// The component registers itself. It can assume componentHandler is available                       // 3368
// in the global scope.                                                                              // 3369
componentHandler.register({                                                                          // 3370
  constructor: MaterialLayout,                                                                       // 3371
  classAsString: 'MaterialLayout',                                                                   // 3372
  cssClass: 'mdl-js-layout'                                                                          // 3373
});                                                                                                  // 3374
                                                                                                     // 3375
/**                                                                                                  // 3376
 * @license                                                                                          // 3377
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 3378
 *                                                                                                   // 3379
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 3380
 * you may not use this file except in compliance with the License.                                  // 3381
 * You may obtain a copy of the License at                                                           // 3382
 *                                                                                                   // 3383
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 3384
 *                                                                                                   // 3385
 * Unless required by applicable law or agreed to in writing, software                               // 3386
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 3387
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 3388
 * See the License for the specific language governing permissions and                               // 3389
 * limitations under the License.                                                                    // 3390
 */                                                                                                  // 3391
                                                                                                     // 3392
/**                                                                                                  // 3393
 * Class constructor for Data Table Card MDL component.                                              // 3394
 * Implements MDL component design pattern defined at:                                               // 3395
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 3396
 * @param {HTMLElement} element The element that will be upgraded.                                   // 3397
 */                                                                                                  // 3398
function MaterialDataTable(element) {                                                                // 3399
  'use strict';                                                                                      // 3400
                                                                                                     // 3401
  this.element_ = element;                                                                           // 3402
                                                                                                     // 3403
  // Initialize instance.                                                                            // 3404
  this.init();                                                                                       // 3405
}                                                                                                    // 3406
                                                                                                     // 3407
/**                                                                                                  // 3408
 * Store constants in one place so they can be updated easily.                                       // 3409
 * @enum {string | number}                                                                           // 3410
 * @private                                                                                          // 3411
 */                                                                                                  // 3412
MaterialDataTable.prototype.Constant_ = {                                                            // 3413
  // None at the moment.                                                                             // 3414
};                                                                                                   // 3415
                                                                                                     // 3416
/**                                                                                                  // 3417
 * Store strings for class names defined by this component that are used in                          // 3418
 * JavaScript. This allows us to simply change it in one place should we                             // 3419
 * decide to modify at a later date.                                                                 // 3420
 * @enum {string}                                                                                    // 3421
 * @private                                                                                          // 3422
 */                                                                                                  // 3423
MaterialDataTable.prototype.CssClasses_ = {                                                          // 3424
  DATA_TABLE: 'mdl-data-table',                                                                      // 3425
  SELECTABLE: 'mdl-data-table--selectable',                                                          // 3426
  IS_SELECTED: 'is-selected',                                                                        // 3427
  IS_UPGRADED: 'is-upgraded'                                                                         // 3428
};                                                                                                   // 3429
                                                                                                     // 3430
MaterialDataTable.prototype.selectRow_ = function(checkbox, row, rows) {                             // 3431
  'use strict';                                                                                      // 3432
                                                                                                     // 3433
  if (row) {                                                                                         // 3434
    return function() {                                                                              // 3435
      if (checkbox.checked) {                                                                        // 3436
        row.classList.add(this.CssClasses_.IS_SELECTED);                                             // 3437
      } else {                                                                                       // 3438
        row.classList.remove(this.CssClasses_.IS_SELECTED);                                          // 3439
      }                                                                                              // 3440
    }.bind(this);                                                                                    // 3441
  }                                                                                                  // 3442
                                                                                                     // 3443
  if (rows) {                                                                                        // 3444
    return function() {                                                                              // 3445
      var i;                                                                                         // 3446
      var el;                                                                                        // 3447
      if (checkbox.checked) {                                                                        // 3448
        for (i = 0; i < rows.length; i++) {                                                          // 3449
          el = rows[i].querySelector('td').querySelector('.mdl-checkbox');                           // 3450
          el.MaterialCheckbox.check();                                                               // 3451
          rows[i].classList.add(this.CssClasses_.IS_SELECTED);                                       // 3452
        }                                                                                            // 3453
      } else {                                                                                       // 3454
        for (i = 0; i < rows.length; i++) {                                                          // 3455
          el = rows[i].querySelector('td').querySelector('.mdl-checkbox');                           // 3456
          el.MaterialCheckbox.uncheck();                                                             // 3457
          rows[i].classList.remove(this.CssClasses_.IS_SELECTED);                                    // 3458
        }                                                                                            // 3459
      }                                                                                              // 3460
    }.bind(this);                                                                                    // 3461
  }                                                                                                  // 3462
};                                                                                                   // 3463
                                                                                                     // 3464
MaterialDataTable.prototype.createCheckbox_ = function(row, rows) {                                  // 3465
  'use strict';                                                                                      // 3466
                                                                                                     // 3467
  var label = document.createElement('label');                                                       // 3468
  label.classList.add('mdl-checkbox');                                                               // 3469
  label.classList.add('mdl-js-checkbox');                                                            // 3470
  label.classList.add('mdl-js-ripple-effect');                                                       // 3471
  label.classList.add('mdl-data-table__select');                                                     // 3472
  var checkbox = document.createElement('input');                                                    // 3473
  checkbox.type = 'checkbox';                                                                        // 3474
  checkbox.classList.add('mdl-checkbox__input');                                                     // 3475
  if (row) {                                                                                         // 3476
    checkbox.addEventListener('change', this.selectRow_(checkbox, row));                             // 3477
  } else if (rows) {                                                                                 // 3478
    checkbox.addEventListener('change', this.selectRow_(checkbox, null, rows));                      // 3479
  }                                                                                                  // 3480
  label.appendChild(checkbox);                                                                       // 3481
  componentHandler.upgradeElement(label, 'MaterialCheckbox');                                        // 3482
  return label;                                                                                      // 3483
};                                                                                                   // 3484
                                                                                                     // 3485
/**                                                                                                  // 3486
 * Initialize element.                                                                               // 3487
 */                                                                                                  // 3488
MaterialDataTable.prototype.init = function() {                                                      // 3489
  'use strict';                                                                                      // 3490
                                                                                                     // 3491
  if (this.element_) {                                                                               // 3492
                                                                                                     // 3493
    var firstHeader = this.element_.querySelector('th');                                             // 3494
    var rows = this.element_.querySelector('tbody').querySelectorAll('tr');                          // 3495
                                                                                                     // 3496
    if (this.element_.classList.contains(this.CssClasses_.SELECTABLE)) {                             // 3497
      var th = document.createElement('th');                                                         // 3498
      var headerCheckbox = this.createCheckbox_(null, rows);                                         // 3499
      th.appendChild(headerCheckbox);                                                                // 3500
      firstHeader.parentElement.insertBefore(th, firstHeader);                                       // 3501
                                                                                                     // 3502
      for (var i = 0; i < rows.length; i++) {                                                        // 3503
        var firstCell = rows[i].querySelector('td');                                                 // 3504
        if (firstCell) {                                                                             // 3505
          var td = document.createElement('td');                                                     // 3506
          var rowCheckbox = this.createCheckbox_(rows[i]);                                           // 3507
          td.appendChild(rowCheckbox);                                                               // 3508
          rows[i].insertBefore(td, firstCell);                                                       // 3509
        }                                                                                            // 3510
      }                                                                                              // 3511
    }                                                                                                // 3512
                                                                                                     // 3513
    this.element_.classList.add(this.CssClasses_.IS_UPGRADED);                                       // 3514
  }                                                                                                  // 3515
};                                                                                                   // 3516
                                                                                                     // 3517
// The component registers itself. It can assume componentHandler is available                       // 3518
// in the global scope.                                                                              // 3519
componentHandler.register({                                                                          // 3520
  constructor: MaterialDataTable,                                                                    // 3521
  classAsString: 'MaterialDataTable',                                                                // 3522
  cssClass: 'mdl-js-data-table'                                                                      // 3523
});                                                                                                  // 3524
                                                                                                     // 3525
/**                                                                                                  // 3526
 * @license                                                                                          // 3527
 * Copyright 2015 Google Inc. All Rights Reserved.                                                   // 3528
 *                                                                                                   // 3529
 * Licensed under the Apache License, Version 2.0 (the "License");                                   // 3530
 * you may not use this file except in compliance with the License.                                  // 3531
 * You may obtain a copy of the License at                                                           // 3532
 *                                                                                                   // 3533
 *      http://www.apache.org/licenses/LICENSE-2.0                                                   // 3534
 *                                                                                                   // 3535
 * Unless required by applicable law or agreed to in writing, software                               // 3536
 * distributed under the License is distributed on an "AS IS" BASIS,                                 // 3537
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                          // 3538
 * See the License for the specific language governing permissions and                               // 3539
 * limitations under the License.                                                                    // 3540
 */                                                                                                  // 3541
                                                                                                     // 3542
/**                                                                                                  // 3543
 * Class constructor for Ripple MDL component.                                                       // 3544
 * Implements MDL component design pattern defined at:                                               // 3545
 * https://github.com/jasonmayes/mdl-component-design-pattern                                        // 3546
 * @param {HTMLElement} element The element that will be upgraded.                                   // 3547
 */                                                                                                  // 3548
function MaterialRipple(element) {                                                                   // 3549
  'use strict';                                                                                      // 3550
                                                                                                     // 3551
  this.element_ = element;                                                                           // 3552
                                                                                                     // 3553
  // Initialize instance.                                                                            // 3554
  this.init();                                                                                       // 3555
}                                                                                                    // 3556
                                                                                                     // 3557
/**                                                                                                  // 3558
 * Store constants in one place so they can be updated easily.                                       // 3559
 * @enum {string | number}                                                                           // 3560
 * @private                                                                                          // 3561
 */                                                                                                  // 3562
MaterialRipple.prototype.Constant_ = {                                                               // 3563
  INITIAL_SCALE: 'scale(0.0001, 0.0001)',                                                            // 3564
  INITIAL_SIZE: '1px',                                                                               // 3565
  INITIAL_OPACITY: '0.4',                                                                            // 3566
  FINAL_OPACITY: '0',                                                                                // 3567
  FINAL_SCALE: ''                                                                                    // 3568
};                                                                                                   // 3569
                                                                                                     // 3570
/**                                                                                                  // 3571
 * Store strings for class names defined by this component that are used in                          // 3572
 * JavaScript. This allows us to simply change it in one place should we                             // 3573
 * decide to modify at a later date.                                                                 // 3574
 * @enum {string}                                                                                    // 3575
 * @private                                                                                          // 3576
 */                                                                                                  // 3577
MaterialRipple.prototype.CssClasses_ = {                                                             // 3578
  RIPPLE_CENTER: 'mdl-ripple--center',                                                               // 3579
  RIPPLE_EFFECT_IGNORE_EVENTS: 'mdl-js-ripple-effect--ignore-events',                                // 3580
  RIPPLE: 'mdl-ripple',                                                                              // 3581
  IS_ANIMATING: 'is-animating',                                                                      // 3582
  IS_VISIBLE: 'is-visible'                                                                           // 3583
};                                                                                                   // 3584
                                                                                                     // 3585
/**                                                                                                  // 3586
 * Handle mouse / finger down on element.                                                            // 3587
 * @param {Event} event The event that fired.                                                        // 3588
 * @private                                                                                          // 3589
 */                                                                                                  // 3590
MaterialRipple.prototype.downHandler_ = function(event) {                                            // 3591
  'use strict';                                                                                      // 3592
                                                                                                     // 3593
  if (!this.rippleElement_.style.width && !this.rippleElement_.style.height) {                       // 3594
    var rect = this.element_.getBoundingClientRect();                                                // 3595
    this.boundHeight = rect.height;                                                                  // 3596
    this.boundWidth = rect.width;                                                                    // 3597
    this.rippleSize_ = Math.sqrt(rect.width * rect.width +                                           // 3598
        rect.height * rect.height) * 2 + 2;                                                          // 3599
    this.rippleElement_.style.width = this.rippleSize_ + 'px';                                       // 3600
    this.rippleElement_.style.height = this.rippleSize_ + 'px';                                      // 3601
  }                                                                                                  // 3602
                                                                                                     // 3603
  this.rippleElement_.classList.add(this.CssClasses_.IS_VISIBLE);                                    // 3604
                                                                                                     // 3605
  if (event.type === 'mousedown' && this.ignoringMouseDown_) {                                       // 3606
    this.ignoringMouseDown_ = false;                                                                 // 3607
  } else {                                                                                           // 3608
    if (event.type === 'touchstart') {                                                               // 3609
      this.ignoringMouseDown_ = true;                                                                // 3610
    }                                                                                                // 3611
    var frameCount = this.getFrameCount();                                                           // 3612
    if (frameCount > 0) {                                                                            // 3613
      return;                                                                                        // 3614
    }                                                                                                // 3615
    this.setFrameCount(1);                                                                           // 3616
    var bound = event.currentTarget.getBoundingClientRect();                                         // 3617
    var x;                                                                                           // 3618
    var y;                                                                                           // 3619
    // Check if we are handling a keyboard click.                                                    // 3620
    if (event.clientX === 0 && event.clientY === 0) {                                                // 3621
      x = Math.round(bound.width / 2);                                                               // 3622
      y = Math.round(bound.height / 2);                                                              // 3623
    } else {                                                                                         // 3624
      var clientX = event.clientX ? event.clientX : event.touches[0].clientX;                        // 3625
      var clientY = event.clientY ? event.clientY : event.touches[0].clientY;                        // 3626
      x = Math.round(clientX - bound.left);                                                          // 3627
      y = Math.round(clientY - bound.top);                                                           // 3628
    }                                                                                                // 3629
    this.setRippleXY(x, y);                                                                          // 3630
    this.setRippleStyles(true);                                                                      // 3631
    window.requestAnimationFrame(this.animFrameHandler.bind(this));                                  // 3632
  }                                                                                                  // 3633
};                                                                                                   // 3634
                                                                                                     // 3635
/**                                                                                                  // 3636
 * Handle mouse / finger up on element.                                                              // 3637
 * @param {Event} event The event that fired.                                                        // 3638
 * @private                                                                                          // 3639
 */                                                                                                  // 3640
MaterialRipple.prototype.upHandler_ = function(event) {                                              // 3641
  'use strict';                                                                                      // 3642
                                                                                                     // 3643
  // Don't fire for the artificial "mouseup" generated by a double-click.                            // 3644
  if (event && event.detail !== 2) {                                                                 // 3645
    this.rippleElement_.classList.remove(this.CssClasses_.IS_VISIBLE);                               // 3646
  }                                                                                                  // 3647
};                                                                                                   // 3648
                                                                                                     // 3649
/**                                                                                                  // 3650
 * Initialize element.                                                                               // 3651
 */                                                                                                  // 3652
MaterialRipple.prototype.init = function() {                                                         // 3653
  'use strict';                                                                                      // 3654
                                                                                                     // 3655
  if (this.element_) {                                                                               // 3656
    var recentering =                                                                                // 3657
        this.element_.classList.contains(this.CssClasses_.RIPPLE_CENTER);                            // 3658
    if (!this.element_.classList.contains(                                                           // 3659
        this.CssClasses_.RIPPLE_EFFECT_IGNORE_EVENTS)) {                                             // 3660
      this.rippleElement_ = this.element_.querySelector('.' +                                        // 3661
          this.CssClasses_.RIPPLE);                                                                  // 3662
      this.frameCount_ = 0;                                                                          // 3663
      this.rippleSize_ = 0;                                                                          // 3664
      this.x_ = 0;                                                                                   // 3665
      this.y_ = 0;                                                                                   // 3666
                                                                                                     // 3667
      // Touch start produces a compat mouse down event, which would cause a                         // 3668
      // second ripples. To avoid that, we use this property to ignore the first                     // 3669
      // mouse down after a touch start.                                                             // 3670
      this.ignoringMouseDown_ = false;                                                               // 3671
                                                                                                     // 3672
      this.boundDownHandler = this.downHandler_.bind(this);                                          // 3673
      this.element_.addEventListener('mousedown',                                                    // 3674
        this.boundDownHandler);                                                                      // 3675
      this.element_.addEventListener('touchstart',                                                   // 3676
          this.boundDownHandler);                                                                    // 3677
                                                                                                     // 3678
      this.boundUpHandler = this.upHandler_.bind(this);                                              // 3679
      this.element_.addEventListener('mouseup', this.boundUpHandler);                                // 3680
      this.element_.addEventListener('mouseleave', this.boundUpHandler);                             // 3681
      this.element_.addEventListener('touchend', this.boundUpHandler);                               // 3682
      this.element_.addEventListener('blur', this.boundUpHandler);                                   // 3683
                                                                                                     // 3684
      this.getFrameCount = function() {                                                              // 3685
        return this.frameCount_;                                                                     // 3686
      };                                                                                             // 3687
                                                                                                     // 3688
      this.setFrameCount = function(fC) {                                                            // 3689
        this.frameCount_ = fC;                                                                       // 3690
      };                                                                                             // 3691
                                                                                                     // 3692
      this.getRippleElement = function() {                                                           // 3693
        return this.rippleElement_;                                                                  // 3694
      };                                                                                             // 3695
                                                                                                     // 3696
      this.setRippleXY = function(newX, newY) {                                                      // 3697
        this.x_ = newX;                                                                              // 3698
        this.y_ = newY;                                                                              // 3699
      };                                                                                             // 3700
                                                                                                     // 3701
      this.setRippleStyles = function(start) {                                                       // 3702
        if (this.rippleElement_ !== null) {                                                          // 3703
          var transformString;                                                                       // 3704
          var scale;                                                                                 // 3705
          var size;                                                                                  // 3706
          var offset = 'translate(' + this.x_ + 'px, ' + this.y_ + 'px)';                            // 3707
                                                                                                     // 3708
          if (start) {                                                                               // 3709
            scale = this.Constant_.INITIAL_SCALE;                                                    // 3710
            size = this.Constant_.INITIAL_SIZE;                                                      // 3711
          } else {                                                                                   // 3712
            scale = this.Constant_.FINAL_SCALE;                                                      // 3713
            size = this.rippleSize_ + 'px';                                                          // 3714
            if (recentering) {                                                                       // 3715
              offset = 'translate(' + this.boundWidth / 2 + 'px, ' +                                 // 3716
                this.boundHeight / 2 + 'px)';                                                        // 3717
            }                                                                                        // 3718
          }                                                                                          // 3719
                                                                                                     // 3720
          transformString = 'translate(-50%, -50%) ' + offset + scale;                               // 3721
                                                                                                     // 3722
          this.rippleElement_.style.webkitTransform = transformString;                               // 3723
          this.rippleElement_.style.msTransform = transformString;                                   // 3724
          this.rippleElement_.style.transform = transformString;                                     // 3725
                                                                                                     // 3726
          if (start) {                                                                               // 3727
            this.rippleElement_.classList.remove(this.CssClasses_.IS_ANIMATING);                     // 3728
          } else {                                                                                   // 3729
            this.rippleElement_.classList.add(this.CssClasses_.IS_ANIMATING);                        // 3730
          }                                                                                          // 3731
        }                                                                                            // 3732
      };                                                                                             // 3733
                                                                                                     // 3734
      this.animFrameHandler = function() {                                                           // 3735
        if (this.frameCount_-- > 0) {                                                                // 3736
          window.requestAnimationFrame(this.animFrameHandler.bind(this));                            // 3737
        } else {                                                                                     // 3738
          this.setRippleStyles(false);                                                               // 3739
        }                                                                                            // 3740
      };                                                                                             // 3741
    }                                                                                                // 3742
  }                                                                                                  // 3743
};                                                                                                   // 3744
                                                                                                     // 3745
/*                                                                                                   // 3746
* Downgrade the component                                                                            // 3747
*/                                                                                                   // 3748
MaterialRipple.prototype.mdlDowngrade_ = function() {                                                // 3749
  'use strict';                                                                                      // 3750
  this.element_.removeEventListener('mousedown',                                                     // 3751
  this.boundDownHandler);                                                                            // 3752
  this.element_.removeEventListener('touchstart',                                                    // 3753
      this.boundDownHandler);                                                                        // 3754
                                                                                                     // 3755
  this.element_.removeEventListener('mouseup', this.boundUpHandler);                                 // 3756
  this.element_.removeEventListener('mouseleave', this.boundUpHandler);                              // 3757
  this.element_.removeEventListener('touchend', this.boundUpHandler);                                // 3758
  this.element_.removeEventListener('blur', this.boundUpHandler);                                    // 3759
};                                                                                                   // 3760
                                                                                                     // 3761
// The component registers itself. It can assume componentHandler is available                       // 3762
// in the global scope.                                                                              // 3763
componentHandler.register({                                                                          // 3764
  constructor: MaterialRipple,                                                                       // 3765
  classAsString: 'MaterialRipple',                                                                   // 3766
  cssClass: 'mdl-js-ripple-effect',                                                                  // 3767
  widget: false                                                                                      // 3768
});                                                                                                  // 3769
                                                                                                     // 3770
///////////////////////////////////////////////////////////////////////////////////////////////////////      // 3779
                                                                                                             // 3780
}).call(this);                                                                                               // 3781
                                                                                                             // 3782
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

}).call(this);


/* Exports */
if (typeof Package === 'undefined') Package = {};
Package['spectrum:material-design-lite'] = {};

})();
