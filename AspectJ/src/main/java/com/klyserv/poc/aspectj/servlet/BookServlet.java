package com.klyserv.poc.aspectj.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.klyserv.poc.aspectj.Book;

/**
 * Servlet implementation class BookServlet
 */
public class BookServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
        Book b=new Book();
        b.setName("some name");
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<body>");
        out.println("<h1>"+b.getName()+"</h1>");
        out.println("</body>");
        out.println("</html>");
    }


}
