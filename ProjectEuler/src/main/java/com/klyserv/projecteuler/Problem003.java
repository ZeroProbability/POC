package com.klyserv.projecteuler;

public class Problem003 {
	
	public static void main(String[] args) {
		long givenNumber=600851475143l;
		int maxToCheck=(int) Math.sqrt(givenNumber);
		PrimeSeive ps=new PrimeSeive(maxToCheck);
		while(!ps.isEndOfSearch()) {
			int nextPrime=ps.getNextPrime();
			if(givenNumber%nextPrime==0) 
				System.out.println(nextPrime);
		}
	}

}
