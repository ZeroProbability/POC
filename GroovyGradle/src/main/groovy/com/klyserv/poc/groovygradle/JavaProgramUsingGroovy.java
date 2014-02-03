/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 3 Feb 2014
 */
package com.klyserv.poc.groovygradle;

public class JavaProgramUsingGroovy {

    public static void main(final String[] args) {
        HelloFromGroovy hfg=new HelloFromGroovy();
        System.out.println(hfg.getGreetings("java"));
    }

}
