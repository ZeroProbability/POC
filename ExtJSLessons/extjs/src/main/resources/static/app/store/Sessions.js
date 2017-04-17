Ext.define('SE.store.Sessions', {
    extend: 'Ext.data.Store',
    model: 'SE.model.Session',

    autoLoad: true, // <== load the data the first time
    autoSync: true, // <== when data in grid is changed, the store will be update
    sorters: [ // <== Defines default sort columns
        {property: 'approved'},
        {property: 'title'}
    ],
    groupField: 'level' // <== defines
});