# EXTJS notes

## Overview

### Singleton

The "Ext" object is a Singleton. This is an example of how you could create your own Singleton.

    (function() {
         if (typeof MyExt === 'undefined') {
             this.MyExt = {
                  add: function(a, b) {
                      return a+b;
                  }
             };
         }
    })();

The above pattern is often referred to as IIFE (Immediately invoked function expression)

### Defining a class

    Ext.define("MyApp.Session", {
        config: {    /* A config object */
           title: '',
           description: '',
           level: 'beginner'
        },

        applyTitle: function(title) { /* A sample method */
           if (title === undefined) {
               alert('title undefined');
           }
           return title;
        },
        
        constructor: function(config) { /* The object's constructor */
           this.initConfig(config);
        }
    });

    var session = Ext.create("MyApp.Session", {
    });

    session.setTitle('Extjs session');

### What is a Component

* It is a JavaScript Object 
* Visual Classes all inherit from Component in ExtJs
* Components have Size and Position
* Components can render HTML
* Components can render HTML Using a template
* Components can enable/disable, hide/show or change size 
* Components can listen for Events
* Components have a life cycle

### Setting up a base application

    var myComponent = Ext.create('Ext.Component', {
        html: 'My first Extjs application'
    });

    Ext.application({
        name: 'MyApp',
        launch: function() {
            Ext.create('Ext.container.Viewport', {
                items: [
                    myComponent
                ]
            });
        }
    });

    // --------------------------------------
    /* That is same as instiating component inline */

    Ext.application({
        name: 'MyApp',
        launch: function() {
            Ext.create('Ext.container.Viewport', {
                items: [
                    {
                         xtype: 'component', // This is the default. So, optional
                         html: 'My first Extjs application',
                         padding: 20
                    }
                ]
            });
        }
    });

### Component lifecycle

* Components always start with initialization
* Sometimes they are rendered. But this could be skipped based on configuration.
* Components are always destroyed.

## Layout Management

### Definition 

From Wikipedia, layout managers are software components uesd in widget toolkits which have the ability to lay out widgets by their relative positions without using distance units.

### Types of layout managers.


