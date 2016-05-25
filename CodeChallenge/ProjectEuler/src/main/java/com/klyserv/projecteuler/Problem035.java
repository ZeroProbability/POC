package com.klyserv.projecteuler;

public class Problem035 {
	
	public static void main(String[] args) {
		PrimeSeive psgrand=new PrimeSeive(1000*1000*10);
		PrimeSeive ps=new PrimeSeive(1000*1000);
		
		int count=0;
		while(!ps.isEndOfSearch()) {
			int nextPrime=ps.getNextPrime();
			int numSize=Helper.numDigits(nextPrime);

			boolean circularPrime=true;
			int nextPrimeRotated=Helper.rotateNumber(nextPrime,numSize);
			
			inner:do {
				circularPrime=circularPrime&&(psgrand.isPrime(nextPrimeRotated));
				if(!circularPrime) break inner;
			} while(nextPrime!=(nextPrimeRotated=Helper.rotateNumber(nextPrimeRotated,numSize)));
			
			if (circularPrime) {
				System.out.println(nextPrime);
				count++;
			}
			
		}
		
		System.out.println("count="+count);
	}

}
