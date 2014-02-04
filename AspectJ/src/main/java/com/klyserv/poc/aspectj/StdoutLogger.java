/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 4 Feb 2014
 */
package com.klyserv.poc.aspectj;

public class StdoutLogger implements ILogger {

    @Override
    public void info(final String msg){
        System.out.println(msg);
    }

    @Override
    public void error(final String msg){
        System.err.println(msg);
    }
}
