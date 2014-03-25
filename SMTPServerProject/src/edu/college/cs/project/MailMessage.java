package edu.college.cs.project;

import java.io.Serializable;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Arrays;
import java.util.List;

public class MailMessage implements Serializable {
	
	private static final long serialVersionUID = -7193462083628137686L;

	private final static StdoutLogger console=new StdoutLogger();

	public enum MessageType {
		LOCAL_MESSAGE,
		FORWARDING_MESSAGE,
		BOTH_WAYS
	}
	
	private String mailFrom;
	
	private List<String> rcptTo;
	
	private String data;
	
	private MessageType messageType;
	
	public static String getHostNameFromRcpt(String rcptString) {
		int hostStart=rcptString.indexOf('@');
		String hostname="";
		if(hostStart>=0) hostname=rcptString.substring(hostStart+1);
		if(hostname.endsWith(">")) hostname=hostname.substring(0, hostname.length()-1);
		return hostname;
	}
	
	public MailMessage(String data, String mailFrom, String... rcptTo) {
		this.data=data;
		this.mailFrom=mailFrom;
		this.rcptTo=Arrays.asList(rcptTo);
		
		InetAddress localAddress=null;
		boolean containsLocal=false;
		boolean containsForward=false;
		
		for(String recepitant:rcptTo) {
			try {
				localAddress=InetAddress.getLocalHost();
			} catch (UnknownHostException e) {
				console.log(Logger.ERROR, "Error finding localhost name"+e.getMessage());
			}
			
			String hostname=getHostNameFromRcpt(recepitant);
			if (localAddress.getHostName().equals(hostname)
					|| localAddress.getHostAddress().equals(hostname)) {
				containsLocal=true;
			} else {
				containsForward=true;
			}
		}
		if(containsForward && containsLocal) { 
			setMessageType(MessageType.BOTH_WAYS);
		} else if(containsForward) {
			setMessageType(MessageType.FORWARDING_MESSAGE);
		} else {
			setMessageType(MessageType.LOCAL_MESSAGE);
		}
		
		
	}
	
	public String getData() {
		return data;
	}

	public List<String> getRcptTo() {
		return rcptTo;
	}

	public String getMailFrom() {
		return mailFrom;
	}

	public void log(Logger l) {
		l.log("FROM:"+mailFrom);
		l.log("TO  :"+rcptTo);
		l.log("Data:\n"+data+"");
	}

	public MessageType getMessageType() {
		return messageType;
	}

	private void setMessageType(MessageType messageType) {
		this.messageType = messageType;
	}

}