package uk.anbu.blog.webflux.server.data;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Person {
    private int id;
    private String firstName;
    private String lastName;
}
