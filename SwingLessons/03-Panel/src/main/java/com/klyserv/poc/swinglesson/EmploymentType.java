package com.klyserv.poc.swinglesson;

public class EmploymentType {
	
	private int id;
	
	public EmploymentType(int id, String description) {
		this.id=id;
		this.description=description;
	}
	
	@Override
	public String toString() {
		return description;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	private String description;

}
