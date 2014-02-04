/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 4 Feb 2014
 */
package com.klyserv.poc.aspectj;

class Point {

    private static final long serialVersionUID = 1L;
    private int x = 0;
    private int y = 0;

    public int getX(){
        return x;
    }
    public int getY(){
        return y;
    }

     public void setX(final int newX) {
        this.x = newX;
    }

    public void setY(final int newY) {
        this.y = newY;
    }
}