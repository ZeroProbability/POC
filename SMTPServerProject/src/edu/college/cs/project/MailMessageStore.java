package edu.college.cs.project;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;
import java.util.List;

public class MailMessageStore implements Serializable {
	
	private static final long serialVersionUID = -7469777139971624935L;

	private List<MailMessage> store;
	
	private String sessionId;
	
	public MailMessageStore(String clientHost) {
		store=new ArrayList<MailMessage>();
		sessionId="ID:"+clientHost+"-"+new Date().getTime();
	}
	
	public void addMessage(MailMessage mailMessage) {
		store.add(mailMessage);
	}
	
	public List<MailMessage> readMessages() {
		return Collections.unmodifiableList(store);
	}
	
	public void dumpMessagesTo(Logger l) {
		l.log("Session ID:"+sessionId);
		for(MailMessage msg:store) {
			msg.log(l);
		}
		l.log("----- end of messages ------");
	}
	
}
