package com.bskyb.onlinestore;

import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class Basket {
	
	private Set<ProductCodes> products;
	
	public Basket(String... productStrings) {
		products=new HashSet<ProductCodes>();
		
		for(String s:productStrings) {
			products.add(ProductCodes.valueOf(s));
		}
	}

	public Collection<ProductCodes> getProducts() {
		return Collections.unmodifiableCollection(products);
	}

}
