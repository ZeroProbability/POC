package com.klyserv.projecteuler;

public class Problem007 {
	
	public static void main(String[] args) {
		PrimeSeive ps=new PrimeSeive(1000000000);
		
		int counter=0;
		while(!ps.isEndOfSearch()) {
			counter++;
			System.out.println(counter+" => "+ps.getNextPrime());
			if(counter>10000) break;
		}
		
	}

}
