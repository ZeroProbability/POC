package com.klyserv.learn.extjs;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.util.Collection;

@SpringBootApplication
public class ExtjsApplication {

	public static void main(String[] args) {
		SpringApplication.run(ExtjsApplication.class, args);
	}

    @Bean
    CommandLineRunner runner(SessionsRepository sr) {
        return args -> {
            sr.save(Session.builder().title("C++").level(3).approved(true).build());
            sr.save(Session.builder().title("C language").level(2).approved(true).build());
            sr.save(Session.builder().title("golang").level(1).approved(false).build());
            sr.save(Session.builder().title("javascript").level(2).approved(true).build());
            sr.findAll().forEach(System.out::println);
        };
    }
}

@RestController
class SessionController {

    @Autowired
    private SessionsRepository sessionsRepository;

    @RequestMapping("/sessions/all.json")
    public Collection<Session> allSessions() {
        return sessionsRepository.findAll();
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
    @Column(name="TITLE") private String title;
    @Column(name="APPROVED") private Boolean approved;
    @Column(name="LEVEL") private Integer level;
}