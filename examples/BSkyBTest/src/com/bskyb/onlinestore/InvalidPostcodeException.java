package com.bskyb.onlinestore;

public class InvalidPostcodeException extends Exception {

	private static final long serialVersionUID = 3871030175274483001L;
	
	public InvalidPostcodeException(String postcode) {
		super("Postcode:"+postcode+" is invalid.");
	}

}
