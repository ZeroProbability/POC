package com.klyserv.poc.fibonacci;

public class Fibonacci {
	
	private int prev1=0;
	private int prev2=1;
	
	public int nextNumber() {
		int tempNumber=prev1+prev2;
		prev1=prev2;
		prev2=tempNumber;
		return prev1;
	}

}
