package com.klyserv.poc.swinglesson;

import java.awt.BorderLayout;

import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class TextPanel extends JPanel {

	private static final long serialVersionUID = 1L;
	
	private JTextArea textArea;
	
	public TextPanel() {
		
		textArea=new JTextArea();
		
		setLayout(new BorderLayout());
		add(new JScrollPane(textArea), BorderLayout.CENTER); // <== wrap text area with scroll bars 
	}

	public void appendText(String str) {
		textArea.append(str);
	}

}
