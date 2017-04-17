Ext.define("SE.view.Sessions", {
    extend: 'Ext.grid.Panel',         // <== this is the way to extend grid panel and create our own
    alias: 'widget.sessiongridpanel', // <== assigning an alias allows us to later refer to this using xtype

    listeners: {
        itemdblclick: function(gridpanel, record, item, index, e) {   // <== Look at the documentation for
            // Ext.grid.panel to find out the argument
            var formWindow = Ext.create('SE.view.SessionForm');
            var form = formWindow.down('form');     // <== using xtype in 'down'
            form.loadRecord(record);
            formWindow.show();

        }
    },
    store: {
        fields: ['id',
            {
                name: 'title',
                sortType: 'asUCText'  // <== case independent sorting
            },
            'approved',
            'level',
            {
                dateFormat: 'c',  // <== says it is ISO date format
                name: 'sessionTimeDateTime',
                sortType: 'asDate',
                type: 'date'
            },
            {
                convert: function(v, rec) {
                    var convertIt = Ext.util.Format.dateRenderer('m/d/Y g:i a'),
                        pretty = convertIt(rec.get("sessionTimeDateTime"));
                    return pretty;
                },
                name: 'sessionTimePretty',
                type: 'string'
            }
        ],
        autoLoad: true, // <== load the data the first time
        autoSync: true, // <== when data in grid is changed, the store will be update
        proxy: {
            type: 'rest',
            url: '/sessions/all.json',
            reader: {
                type: 'json',
                root: 'data'
            }
        },
        sorters: [ // <== Defines default sort columns
            {property: 'approved'},
            {property: 'title'}
        ],
        groupField: 'level' // <== defines
    },
    columns: [
        {
            xtype: 'gridcolumn',
            text: 'Id',
            dataIndex: 'id'
        },
        {
            xtype: 'gridcolumn',
            text: 'Title',
            dataIndex: 'title',
            flex: 1, // <== assigning flex parameter here but not for other columns
            // makes this column auto expand.
            minWidth: 100,
            width: 75
        },{
            xtype: 'gridcolumn',
            text: 'Level',
            dataIndex: 'level'
        },{
            xtype: 'gridcolumn',
            text: 'Approved',
            dataIndex: 'approved'
        },
        {
            dataIndex: 'sessionTimePretty',
            text: 'Session Start Time',
            width: 180
        }
    ],
    features: [{
        ftype: 'grouping'
    }]

});
