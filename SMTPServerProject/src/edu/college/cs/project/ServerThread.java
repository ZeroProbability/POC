package edu.college.cs.project;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.List;

public class ServerThread extends Thread {
	private BufferedReader br;
	private PrintWriter pw;;
	private Socket client;
	public String hostName;
	private boolean TerminationFlag;
	
	private List<String> gRcptTo=null;
	private String gMailFrom=null;
	private class Stat {
		int totalMessage=0;
		int localMessage=0;
		int forwardMessage=0;
		int bothWays=0;
		
		public void reset() {
			totalMessage=localMessage=forwardMessage=bothWays=0;
		}
		
		public void addMessageType(MailMessage msg) {
			totalMessage++;
			switch(msg.getMessageType()) {
				case LOCAL_MESSAGE:localMessage++;break;
				case BOTH_WAYS:bothWays++;break;
				case FORWARDING_MESSAGE:forwardMessage++;break;
				default: ;// nothing
			}
		}
		
		@Override
		public String toString() {
			return "" + totalMessage + " message(s) received, " + localMessage
					+ " message(s) for local delivery, " + forwardMessage
					+ " message(s) for forwarding, " + bothWays
					+ " message(s) marked both ways.";
		}
	};
	private Stat stat=new Stat();
	
	private enum SessionState {
		WAITING_FOR_HELLO,
		WAITING_FOR_MAIL_FROM,
		WAITING_FOR_RCPT_TO,
		WAITING_FOR_DATA
	}
	
	private SessionState currentSessionState=SessionState.WAITING_FOR_HELLO;
	
	private MailMessageStore messageStore=null; 
	
	private final static StdoutLogger console=new StdoutLogger();

	public boolean isTerminationFlag() {
		return TerminationFlag;
	}

	public ServerThread(Socket client) {
		this.client = client;
		this.TerminationFlag = false;
	}

	public void run() {
		String command = null;
		String text = null;
		try {
			hostName = InetAddress.getLocalHost().getHostName();
			//String destName = client.getInetAddress().getHostName();
			//int destPort = client.getPort();
			br = new BufferedReader(new InputStreamReader(
					client.getInputStream()));
			pw = new PrintWriter(client.getOutputStream(), true);
			pw.println("220 : Service ready! You are connected with the SMTP server.");
		} catch (UnknownHostException ex) {
			console.log("UnknownHostException occurred.");
		} catch (IOException e) {
			pw.println("421 : Service not available, closing transmission channel");
			console.log(Logger.ERROR, "UnknownHostException occurred."+e.getMessage());
		}
		// SmtpMessage msg = new SmtpMessage();

		while (true) {
			try {
				command = br.readLine();
			} catch (IOException e) {
				console.log(Logger.ERROR, "Readline() failed");
				break;
				// -- to add additional processing
			}
			if (command.equalsIgnoreCase("HELP")) {
				doHelp();
			} else if (command.equalsIgnoreCase("HELO")) {
				doHello();
			} else if (command.toUpperCase().startsWith("MAIL FROM:")) {
				doMailFrom(command);
			} else if (command.toUpperCase().startsWith("RCPT TO:")) {
				doRcptTo(command);
			} else if (command.equalsIgnoreCase("DATA")) {
				pw.println("354:Start mail input; end with <CRLF>.<CRLF>! Enter the text and complete it with period sign (.)");
				StringBuffer dataString=new StringBuffer();
				try {
					text = br.readLine();
					while(!text.equals(".")) {
						dataString.append(text+"\n");
						text = br.readLine();
					};
					pw.println("250: Your data has been sent successfully recieved");
				} catch (IOException ioex) {
					console.log(Logger.ERROR, "IO Exception occurred");
				}
				doData(dataString.toString());

			} else if (command.equalsIgnoreCase("quit")) {
				doquit();
				break;
			} else {
				pw.println("Error: " + command
						+ "! Wrong command! Please enter a correct one.");
				console.log(Logger.ERROR, "Incorrect command. Received '"+command+"'");
			}
		}
	}
	
	private void doquit() {
		try {
			br.close();
			pw.close();
			client.close();
			pw.println("221: Service closing transmission channel! Terminating the connection");
			console.log("client side quit requested. Connection has been closed.");
			
			Logger messageLogger=new FileLogger("messagelog.txt");
			messageStore.dumpMessagesTo(messageLogger);
			
			String repofilename=MessageRepository.REPO_FILE_NAME;
			MessageRepository repo=MessageRepository.readFromFile(repofilename);
			if(repo==null) repo=new MessageRepository();
			repo.addMessages(messageStore);
			repo.saveToFile(repofilename);
			
			resetFields();
			console.log(stat.toString());
			stat.reset();
		} catch (IOException e) {
			console.log(Logger.ERROR,"Clean up procedure failed");
		}
		currentSessionState=SessionState.WAITING_FOR_HELLO;
		this.TerminationFlag = true;
	}

	private void resetFields() {
		gMailFrom=null;
		gRcptTo=null;
	}

	private void doData(String text) {
		if (currentSessionState != SessionState.WAITING_FOR_DATA) {
			pw.println("503 bad sequence of commands");
			return;
		}
		if(gMailFrom==null||gRcptTo==null) {
			console.log("Incomplete mail message, message discarded");
			resetFields();
			return;
		}
		String[] tempRcptList=new String[gRcptTo.size()];
		gRcptTo.toArray(tempRcptList);
		MailMessage m=new MailMessage(text, gMailFrom, tempRcptList);
		if(messageStore==null) {
			String h=client.getInetAddress().getHostName()+":"+client.getPort();
			messageStore=new MailMessageStore(h);
		}
		messageStore.addMessage(m);
		currentSessionState=SessionState.WAITING_FOR_MAIL_FROM;
		stat.addMessageType(m);
		
		resetFields();
	}

	private void doRcptTo(String command) {
		if (currentSessionState == SessionState.WAITING_FOR_RCPT_TO
				|| currentSessionState == SessionState.WAITING_FOR_DATA) {
			// nothing
		} else {
			pw.println("503 bad sequence of commands");
			return;
		}
		command=command.substring("RCPT TO:".length());
		if(gRcptTo==null) {
			gRcptTo=new ArrayList<String>();
		}
		gRcptTo.add(command);
		pw.println("250: Requested mail action okay, completed! Recipients Recieved");
		currentSessionState=SessionState.WAITING_FOR_DATA;
	}

	private void doMailFrom(String command) {
		if(currentSessionState!=SessionState.WAITING_FOR_MAIL_FROM) {
			pw.println("503 bad sequence of commands");
			return;
		}
		command=command.substring("MAIL FROM:".length());
		gMailFrom=command;
		pw.println("250: Requested mail action okay, completed! Received the Mail");
		currentSessionState=SessionState.WAITING_FOR_RCPT_TO;
	}

	private void doHello() {
		if(currentSessionState!=SessionState.WAITING_FOR_HELLO) {
			pw.println("503 bad sequence of commands");
			return;
		}
		messageStore=new MailMessageStore(hostName);
		pw.println("250: Requested mail action okay, completed! Hello! Mr. "
				+ hostName);
		currentSessionState=SessionState.WAITING_FOR_MAIL_FROM;
	}

	private void doHelp() {
		pw.println("Known commands HELO, MAIL, RCPT, DATA and QUIT. Current state:"+currentSessionState);
		pw.println("250: Requested mail action okay, completed!");
	}
}
