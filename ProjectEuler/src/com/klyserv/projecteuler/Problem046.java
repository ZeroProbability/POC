package com.klyserv.projecteuler;

public class Problem046 {
	final static private int max=100000; 
	
	public static void main(String[] args) {
		PrimeSeive ps=new PrimeSeive(max);
		
		for(int i=9;i<max;i+=2) {
			if(ps.isPrime(i)) continue;
			
			int p=0;
			boolean solutionExists=false;
			while(true) {
				p++;
				int y=p*p*2;
				int x=i-y;
				if(x<0) break;
				if(ps.isPrime(x)) {
				   solutionExists=true;
				   break;
				}
			}
			if(!solutionExists) {
				System.out.println(i);
				break;
			}
		}
	}

}
