package com.klyserv.projecteuler;

public class Problem045 {
	
	private final static long max=100000l; 
	
	public static void main(String[] args) {
		
		for(long i=1;i<max;i++) {
			long hex=i*(2*i-1);
			if(Helper.isPentagonal(hex)>0 && Helper.isTriangle(hex)>0) System.out.println(hex);
		}
		
	}

}
