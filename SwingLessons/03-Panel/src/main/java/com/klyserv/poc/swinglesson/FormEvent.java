package com.klyserv.poc.swinglesson;

import java.util.EventObject;

public class FormEvent extends EventObject {
	
	private String name;
	
	private String occupation;
	
	private AgeCategory ageCategory;
	
	private EmploymentType employmentType;

	public FormEvent(Object source, String name, String occupation, AgeCategory ageCategory, EmploymentType employmentType) {
		super(source);
		this.name=name;
		this.occupation=occupation;
		this.ageCategory=ageCategory;
		this.setEmploymentType(employmentType);
	}

	@Override
	public String toString() {
		return "FormEvent [name=" + name + ", occupation=" + occupation + "]";
	}

	public String getOccupation() {
		return occupation;
	}

	public void setOccupation(String occupation) {
		this.occupation = occupation;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public AgeCategory getAgeCategory() {
		return ageCategory;
	}

	public void setAgeCategory(AgeCategory ageCategory) {
		this.ageCategory = ageCategory;
	}

	public EmploymentType getEmploymentType() {
		return employmentType;
	}

	public void setEmploymentType(EmploymentType employmentType) {
		this.employmentType = employmentType;
	}

	private static final long serialVersionUID = 1L;

}
