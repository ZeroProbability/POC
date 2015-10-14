package com.klyserv.poc.spring4;

import com.klyserv.poc.spring4.config.AppConfig;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Created by anbu on 14/10/15.
 */
public class MainClass {

    public static void main(String[] args) {
        AnnotationConfigApplicationContext context=new AnnotationConfigApplicationContext();
        context.register(AppConfig.class);
        context.refresh();

        context.getBean(SecondService.class).someMethod();

    }
}
