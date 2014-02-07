package com.klyserv.poc.swinglesson;

import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.DefaultComboBoxModel;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.Border;

public class FormPanel extends JPanel {

	private static final long serialVersionUID = 1L;
	
	private JLabel nameLabel;
	private JLabel occupationLabel;
	private JLabel ageCategoryLabel;
	private JLabel employmentLabel;
	
	
	private JTextField nameField;
	private JTextField occupationField;
	private JList<AgeCategory> ageList;
	private JComboBox<EmploymentType> employmentCombo;
	
	private JButton addButton;

	private FormPanelListener panelListener;
	
	public FormPanel() {
		Dimension dim=getPreferredSize();
		dim.width=350;
		setPreferredSize(dim);
		DefaultListModel<AgeCategory> dlm=new DefaultListModel<>();
		dlm.addElement(new AgeCategory(1, "Under 18"));
		dlm.addElement(new AgeCategory(2, "Over 18 Under 65"));
		dlm.addElement(new AgeCategory(3, "Over 65"));
		
		nameLabel=new JLabel("Name :");
		occupationLabel=new JLabel("Occupation :");
		ageCategoryLabel=new JLabel("Age :");
		employmentLabel=new JLabel("Employment type :");
		
		DefaultComboBoxModel<EmploymentType> dcbm=new DefaultComboBoxModel<>();
		dcbm.addElement(new EmploymentType(1,"employed"));
		dcbm.addElement(new EmploymentType(2,"self employed"));
		dcbm.addElement(new EmploymentType(3,"un employed"));

		nameField=new JTextField(10);
		occupationField=new JTextField(10);
		ageList=new JList<>(dlm);
		employmentCombo=new JComboBox<>(dcbm);
		addButton=new JButton("Add");
		
		ageList.setPreferredSize(new Dimension(135, 60));
		ageList.setBorder(BorderFactory.createEtchedBorder());
		
		employmentCombo.setMaximumSize(employmentCombo.getPreferredSize());
		
		addButton.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				String name=nameField.getText();
				String occupation=occupationField.getText();
				AgeCategory ageCategory=ageList.getSelectedValue();
				EmploymentType employmentType=employmentCombo.getItemAt(employmentCombo.getSelectedIndex());
				
				FormEvent fe=new FormEvent(this, name, occupation, ageCategory, employmentType);
				if(panelListener!=null) {
					panelListener.formAddButtonClicked(fe);
				}
			}
		});
		
		Border innerBorder=BorderFactory.createTitledBorder("Add Person");
		Border outerBorder=BorderFactory.createEmptyBorder(0, 0, 0, 5);
		setBorder(BorderFactory.createCompoundBorder(outerBorder, innerBorder));
		
		setLayout(new GridBagLayout());
		
		doLayoutInternal();
	}
	
	private void doLayoutInternal() {
		GridBagConstraints gc=new GridBagConstraints();
		
		// -------------- First row
		gc.gridx=0;
		gc.gridy=0;
		
		gc.weightx=0.1;
		gc.weighty=0.1;
		
		gc.fill=GridBagConstraints.NONE;
		gc.anchor=GridBagConstraints.EAST;
		gc.insets=new Insets(0,0,0,5);
		add(nameLabel,gc);
		
		gc.gridx=1;
		gc.gridy=0;
		gc.anchor=GridBagConstraints.WEST;
		gc.insets=new Insets(0,0,0,0);
		add(nameField,gc);
		
		// -------------- Second row
		gc.gridx=0;
		gc.gridy=1;
		gc.anchor=GridBagConstraints.EAST;
		gc.insets=new Insets(0,0,0,5);
		add(occupationLabel,gc);
		
		gc.gridx=1;
		gc.gridy=1;
		gc.anchor=GridBagConstraints.WEST;
		gc.insets=new Insets(0,0,0,0);
		add(occupationField,gc);
		
		// -------------- third row
		gc.gridx=0;
		gc.gridy=2;
		gc.anchor=GridBagConstraints.EAST;
		gc.insets=new Insets(0,0,0,5);
		add(ageCategoryLabel,gc);
		
		gc.gridx=1;
		gc.gridy=2;
		gc.anchor=GridBagConstraints.WEST;
		gc.insets=new Insets(0,0,0,0);
		add(ageList,gc);
		

		// -------------- fourth row
		gc.gridx=0;
		gc.gridy=3;
		gc.anchor=GridBagConstraints.EAST;
		gc.insets=new Insets(0,0,0,5);
		add(employmentLabel,gc);
		
		gc.gridx=1;
		gc.gridy=3;
		gc.anchor=GridBagConstraints.WEST;
		gc.insets=new Insets(0,0,0,0);
		add(employmentCombo,gc);
		

		// -------------- Fifth row
		
		gc.gridx=1;
		gc.gridy=4;
		
		gc.weightx=1;
		gc.weighty=1;

		gc.anchor=GridBagConstraints.FIRST_LINE_START;
		add(addButton,gc);
	}
	
	public void setFormPanelListerner(FormPanelListener panelListener) {
		this.panelListener=panelListener;
	}

}
