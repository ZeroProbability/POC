package edu.college.cs.project;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;

import edu.college.cs.project.MailMessage.MessageType;

/*
 * Reads messages from mail repository file and relays it to other SMTP hosts 
 */
public class msgProvider {
	
	private final static StdoutLogger console=new StdoutLogger();
	
	private int port=0;
	
	public msgProvider() {
	}
	
	public static void main(String[] args) {
		msgProvider md=new msgProvider();
		ArrayList<ServerThread> listOfThreads = new ArrayList<ServerThread>(); 
		if(args.length < 1) {  
			console.log(Logger.ERROR, "Need at least on command line argument");
			System.exit(1);
		}
		try {
			md.port = Integer.parseInt(args[0]);
		}
		catch(NumberFormatException ex) {
			console.log(Logger.ERROR, "First command-line argument must be an integer");
			System.exit(2);
		}

		md.sendMessages();
	}
	
	private void writeSmtpCommand(PrintWriter out, BufferedReader in, String command) {
		out.println(command);
		try {
			String str=in.readLine();
			// TODO: if input does not start with 250.. there is an error
		} catch (IOException e) {
			console.log(Logger.ERROR, "Error reading input from SMTP server. Exception "+e);
		}
	}

	private void writeSmtpMailData(PrintWriter out, BufferedReader in, String data) {
		out.println("DATA");
		out.println(data);
		out.println(".");
		try {
			String str=in.readLine();
			// TODO: if input does not start with 250.. there is an error
		} catch (IOException e) {
			console.log(Logger.ERROR, "Error reading input from SMTP server. Exception "+e);
		}
	}
	private void sendMessages() {
		MessageRepository repo=MessageRepository.readFromFile(MessageRepository.REPO_FILE_NAME); 
		if(repo==null) repo=new MessageRepository();
		
		for(String destination:repo.findDestinations()) {
			Socket socket=null;
			PrintWriter out=null;
			BufferedReader in=null;
			try {
				socket = new Socket(destination, port);
				out = new PrintWriter(socket.getOutputStream(), true);
				in = new BufferedReader(new InputStreamReader(
						socket.getInputStream()));
			} catch (Exception e) {
				console.log(Logger.ERROR, "Error while trying to open sockets. Exception:"+e);
			}
			
			writeSmtpCommand(out, in, "HELO");
			for(MailMessage mm:repo.findMessagesForDestination(destination)) {
				if(mm.getMessageType()==MessageType.LOCAL_MESSAGE) continue; // Don't have to send local messages anywhere
				writeSmtpCommand(out, in, "MAIL FROM:"+mm.getMailFrom());
				for(String rcptTo:mm.getRcptTo()) {
					if(MailMessage.getHostNameFromRcpt(rcptTo).equalsIgnoreCase(destination)){
						writeSmtpCommand(out, in, "RCPT TO:"+mm.getRcptTo());
					}
				}
				writeSmtpMailData(out, in, mm.getData());
			}
			writeSmtpCommand(out, in, "QUIT");
			
		}
	}
}
