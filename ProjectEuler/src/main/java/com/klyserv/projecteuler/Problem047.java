package com.klyserv.projecteuler;

public class Problem047 {
	
	public static final int max=1000000;
	
	private static int getPrimeFactorCount(int number) {
		PrimeSeive ps=new PrimeSeive(number);
		int primeFactorCount=0;
		while(!ps.isEndOfSearch()) {
			int primeFactor=ps.getNextPrime();
			if(number%primeFactor==0) {
				primeFactorCount++;
				do {
					number=number/primeFactor;
				} while(number%primeFactor==0);
			}
		}
		return primeFactorCount;
	}
	
	public static void main(String[] args) {
		
		for(int i=10;i<max;i++){
			if (getPrimeFactorCount(i) == 4 && getPrimeFactorCount(i + 1) == 4
					&& getPrimeFactorCount(i + 2) == 4
					&& getPrimeFactorCount(i + 3) == 4) {
				System.out.println(i + "," + (i + 1) + "," + (i + 2) + ","
						+ (i + 3));
			}
		}
		
	}

}
