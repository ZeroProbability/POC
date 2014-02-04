/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 4 Feb 2014
 */
package com.klyserv.poc.aspectj;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.io.Serializable;

public aspect PointAspect {
    /*
     * privately introduce a field into Point to hold the property
     * change support object.  `this' is a reference to a Point object.
     */
    private final PropertyChangeSupport Point.support = new PropertyChangeSupport(this);

    /*
     * Introduce the property change registration methods into Point.
     * also introduce implementation of the Serializable interface.
     */
    public void Point.addPropertyChangeListener(final PropertyChangeListener listener){
      support.addPropertyChangeListener(listener);
    }

    public void Point.addPropertyChangeListener(final String propertyName,
                                                final PropertyChangeListener listener){

      support.addPropertyChangeListener(propertyName, listener);
    }

    public void Point.removePropertyChangeListener(final String propertyName,
                                                   final PropertyChangeListener listener) {
      support.removePropertyChangeListener(propertyName, listener);
    }

    public void Point.removePropertyChangeListener(final PropertyChangeListener listener) {
      support.removePropertyChangeListener(listener);
    }

    public void Point.hasListeners(final String propertyName) {
      support.hasListeners(propertyName);
    }

    declare parents: Point implements Serializable;

    /**
     * Pointcut describing the set<property> methods on Point.
     * (uses a wildcard in the method name)
     */
    pointcut setter(Point p): execution( public void Point.set*(*) ) && target(p);

    /**
     * Advice to get the property change event fired when the
     * setters are called. It's around advice because you need
     * the old value of the property.
     */
    void around(final Point p): setter(p) {
          String propertyName =
        thisJoinPointStaticPart.getSignature().getName().substring("set".length());
          int oldX = p.getX();
          int oldY = p.getY();
          proceed(p);
          if (propertyName.equals("X")){
        firePropertyChange(p, propertyName, oldX, p.getX());
          } else {
        firePropertyChange(p, propertyName, oldY, p.getY());
          }
    }

    /*
     * Utility to fire the property change event.
     */
    void firePropertyChange(final Point p, final String property, final double oldval, final double newval) {
          p.support.firePropertyChange(property, new Double(oldval), new Double(newval));
    }
  }