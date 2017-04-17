Ext.define("SE.view.SessionForm", {
    extend: 'Ext.window.Window',
    alias: 'widget.sessionform',
    padding: 5,
    width: 600,
    title: 'Edit Sessions',
    model: true,
    items: [
        {
            xtype: 'form',
            bodyPadding: 10,
            title: "",
            defaults: {
                labelWidth: 90,
                margin: '0 0 10 0',
                anchor: '90%'
            },
            items: [
                { xtype: 'textfield', name: 'title', fieldLabel: 'Title', allowBlank: false },
                { xtype: 'checkboxfield', name: 'approved', fieldLabel: 'Approved'}
            ]
        },
        {
            xtype: 'container',
            padding: '10 10 10 10',
            layout: {
                type: 'hbox',
                align: 'middle',
                pack: 'center',
            },
            items: [
                {
                    xtype: 'button',
                    text: 'Save',
                    formBind: true, // <== Disables the button if the form is invalid. Hmm! Doesn't appear to work
                    margin: '5 5 5 5',
                    handler: function(button) {
                        var form = button.up('window').down('form');
                        form.updateRecord();
                        button.up('window').destroy();
                    }
                }, {
                    xtype: 'button',
                    text: 'Cancel',
                    margin: '5 5 5 5',
                    handler: function(button) {
                        button.up('window').destroy();
                    }
                }
            ]
        }
    ]
});
