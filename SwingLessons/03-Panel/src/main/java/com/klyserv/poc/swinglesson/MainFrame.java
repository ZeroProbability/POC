package com.klyserv.poc.swinglesson;

import java.awt.BorderLayout;

import javax.swing.JFrame;

public class MainFrame extends JFrame {
	
	private static final long serialVersionUID = 1L;
	
	private TextPanel textPanel;
	private Toolbar toolbar;
	private FormPanel formPanel;

	public MainFrame() {
		super("MainFrame");
		
		textPanel=new TextPanel();
		toolbar=new Toolbar();
		formPanel=new FormPanel();
		
		BorderLayout layoutManager=new BorderLayout();
		setLayout(layoutManager);
		
		toolbar.setToolBarActionListener(new ToolbarActionListener() {
			
			@Override
			public void buttonClicked(String str) {
				textPanel.appendText(str+"\n");
			}
		});
		
		formPanel.setFormPanelListerner(new FormPanelListener() {
			@Override
			public void formAddButtonClicked(FormEvent e) {
				textPanel.appendText(e.getName()+"\n");
				textPanel.appendText(e.getOccupation()+"\n");
				textPanel.appendText(e.getAgeCategory()+"\n");
				textPanel.appendText(e.getEmploymentType()+"\n");
			}
		});
		
		add(toolbar,BorderLayout.NORTH);
		add(textPanel,BorderLayout.CENTER);
		add(formPanel, BorderLayout.WEST);
		
		setSize(600,400);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
	}

}
