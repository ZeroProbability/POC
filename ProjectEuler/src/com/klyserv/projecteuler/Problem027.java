package com.klyserv.projecteuler;

public class Problem027 {
	
	private static long f(long n, long a, long b) {
		return n*n+a*n+b;
	}
	
	public static void main(String[] args) {
		PrimeSeive masterps=new PrimeSeive(1000*1000*100);
		int maxPrimeCount=0;
		for(int a=-999;a<1000;a++) {
			PrimeSeive ps=new PrimeSeive(1000);
			while(!ps.isEndOfSearch()) {
				int b=ps.getNextPrime();
				
				int primeCount=1;
				for(int n=1;n<1000;n++){
					long computedNUmber=f(n,a,b);
					if(!masterps.isPrime((int)computedNUmber)) break;
					primeCount++;
				}
				
				if(primeCount>maxPrimeCount) {
					System.out.println("n*n+("+a+")n+"+b+" produces "+primeCount+" primes. axb="+a*b);
					maxPrimeCount=primeCount;
				}
			}
		}
	}

}
