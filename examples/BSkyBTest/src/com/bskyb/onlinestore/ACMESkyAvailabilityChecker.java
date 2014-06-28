package com.bskyb.onlinestore;

import com.acme.serviceavailability.AvailabilityChecker;
import com.acme.serviceavailability.TechnicalFailureException;


public class ACMESkyAvailabilityChecker implements Sky3DAvailabilityChecker {
	private AvailabilityChecker checker=null;
	
	public ACMESkyAvailabilityChecker(AvailabilityChecker availabilityChecker) {
		this.checker=availabilityChecker;
	}

	@Override
	public boolean isAvailableIn(String postcode) throws InvalidPostcodeException {
		if (postcode == null)
			return false;

		String availabilityString = null;
		try {
			availabilityString = checker.isPostCodeIn3DTVServiceArea(postcode);
		} catch (TechnicalFailureException e) {
			// According to specification, TechnicalFailureException implies
			// service unavailable.
			availabilityString = AvailabilityReturnCodes.SERVICE_UNAVAILABLE
					.name();
		}
	
		AvailabilityReturnCodes availability = AvailabilityReturnCodes.valueOf(availabilityString);

		if (availability == AvailabilityReturnCodes.SERVICE_AVAILABLE) {
			return true;
		} else if (availability == AvailabilityReturnCodes.SERVICE_UNAVAILABLE
				|| availability == AvailabilityReturnCodes.SERVICE_PLANNED) {
			return false;
		} else if(availability == AvailabilityReturnCodes.POSTCODE_INVALID) {
			throw new InvalidPostcodeException("Postcode '"+postcode+"' is invalid.");
		}
		// The code should never reach here unless there is a programming error
		assert false:"Internal error, Unhandled return code:"+availability.name();
		// return emptySet if asserts are disabled.
		return false;
	}

}
