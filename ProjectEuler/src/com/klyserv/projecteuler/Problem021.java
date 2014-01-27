package com.klyserv.projecteuler;

import java.util.HashSet;
import java.util.Set;

public class Problem021 {
	
	private static long d(long n) {
		int sum=0;
		for(long f:Factors.findFactors(n)) {
			if(f!=n) sum+=f;
		}
		return sum;
	}
	
	public static void main(String[] args) {
		Set<Long> allAmiable=new HashSet<Long>();
		for(long i=2;i<10000;i++) {
			long d=d(i);
			long dd=d(d);
			
			if(dd==i && d!=i) {
				allAmiable.add(i);
				allAmiable.add(d);
			}
		}
		long sum=0;
		for(long i:allAmiable) {
			sum+=i;
		}
		System.out.println(sum);
	}

}
