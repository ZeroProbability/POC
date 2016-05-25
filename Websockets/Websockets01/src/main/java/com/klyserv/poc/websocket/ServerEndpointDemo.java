package com.klyserv.poc.websocket;

import javax.websocket.OnClose;
import javax.websocket.OnError;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.server.ServerEndpoint;

/**
 * Created by anbu on 12/05/15.
 */
@ServerEndpoint("/serverendpointdemo")
public class ServerEndpointDemo {
    @OnOpen
    public void handleOpen() {
        System.out.println("Client is now connected");
    }

    @OnMessage
    public String handleMessage(String message) {
        System.out.println("received from client: "+message);
        return("Server: "+message);
    }

    @OnClose
    public void handleClose() {
        System.out.println("Client is now closed");
    }

    @OnError
    public void handleError(Throwable t) {
        t.printStackTrace();
    }
}
