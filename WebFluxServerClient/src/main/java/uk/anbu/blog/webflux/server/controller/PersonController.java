package uk.anbu.blog.webflux.server.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;
import uk.anbu.blog.webflux.server.data.Person;
import uk.anbu.blog.webflux.server.data.PersonDataGenerator;

@RestController
@AllArgsConstructor
public class PersonController {
    private final PersonDataGenerator personDataGenerator;

    @GetMapping("/persons")
    Flux<Person> list() {
        return Flux.fromStream(personDataGenerator.personStream());
    }

    @GetMapping("/person/{id}")
    Mono<Person> findById(@PathVariable("id") int id) {
        return Mono.justOrEmpty(personDataGenerator.findPerson(id));
    }
}
