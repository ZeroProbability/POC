/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 4 Feb 2014
 */
package com.klyserv.poc.aspectj;

public class Main {
    public static void main(final String[] args) throws InterruptedException {
        Book b=new Book();
        b.setName("some name");
        b.getName();

        // ----

        Point p=new Point();
        p.setX(10);p.setY(20);
        System.out.printf("p(%d,%d)\n", p.getX(), p.getY());

        Thread.sleep(1000);
    }
}
