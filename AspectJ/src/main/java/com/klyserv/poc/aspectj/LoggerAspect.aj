/**
 * Copyright 2014 (C) Klyserv Software Solutions
 *
 * Author     : Anbu
 * Created on : 4 Feb 2014
 */
package com.klyserv.poc.aspectj;

public aspect LoggerAspect {

    private final ILogger logger = new StdoutLogger();

    pointcut logGetName() : execution (public String getName());
    pointcut logSetName() : execution (public void setName(String));

    before() : logGetName() {
        logger.info("before getName");
    }

    after() returning() : logGetName() {
        logger.info("after getName");
    }

    before() :logSetName() {
        Object[] paramValues = thisJoinPoint.getArgs();
        logger.info("Name is being set to " + paramValues[0]);
    }

    after() returning() : logSetName() {
    }
}
