# Aspectj POC

## Requirements 

* JDK 1.8
* gradle

## To run the project use 

Launch the application using

    gradle tomcatRun

Then from browser try to open this [page](http://localhost:8080/AspectJ/bookServlet)

## Issues

   The last time I tried this project with jdk 1.8, I was getting `javax.servlet.ServletException: Class com.klyserv.poc.aspectj.servlet.BookServlet is not a Servlet`
