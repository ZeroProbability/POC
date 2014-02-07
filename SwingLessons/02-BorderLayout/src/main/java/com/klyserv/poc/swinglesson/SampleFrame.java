package com.klyserv.poc.swinglesson;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextArea;

public class SampleFrame extends JFrame {
	
	private static final long serialVersionUID = 1L;

	public SampleFrame() {
		super("Hello sample frame");
		
		setSize(600,400);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// It is a good idea to have a layout manager manage the component layouts
		BorderLayout layoutManager=new BorderLayout();
		setLayout(layoutManager);
		
		// Create a button component and add it to frame
		JButton clickMeButton=new JButton("Click me");
		add(clickMeButton,BorderLayout.SOUTH);
		
		// Create a text area and add it to frame
		final JTextArea textArea=new JTextArea();
		add(textArea, BorderLayout.CENTER);
		
		// Now attach a even listener to the button to populate the text area
		clickMeButton.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				textArea.append("Hello there!!\n");   
				
			}
		});
	}
	
	public static void main(String[] args) {
		new SampleFrame();
	}

}