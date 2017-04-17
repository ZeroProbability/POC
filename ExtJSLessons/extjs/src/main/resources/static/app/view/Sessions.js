Ext.define("SE.view.Sessions", {
    extend: 'Ext.grid.Panel',         // <== this is the way to extend grid panel and create our own
    alias: 'widget.sessiongridpanel', // <== assigning an alias allows us to later refer to this using xtype

    store: 'Sessions', // <== lookup 'Sessions' from app.js
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
