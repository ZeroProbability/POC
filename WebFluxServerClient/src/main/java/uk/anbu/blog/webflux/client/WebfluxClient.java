package uk.anbu.blog.webflux.client;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.http.MediaType;
import org.springframework.web.reactive.function.client.WebClient;
import uk.anbu.blog.webflux.server.data.Person;

@SpringBootApplication(scanBasePackages = {"uk.anbu.blog.webflux.client"})
@Slf4j
public class WebfluxClient implements CommandLineRunner {
    @Bean
    WebClient getWebClient() {
        return WebClient.create("http://localhost:53797");
    }

//    @Bean
//    CommandLineRunner demo(WebClient client) {
//        return args -> client.get()
//                .uri("/persons")
//                .accept(MediaType.TEXT_EVENT_STREAM)
//                .retrieve()
//                .bodyToFlux(Person.class)
//                .map(String::valueOf)
//                .subscribe(log::info);
//    }
//
    public static void main(String[] args) {
        new SpringApplicationBuilder(WebfluxClient.class)
                .run(args);
    }

    @Override
    public void run(String... args) throws Exception {

    }
}
