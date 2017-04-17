Ext.Loader.setConfig({
    enabled: true
});

Ext.application({
    name: 'SE',
    requires: ['SE.view.MainView'], // <== list of libraries to be preloaded
    views: [
        'Sessions',
        'SessionForm'
    ], // <== No need to specify 'SE.view'
    stores: [
        'Sessions'
    ],
    models: [
        'Session'
    ],
    launch: function () {
        Ext.create('SE.view.MainView'); // <== we ask ExtJS to look for a file named 'view/MainView.js'
    }
});
