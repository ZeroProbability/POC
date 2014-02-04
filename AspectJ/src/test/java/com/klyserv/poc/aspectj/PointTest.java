/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 4 Feb 2014
 */
package com.klyserv.poc.aspectj;

import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;

import org.junit.Before;
import org.junit.Test;
import static org.mockito.Mockito.*;

public class PointTest {

    //class under test
    private Point cut;

    @Before
    public void setup(){
        cut = new Point();
    }

    @Test
    public void testPropertyChangeEventFired(){
        PropertyChangeListener changeListenerMock =
                   mock(PropertyChangeListener.class);
        cut.addPropertyChangeListener(changeListenerMock);
        cut.setX(1);
        verify(changeListenerMock,times(1))
                   .propertyChange((PropertyChangeEvent) anyObject());
    }
}