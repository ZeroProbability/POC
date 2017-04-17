Ext.define('SE.model.Session', {
    extend: 'Ext.data.Model',

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
    proxy: {
        type: 'rest',
        url: '/sessions/all.json',
        reader: {
            type: 'json',
            root: 'data'
        }
    }
});