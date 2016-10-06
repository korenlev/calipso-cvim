Template.loading.rendered = function () {
    if ( ! Session.get('loadingSplash') ) {
        this.loading = window.pleaseWait({
            logo: '/cisco-logo-load.png',
            // logo: '',
            backgroundColor: '#2196F3',
            loadingHtml: message + spinner
        });
        Session.set('loadingSplash', true); // just show loading splash once
    }
};

Template.loading.destroyed = function () {
    if ( this.loading ) {
        this.loading.finish();
    }
};

var message = '<p class="loading-message">Loading OSDNA</p>';
var spinner = '<div class="sk-spinner sk-spinner-rotating-plane"></div>';