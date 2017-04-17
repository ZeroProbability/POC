Ext.define('SE.model.Presenter', {
    extend: 'Ext.data.Model',

    requires: [
        'Ext.data.Field',
        'Ext.data.proxy.Rest',
        'Ext.data.reader.Json'
    ],

    fields: [
        {
            name: 'id'
        },
        {
            name: 'firstName'
        },
        {
            name: 'lastName'
        },
        {
            convert: function(v, rec) {
                return rec.get("firstName") + ' ' + rec.get('lastName')
            },
            name: 'firstLast'
        },
        {
            name: 'webSite'
        },
        {
            name: 'bio'
        },
        {
            name: 'imageUrl'
        },
        {
            name: 'imagePicture'
        }
    ],
    proxy: {
        type: 'rest',
        url: '/presenters/all.json',
        reader: {
            type: 'json',
            root: 'data'
        }
    }
});