package uk.anbu.blog.webflux.server;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;

import java.util.Collections;

@SpringBootApplication(scanBasePackages = {"uk.anbu.blog.webflux.server"})
public class WebfluxApplication {

    public static void main(String[] args) {
        new SpringApplicationBuilder(WebfluxApplication.class)
                .properties(Collections.singletonMap("server.port", "53797"))
                .run(args);
    }

}
