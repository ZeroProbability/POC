package uk.anbu.blog.webflux.server.controller;

import org.springframework.web.bind.annotation.RestController;
import uk.anbu.blog.webflux.server.data.PersonDataGenerator;

@RestController
public class PersonController {
    private final PersonDataGenerator personDataGenerator;
}
