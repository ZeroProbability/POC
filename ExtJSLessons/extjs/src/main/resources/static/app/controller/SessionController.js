Ext.define('SE.controller.SessionController', {
    extend: 'Ext.app.Controller',

    init: function() {
        this.control({
            "sessiongridpanel" : {
                itemdblclick: function() {
                    console.log('itemdblclick')
                }
            }
        });
    }
});
