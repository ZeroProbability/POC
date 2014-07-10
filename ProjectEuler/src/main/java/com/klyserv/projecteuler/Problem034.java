package com.klyserv.projecteuler;

public class Problem034 {

	public static void main(String[] args) {
		long grandSum=0;
		for(int i=3;i<9999999;i++) {
			long factSum=0;
			int n=i;
			while(n>0) {
				int oneDigit=n%10;
				n=n/10;
				factSum+=Helper.factorial(oneDigit).intValue();
				if(factSum>i) break;
			}
			if(factSum==i) {
				System.out.println(factSum);
				grandSum+=factSum;
			}
		}
		System.out.println(grandSum);
			
	}
}
