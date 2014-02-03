/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 3 Feb 2014
 */
package com.klyserv.poc.groovygradle

import com.sun.org.apache.bcel.internal.generic.NEW;

class HelloFromGroovy {

    String getGreetings(String string) {
        return "Hello from groovy to "+string;
    }

    static main(args) {
        HelloFromJava hfj=new HelloFromJava()

        println hfj.getGreetings("groovy")
    }

}
