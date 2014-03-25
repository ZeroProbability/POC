package edu.college.cs.project;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class MessageRepository implements Serializable {
	
	private static final long serialVersionUID = -7469777139971624935L;

	private final static StdoutLogger console=new StdoutLogger();

	public static final String REPO_FILE_NAME="messagerepo.dat";

	private Map<String, List<MailMessage>> repository=new HashMap<String, List<MailMessage>>();
	
	public void addMessages(MailMessageStore messageStore) {
		List<MailMessage> mailList=messageStore.readMessages();
		for(MailMessage mm:mailList) {
			Set<String> uniqueHostNames=new HashSet<String>();
			for(String recipient:mm.getRcptTo()) {
				String rcptHost=MailMessage.getHostNameFromRcpt(recipient);
				if(uniqueHostNames.contains(rcptHost)) continue;
				
				List<MailMessage> sendList=null; 
				if(repository.containsKey(rcptHost)) {
					sendList=repository.get(rcptHost); 
				} else {
					sendList=new ArrayList<MailMessage>(); 
				}
				sendList.add(mm);
				repository.put(rcptHost, sendList);
				uniqueHostNames.add(rcptHost);
			}
		}
	}
	
	public static MessageRepository readFromFile(String fileName) {
		FileInputStream fis;
		MessageRepository m=null;
		try {
			fis=new FileInputStream(fileName);
			ObjectInputStream ois=new ObjectInputStream(fis);
			m=(MessageRepository)ois.readObject();
			ois.close();
			fis.close();
		} catch(Exception e) {
			console.log(Logger.ERROR, "Exception while reading message store "+e.getMessage());
		}
		return m;
	}
	
	public synchronized void saveToFile(String fileName) {
		FileOutputStream fos;
		try {
			fos = new FileOutputStream(fileName);
			ObjectOutputStream oos=new ObjectOutputStream(fos);
			oos.writeObject(this);
			oos.close();
			fos.close();
		} catch (Exception e) {
			console.log(Logger.ERROR, "Exception while saving message store "+e.getMessage());
		}
	}
	
	public Set<String> findDestinations() {
		return Collections.unmodifiableSet(repository.keySet());
	}

	public List<MailMessage> findMessagesForDestination(String destination) {
		return Collections.unmodifiableList(repository.get(destination));
	}

}
