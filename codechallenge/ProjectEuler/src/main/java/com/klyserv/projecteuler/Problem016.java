package com.klyserv.projecteuler;

import java.math.BigInteger;

public class Problem016 {
	
	public static void main(String[] args) {
		BigInteger prod=BigInteger.ONE;
		
		int count=1000;
		
		for(int i=0;i<count;i++){
			prod=prod.multiply(BigInteger.valueOf(2));
		}
		
		System.out.println(Helper.sumDigits(prod));
	}

}
