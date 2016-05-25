package com.klyserv.projecteuler;

public class Problem028 {
	
	public static void main(String[] args) {
		int i=1;
		int max=1001;
		
		int inc=2;
		int sumOfDiag=1;
		while(i<max*max) {
			for(int counter=0;counter<4;counter++) {
				i+=inc;
				sumOfDiag+=i;
			}
			inc+=2;
		}
		System.out.println(sumOfDiag);
		
	}

}
