package com.bskyb.onlinestore;

import java.util.Set;

public interface ThreeDeeAddOnService {
	public Set<ProductCodes3D> checkFor3DAddOnProducts(Basket basket,
			String postCode) throws InvalidPostcodeException;
}