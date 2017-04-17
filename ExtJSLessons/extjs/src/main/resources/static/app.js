Ext.Loader.setConfig({
    enabled: true
});

Ext.application({
    name: 'SE',
    requires: ['SE.view.MainView'], // <== list of libraries to be preloaded
    views: [
        'Sessions',
        'SessionForm',
        'Presenters'
    ], // <== No need to specify 'SE.view'
    controllers: [
        'SE.controller.SessionController'
    ],
    stores: [
        'Sessions',
        'SessionPresenters',
        'Presenters'
    ],
    models: [
        'Session',
        'SessionPresenter',
        'Presenter'
    ],
    launch: function () {
        Ext.create('SE.view.MainView'); // <== we ask ExtJS to look for a file named 'view/MainView.js'
    }
});
