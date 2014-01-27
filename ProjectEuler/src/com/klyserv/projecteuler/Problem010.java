package com.klyserv.projecteuler;

public class Problem010 {
	
	public static void main(String[] args) {
		PrimeSeive ps=new PrimeSeive(2*1000*1000);
		
		long sum=0;
		while(!ps.isEndOfSearch()) {
			sum+=ps.getNextPrime();
		}
		System.out.println(sum);
	}

}
