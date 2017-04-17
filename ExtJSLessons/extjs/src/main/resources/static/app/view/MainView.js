Ext.define('SE.view.MainView', {
    extend: "Ext.container.Viewport",
    layout: 'fit',
    items: [ {
        layout: {
            type: 'border' // <== better than hbox in general because has more capability
        },
        items: [
            {
                region: 'west',
                layout: {
                    type: 'vbox',
                    align: 'stretch'
                },
                flex: 1, // <== Without this 'flex' attribute collapsing the
                         // center panel doesn't expand left panel.
                items: [
                    {
                        xtype: 'sessiongridpanel',
                        html: 'sessions',
                        flex: 3
                    }, {
                        xtype: 'splitter'
                    },
                    {
                        xtype: 'panel',
                        html:'<b>Speakers panel</b>',
                        flex: 2
                    }
                ]
            },
            {
                region: 'center', //<== All 'border' layout should have a center
                xtype: 'panel',
                html:'<b>Details panel</b>',
                flex: 1,
                title: 'Details panel'
            }
        ]
    }]
});
