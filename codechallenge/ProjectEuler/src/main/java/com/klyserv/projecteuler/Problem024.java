package com.klyserv.projecteuler;

import java.util.Arrays;
import java.util.List;

public class Problem024 {
	
	public static void main(String[] args) {
		final int[] counter=new int[1];
		counter[0]=0;
		Permutation.compute(Arrays.asList(0,1,2,3,4,5,6,7,8,9), new PermutationListener() {
			
			@Override
			public void listen(List<Object> occur) {
				counter[0]++;
				if(counter[0]==1000*1000) {
					System.out.println(occur);
				}
				
			}
		});
	}

}
