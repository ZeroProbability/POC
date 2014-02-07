package com.klyserv.poc.swinglesson;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class HelloSwing {
	
	public static void main(String[] args) {
		
		SwingUtilities.invokeLater(new Runnable() { // Executing through this static method is recommended by Sun/Oracle
			
			@Override
			public void run() {
				JFrame helloFrame=new JFrame("Hello Swing");
				
				helloFrame.setVisible(true); // Without this the frame will be not displayed and the program will end
				helloFrame.setSize(600,400); // Without this the size of frame is set to 0,0. Nothing will be visible
				helloFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Without the program won't exit on closing the frame
			}
		});
	}

}
