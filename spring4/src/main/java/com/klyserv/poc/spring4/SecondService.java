package com.klyserv.poc.spring4;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Created by anbu on 14/10/15.
 */
@Service
public class SecondService {
    private final FirstService fs;

    @Autowired
    public SecondService(FirstService fs) {
        this.fs=fs;
    }

    public void someMethod() {
        System.out.println("Some method was called");
        this.fs.myMethod();
    }
}
