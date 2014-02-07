package com.klyserv.poc.swinglesson;

public class AgeCategory {
	
	@Override
	public String toString() {
		return description;
	}

	private String description;
	private int id;

	public AgeCategory(int id, String description) {
		this.setId(id);
		this.setDescription(description);
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

}
