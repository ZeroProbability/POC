package com.klyserv.projecteuler;

public class Problem037 {
	
	public static void main(String[] args) {
		PrimeSeive psGrand=new PrimeSeive(1000*1000);
		
		PrimeSeive ps=new PrimeSeive(1000*1000);
		
		int sum=0;
		
		while(!ps.isEndOfSearch()) {
			int nextPrime=ps.getNextPrime();
			if(nextPrime<10) continue;
			
			boolean truncatablePrime=true;
			
			int tempNextPrime=nextPrime;
			while(truncatablePrime && (tempNextPrime=tempNextPrime/10)>0) {
				if(!psGrand.isPrime(tempNextPrime)) 
					truncatablePrime=false;
			}

			tempNextPrime=nextPrime;
			while(truncatablePrime && (tempNextPrime=(int) Helper.chopLeft(tempNextPrime))>0) {
				if(!psGrand.isPrime(tempNextPrime)) 
					truncatablePrime=false;
			}
			
			if(truncatablePrime) {
				sum+=nextPrime;
			}
		}
		System.out.println("sum="+sum);
	}

}
