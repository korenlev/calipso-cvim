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

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                                  //
// packages/pcel_loading/packages/pcel_loading.js                                                                   //
//                                                                                                                  //
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                                    //
(function () {                                                                                                      // 1
                                                                                                                    // 2
///////////////////////////////////////////////////////////////////////////////////////////////////////////////     // 3
//                                                                                                           //     // 4
// packages/pcel:loading/lib/please-wait.js                                                                  //     // 5
//                                                                                                           //     // 6
///////////////////////////////////////////////////////////////////////////////////////////////////////////////     // 7
                                                                                                             //     // 8
/**                                                                                                          // 1   // 9
* Please Wait                                                                                                // 2   // 10
* Display a nice loading screen while your app loads                                                         // 3   // 11
                                                                                                             // 4   // 12
* @author Pathgather <tech@pathgather.com>                                                                   // 5   // 13
* @copyright Pathgather 2014                                                                                 // 6   // 14
* @license MIT <http://opensource.org/licenses/mit-license.php>                                              // 7   // 15
* @link https://github.com/Pathgather/please-wait                                                            // 8   // 16
* @module pleaseWait                                                                                         // 9   // 17
* @version 0.0.1                                                                                             // 10  // 18
*/                                                                                                           // 11  // 19
(function(root, factory) {                                                                                   // 12  // 20
  if (typeof exports === "object") {                                                                         // 13  // 21
    factory(exports);                                                                                        // 14  // 22
  } else if (typeof define === "function" && define.amd) {                                                   // 15  // 23
    define(["exports"], factory);                                                                            // 16  // 24
  } else {                                                                                                   // 17  // 25
    factory(root);                                                                                           // 18  // 26
  }                                                                                                          // 19  // 27
})(this, function(exports) {                                                                                 // 20  // 28
  var PleaseWait, animationEvent, animationSupport, domPrefixes, elm, key, pfx, pleaseWait, transEndEventNames, transitionEvent, transitionSupport, val, _i, _len;
  elm = document.createElement('fakeelement');                                                               // 22  // 30
  animationSupport = false;                                                                                  // 23  // 31
  transitionSupport = false;                                                                                 // 24  // 32
  animationEvent = 'animationend';                                                                           // 25  // 33
  transitionEvent = null;                                                                                    // 26  // 34
  domPrefixes = 'Webkit Moz O ms'.split(' ');                                                                // 27  // 35
  transEndEventNames = {                                                                                     // 28  // 36
    'WebkitTransition': 'webkitTransitionEnd',                                                               // 29  // 37
    'MozTransition': 'transitionend',                                                                        // 30  // 38
    'OTransition': 'oTransitionEnd',                                                                         // 31  // 39
    'msTransition': 'MSTransitionEnd',                                                                       // 32  // 40
    'transition': 'transitionend'                                                                            // 33  // 41
  };                                                                                                         // 34  // 42
  for (key in transEndEventNames) {                                                                          // 35  // 43
    val = transEndEventNames[key];                                                                           // 36  // 44
    if (elm.style[key] != null) {                                                                            // 37  // 45
      transitionEvent = val;                                                                                 // 38  // 46
      transitionSupport = true;                                                                              // 39  // 47
      break;                                                                                                 // 40  // 48
    }                                                                                                        // 41  // 49
  }                                                                                                          // 42  // 50
  if (elm.style.animationName != null) {                                                                     // 43  // 51
    animationSupport = true;                                                                                 // 44  // 52
  }                                                                                                          // 45  // 53
  if (!animationSupport) {                                                                                   // 46  // 54
    for (_i = 0, _len = domPrefixes.length; _i < _len; _i++) {                                               // 47  // 55
      pfx = domPrefixes[_i];                                                                                 // 48  // 56
      if (elm.style["" + pfx + "AnimationName"] != null) {                                                   // 49  // 57
        switch (pfx) {                                                                                       // 50  // 58
          case 'Webkit':                                                                                     // 51  // 59
            animationEvent = 'webkitAnimationEnd';                                                           // 52  // 60
            break;                                                                                           // 53  // 61
          case 'Moz':                                                                                        // 54  // 62
            animationEvent = 'animationend';                                                                 // 55  // 63
            break;                                                                                           // 56  // 64
          case 'O':                                                                                          // 57  // 65
            animationEvent = 'oanimationend';                                                                // 58  // 66
            break;                                                                                           // 59  // 67
          case 'ms':                                                                                         // 60  // 68
            animationEvent = 'MSAnimationEnd';                                                               // 61  // 69
        }                                                                                                    // 62  // 70
        animationSupport = true;                                                                             // 63  // 71
        break;                                                                                               // 64  // 72
      }                                                                                                      // 65  // 73
    }                                                                                                        // 66  // 74
  }                                                                                                          // 67  // 75
  PleaseWait = (function() {                                                                                 // 68  // 76
    PleaseWait._defaultOptions = {                                                                           // 69  // 77
      backgroundColor: null,                                                                                 // 70  // 78
      logo: null,                                                                                            // 71  // 79
      loadingHtml: null,                                                                                     // 72  // 80
      template: "<div class='pg-loading-inner'>\n  <div class='pg-loading-center-outer'>\n    <div class='pg-loading-center-middle'>\n      <h1 class='pg-loading-logo-header'>\n        <img class='pg-loading-logo'></img>\n      </h1>\n      <div class='pg-loading-html'>\n      </div>\n    </div>\n  </div>\n</div>"
    };                                                                                                       // 74  // 82
                                                                                                             // 75  // 83
    function PleaseWait(options) {                                                                           // 76  // 84
      var defaultOptions, k, listener, v;                                                                    // 77  // 85
      defaultOptions = this.constructor._defaultOptions;                                                     // 78  // 86
      this.options = {};                                                                                     // 79  // 87
      this.loaded = false;                                                                                   // 80  // 88
      for (k in defaultOptions) {                                                                            // 81  // 89
        v = defaultOptions[k];                                                                               // 82  // 90
        this.options[k] = options[k] != null ? options[k] : v;                                               // 83  // 91
      }                                                                                                      // 84  // 92
      this._loadingElem = document.createElement("div");                                                     // 85  // 93
      this._loadingHtmlToDisplay = [];                                                                       // 86  // 94
      this._loadingElem.className = "pg-loading-screen";                                                     // 87  // 95
      if (this.options.backgroundColor != null) {                                                            // 88  // 96
        this._loadingElem.style.backgroundColor = this.options.backgroundColor;                              // 89  // 97
      }                                                                                                      // 90  // 98
      this._loadingElem.innerHTML = this.options.template;                                                   // 91  // 99
      this._loadingHtmlElem = this._loadingElem.getElementsByClassName("pg-loading-html")[0];                // 92  // 100
      if (this._loadingHtmlElem != null) {                                                                   // 93  // 101
        this._loadingHtmlElem.innerHTML = this.options.loadingHtml;                                          // 94  // 102
      }                                                                                                      // 95  // 103
      this._readyToShowLoadingHtml = false;                                                                  // 96  // 104
      this._logoElem = this._loadingElem.getElementsByClassName("pg-loading-logo")[0];                       // 97  // 105
      if (this._logoElem != null) {                                                                          // 98  // 106
        this._logoElem.src = this.options.logo;                                                              // 99  // 107
      }                                                                                                      // 100
      document.body.className += " pg-loading";                                                              // 101
      document.body.appendChild(this._loadingElem);                                                          // 102
      this._loadingElem.className += " pg-loading";                                                          // 103
      listener = (function(_this) {                                                                          // 104
        return function() {                                                                                  // 105
          _this.loaded = true;                                                                               // 106
          _this._readyToShowLoadingHtml = true;                                                              // 107
          _this._loadingHtmlElem.className += " pg-loaded";                                                  // 108
          if (animationSupport) {                                                                            // 109
            _this._loadingHtmlElem.removeEventListener(animationEvent, listener);                            // 110
          }                                                                                                  // 111
          if (_this._loadingHtmlToDisplay.length > 0) {                                                      // 112
            return _this._changeLoadingHtml();                                                               // 113
          }                                                                                                  // 114
        };                                                                                                   // 115
      })(this);                                                                                              // 116
      if (this._loadingHtmlElem != null) {                                                                   // 117
        if (animationSupport) {                                                                              // 118
          this._loadingHtmlElem.addEventListener(animationEvent, listener);                                  // 119
        } else {                                                                                             // 120
          listener();                                                                                        // 121
        }                                                                                                    // 122
        this._loadingHtmlListener = (function(_this) {                                                       // 123
          return function() {                                                                                // 124
            _this._readyToShowLoadingHtml = true;                                                            // 125
            _this._loadingHtmlElem.className = _this._loadingHtmlElem.className.replace(" pg-loading ", ""); // 126
            if (transitionSupport) {                                                                         // 127
              _this._loadingHtmlElem.removeEventListener(transitionEvent, _this._loadingHtmlListener);       // 128
            }                                                                                                // 129
            if (_this._loadingHtmlToDisplay.length > 0) {                                                    // 130
              return _this._changeLoadingHtml();                                                             // 131
            }                                                                                                // 132
          };                                                                                                 // 133
        })(this);                                                                                            // 134
        this._removingHtmlListener = (function(_this) {                                                      // 135
          return function() {                                                                                // 136
            _this._loadingHtmlElem.innerHTML = _this._loadingHtmlToDisplay.shift();                          // 137
            _this._loadingHtmlElem.className = _this._loadingHtmlElem.className.replace(" pg-removing ", " pg-loading ");
            if (transitionSupport) {                                                                         // 139
              _this._loadingHtmlElem.removeEventListener(transitionEvent, _this._removingHtmlListener);      // 140
              return _this._loadingHtmlElem.addEventListener(transitionEvent, _this._loadingHtmlListener);   // 141
            } else {                                                                                         // 142
              return _this._loadingHtmlListener();                                                           // 143
            }                                                                                                // 144
          };                                                                                                 // 145
        })(this);                                                                                            // 146
      }                                                                                                      // 147
    }                                                                                                        // 148
                                                                                                             // 149
    PleaseWait.prototype.finish = function(immediately) {                                                    // 150
      var listener;                                                                                          // 151
      if (immediately == null) {                                                                             // 152
        immediately = false;                                                                                 // 153
      }                                                                                                      // 154
      if (this._loadingElem == null) {                                                                       // 155
        return;                                                                                              // 156
      }                                                                                                      // 157
      if (this.loaded || immediately) {                                                                      // 158
        return this._finish();                                                                               // 159
      } else {                                                                                               // 160
        listener = (function(_this) {                                                                        // 161
          return function() {                                                                                // 162
            _this._loadingElem.removeEventListener(animationEvent, listener);                                // 163
            return window.setTimeout(function() {                                                            // 164
              return _this._finish();                                                                        // 165
            }, 1);                                                                                           // 166
          };                                                                                                 // 167
        })(this);                                                                                            // 168
        return this._loadingHtmlElem.addEventListener(animationEvent, listener);                             // 169
      }                                                                                                      // 170
    };                                                                                                       // 171
                                                                                                             // 172
    PleaseWait.prototype.updateOption = function(option, value) {                                            // 173
      switch (option) {                                                                                      // 174
        case 'backgroundColor':                                                                              // 175
          return this._loadingElem.style.backgroundColor = value;                                            // 176
        case 'logo':                                                                                         // 177
          return this._logoElem.src = value;                                                                 // 178
        case 'loadingHtml':                                                                                  // 179
          return this.updateLoadingHtml(value);                                                              // 180
        default:                                                                                             // 181
          throw new Error("Unknown option '" + option + "'");                                                // 182
      }                                                                                                      // 183
    };                                                                                                       // 184
                                                                                                             // 185
    PleaseWait.prototype.updateOptions = function(options) {                                                 // 186
      var k, v, _results;                                                                                    // 187
      if (options == null) {                                                                                 // 188
        options = {};                                                                                        // 189
      }                                                                                                      // 190
      _results = [];                                                                                         // 191
      for (k in options) {                                                                                   // 192
        v = options[k];                                                                                      // 193
        _results.push(this.updateOption(k, v));                                                              // 194
      }                                                                                                      // 195
      return _results;                                                                                       // 196
    };                                                                                                       // 197
                                                                                                             // 198
    PleaseWait.prototype.updateLoadingHtml = function(loadingHtml, immediately) {                            // 199
      if (immediately == null) {                                                                             // 200
        immediately = false;                                                                                 // 201
      }                                                                                                      // 202
      if (this._loadingHtmlElem == null) {                                                                   // 203
        throw new Error("The loading template does not have an element of class 'pg-loading-html'");         // 204
      }                                                                                                      // 205
      if (immediately) {                                                                                     // 206
        this._loadingHtmlToDisplay = [loadingHtml];                                                          // 207
        this._readyToShowLoadingHtml = true;                                                                 // 208
      } else {                                                                                               // 209
        this._loadingHtmlToDisplay.push(loadingHtml);                                                        // 210
      }                                                                                                      // 211
      if (this._readyToShowLoadingHtml) {                                                                    // 212
        return this._changeLoadingHtml();                                                                    // 213
      }                                                                                                      // 214
    };                                                                                                       // 215
                                                                                                             // 216
    PleaseWait.prototype._changeLoadingHtml = function() {                                                   // 217
      this._readyToShowLoadingHtml = false;                                                                  // 218
      this._loadingHtmlElem.removeEventListener(transitionEvent, this._loadingHtmlListener);                 // 219
      this._loadingHtmlElem.removeEventListener(transitionEvent, this._removingHtmlListener);                // 220
      this._loadingHtmlElem.className = this._loadingHtmlElem.className.replace(" pg-loading ", "").replace(" pg-removing ", "");
      if (transitionSupport) {                                                                               // 222
        this._loadingHtmlElem.className += " pg-removing ";                                                  // 223
        return this._loadingHtmlElem.addEventListener(transitionEvent, this._removingHtmlListener);          // 224
      } else {                                                                                               // 225
        return this._removingHtmlListener();                                                                 // 226
      }                                                                                                      // 227
    };                                                                                                       // 228
                                                                                                             // 229
    PleaseWait.prototype._finish = function() {                                                              // 230
      var listener;                                                                                          // 231
      document.body.className += " pg-loaded";                                                               // 232
      listener = (function(_this) {                                                                          // 233
        return function() {                                                                                  // 234
          document.body.removeChild(_this._loadingElem);                                                     // 235
          document.body.className = document.body.className.replace("pg-loading", "");                       // 236
          if (animationSupport) {                                                                            // 237
            _this._loadingElem.removeEventListener(animationEvent, listener);                                // 238
          }                                                                                                  // 239
          return _this._loadingElem = null;                                                                  // 240
        };                                                                                                   // 241
      })(this);                                                                                              // 242
      if (animationSupport) {                                                                                // 243
        this._loadingElem.className += " pg-loaded";                                                         // 244
        return this._loadingElem.addEventListener(animationEvent, listener);                                 // 245
      } else {                                                                                               // 246
        return listener();                                                                                   // 247
      }                                                                                                      // 248
    };                                                                                                       // 249
                                                                                                             // 250
    return PleaseWait;                                                                                       // 251
                                                                                                             // 252
  })();                                                                                                      // 253
  pleaseWait = function(options) {                                                                           // 254
    if (options == null) {                                                                                   // 255
      options = {};                                                                                          // 256
    }                                                                                                        // 257
    return new PleaseWait(options);                                                                          // 258
  };                                                                                                         // 259
  exports.pleaseWait = pleaseWait;                                                                           // 260
  return pleaseWait;                                                                                         // 261
});                                                                                                          // 262
                                                                                                             // 263
///////////////////////////////////////////////////////////////////////////////////////////////////////////////     // 272
                                                                                                                    // 273
}).call(this);                                                                                                      // 274
                                                                                                                    // 275
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

}).call(this);


/* Exports */
if (typeof Package === 'undefined') Package = {};
Package['pcel:loading'] = {};

})();
