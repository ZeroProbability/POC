package edu.college.cs.project;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.ArrayList;

public class smtpd {
	
	private final static StdoutLogger console=new StdoutLogger();

	public static void main(String[] args) {
		int port = 0;
		ArrayList<ServerThread> listOfThreads = new ArrayList<ServerThread>(); 
		if(args.length < 1) {  
			console.log(Logger.ERROR, "Need at least on command line argument");
			System.exit(1);
		}
		try {
			port = Integer.parseInt(args[0]);
		}
		catch(NumberFormatException ex) {
			console.log(Logger.ERROR, "First command-line argument must be an integer");
			System.exit(2);
		}
		ServerSocket server;
		Socket client;
		while(true) {
			try {
				server = new ServerSocket(port);
				break;
			} catch (IOException e) {			
				port++;
			}
		}
		console.log("SMTP server is now active listening on port number " + port + ".");
		try {
			server.setSoTimeout(5000);
		} 
		catch (SocketException e) {
			console.log(Logger.ERROR, "ServerSocket timeout setting failed: " + e);
		}
		while(true) {
			try {
				client = server.accept();
				//-- create new thread to serve new connection request
				console.log("New client from '" + client.getRemoteSocketAddress() + "' requested connection");
				ServerThread tempThread = new ServerThread(client);
				listOfThreads.add(tempThread);
				tempThread.start();
			} 
			catch (java.net.SocketTimeoutException e1) {
				/*
				for(ServerThread T : listOfThreads) {
					//-- Try this approach to implement iteration, it should throw an exception
				}
				*/
				for(int i=listOfThreads.size()-1; i>= 0; i--) {
					ServerThread termThread = listOfThreads.get(i);
					if(termThread.isTerminationFlag() == true) {
						try {
							termThread.join();
						} 
						catch (InterruptedException e2) {
							console.log("Joining of a thread failed: " + e2);
						}
						listOfThreads.remove(termThread);
						console.log("Thread had been successfully removed.");
					}
				}
			}
			catch (IOException e3) {
				console.log(Logger.ERROR, "Accept() method returned error: " + e3);
				//-- to add additional processing
			}			
		}

	}
}