package uk.anbu.blog.webflux.server.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.RestController;
import uk.anbu.blog.webflux.server.data.PersonDataGenerator;

@RestController
@AllArgsConstructor
public class PersonController {
    private final PersonDataGenerator personDataGenerator;
}
