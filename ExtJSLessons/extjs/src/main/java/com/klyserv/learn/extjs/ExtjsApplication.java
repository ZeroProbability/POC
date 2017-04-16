package com.klyserv.learn.extjs;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RestController;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.util.Arrays;

@SpringBootApplication
public class ExtjsApplication {

	public static void main(String[] args) {
		SpringApplication.run(ExtjsApplication.class, args);
	}

    @Bean
    CommandLineRunner runner(SessionsRepository sr) {
        return args -> {
            Arrays.asList("C++,C lang,golang,javascript".split(","))
                    .forEach(n -> sr.save(Session.builder().session(n).build()));
            sr.findAll().forEach(System.out::println);
        };
    }
}

@RepositoryRestResource
interface SessionsRepository extends JpaRepository<Session, Long> {
}

@Entity
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
class Session {
    @GeneratedValue @Id private Long id;
    @Column(name="SESSION") private String session;
    @Column(name="LEVEL") private Integer level;
}