package com.klyserv.projecteuler;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Factors {
	
	public static List<Long> findFactors(long number) {
		PrimeFactors pf=new PrimeFactors(number);
		Map<Object,Integer> pfList=new HashMap<Object, Integer>();
		for(PrimeFactors.Factor f:pf.getFactorList()) {
			pfList.put(f.getFactor(), f.getTimes());
		}
		final List<Long> factorList=new ArrayList<Long>();
		new Combination(pfList, new CombinationListener() {
			
			@Override
			public void listen(Map<Object, Integer> occur) {
				long factor=1;
				for(Object o:occur.keySet()) {
					for(int i=0;i<occur.get(o);i++){
						factor*=((Integer)o);
					}
				}
				factorList.add(factor);
			}
		});
		return factorList;
	}
	
	public static void main(String[] args) {
		findFactors(100);
	}

}
