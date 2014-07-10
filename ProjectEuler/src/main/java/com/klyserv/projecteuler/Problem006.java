package com.klyserv.projecteuler;

public class Problem006 {
	
	public static void main(String[] args) {
		long sum1=0;
		long sum2=0;
		for (int i = 1; i < 101; i++) {
			sum1+=(i);
			sum2+=(i*i);
		}
		System.out.println(sum1*sum1-sum2);
	}

}
