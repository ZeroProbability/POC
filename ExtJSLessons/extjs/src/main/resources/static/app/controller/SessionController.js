Ext.define('SE.controller.SessionController', {
    extend: 'Ext.app.Controller',

    init: function() {
        this.control({
            "sessiongridpanel" : {
                itemdblclick: function(gridpanel, record, item, index, e) {

                    var formWindow = Ext.create('SE.view.SessionForm');
                    var form = formWindow.down('form');     // <== using xtype in 'down'
                    form.loadRecord(record);
                    formWindow.show();
                }
            }
        });
    }
});
