package com.klyserv.poc.swinglesson;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;

public class Toolbar extends JPanel implements ActionListener {

	private static final long serialVersionUID = 1L;
	
	private JButton helloButton;
	private JButton byeButton;
	
	private ToolbarActionListener tal;
	
	public Toolbar() {
		helloButton=new JButton("Hello");
		byeButton=new JButton("Bye");
		
		setLayout(new FlowLayout(FlowLayout.LEFT));
		
		add(helloButton);
		add(byeButton);
		
		helloButton.addActionListener(this);
		byeButton.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		JButton button=(JButton) e.getSource();
		if(tal!=null) {
			tal.buttonClicked(button.getText());
		}
	}

	public void setToolBarActionListener(ToolbarActionListener tal) {
		this.tal = tal;
	}
	

}