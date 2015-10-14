package com.klyserv.poc.spring4.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

/**
 * Created by anbu on 14/10/15.
 */
@Configuration
@ComponentScan("com.klyserv.poc.spring4")
public class AppConfig {

    @Bean(name="firstService")
    public FirstService firstService() {
        return new FirstService();
    }

}
