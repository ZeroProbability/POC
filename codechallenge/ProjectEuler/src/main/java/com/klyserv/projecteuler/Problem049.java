package com.klyserv.projecteuler;

import static com.klyserv.projecteuler.Helper.digitsIn;

import java.util.Arrays;

public class Problem049 {
	
	public static void main(String[] args) {
		PrimeSeive ps=new PrimeSeive(10000);
		PrimeSeive ps1=new PrimeSeive(10000);
		
		while(!ps.isEndOfSearch()) {
			int p=ps.getNextPrime();
			if(p<1000) continue;
			if(p+6660>10000) break;
			int p1=p+3330;
			int p2=p+6660;
			if(ps1.isPrime(p1) & ps1.isPrime(p2)) {
				//nothing
			} else {
				continue;
			}
			
			Object[] pa=digitsIn(p).toArray(); Arrays.sort(pa);
			Object[] pa1=digitsIn(p1).toArray(); Arrays.sort(pa1);
			Object[] pa2=digitsIn(p2).toArray(); Arrays.sort(pa2);
			
			if(Arrays.deepEquals(pa1, pa2) && Arrays.deepEquals(pa1, pa)) {
				System.out.printf("%d%d%d\n",p,p1,p2);
			}
		}
	}

}
