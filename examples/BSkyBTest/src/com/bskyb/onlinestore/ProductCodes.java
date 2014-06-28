package com.bskyb.onlinestore;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public enum ProductCodes {
		SPORTS {
			@Override
			public Collection<ProductCodes3D> corresponding3d() {
				return Arrays.asList(ProductCodes3D.SPORTS_3D_ADD_ON);
			}
		}, KIDS 
		, VARIETY
		, NEWS {
			@Override
			public Collection<ProductCodes3D> corresponding3d() {
				return Arrays.asList(ProductCodes3D.NEWS_3D_ADD_ON);
			}
		}, MOVIES_1 {
			@Override
			public Collection<ProductCodes3D> corresponding3d() {
				return Arrays.asList(ProductCodes3D.MOVIES_3D_ADD_ON);
			}
		}, MOVIES_2 {
			@Override
			public Collection<ProductCodes3D> corresponding3d() {
				return Arrays.asList(ProductCodes3D.MOVIES_3D_ADD_ON);
			}
		};
		
		public Collection<ProductCodes3D> corresponding3d() {
			return Collections.emptyList();
		}

}
