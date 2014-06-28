package com.bskyb.onlinestore;

public interface Sky3DAvailabilityChecker {
	
	public boolean isAvailableIn(String postcode) throws InvalidPostcodeException;

}
