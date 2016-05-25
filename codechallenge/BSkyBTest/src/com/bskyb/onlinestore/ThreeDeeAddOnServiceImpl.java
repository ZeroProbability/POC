package com.bskyb.onlinestore;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class ThreeDeeAddOnServiceImpl implements ThreeDeeAddOnService {
	private Sky3DAvailabilityChecker skyAvailabilityChecker;

	public ThreeDeeAddOnServiceImpl(
			Sky3DAvailabilityChecker skyAvailabilityChecker) {
		this.skyAvailabilityChecker = skyAvailabilityChecker;
	}

	private Set<ProductCodes3D> getRelevent3DProducts(Basket basket) {
		Set<ProductCodes3D> ret = new HashSet<ProductCodes3D>();

		for (ProductCodes p : basket.getProducts()) {
			ret.addAll(p.corresponding3d());
		}
		return ret;
	}

	@Override
	public Set<ProductCodes3D> checkFor3DAddOnProducts(Basket basket,
			String postCode) throws InvalidPostcodeException {

		if (skyAvailabilityChecker.isAvailableIn(postCode)) {
			return getRelevent3DProducts(basket);
		}
		return Collections.emptySet();

	}

}
