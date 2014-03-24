package com.klyserv.projecteuler;

import java.math.BigInteger;

public class Problem048 {
	
	public static void main(String[] args) {
		BigInteger sum=BigInteger.ZERO;
		
		for(int i=1;i<1001;i++)
			sum=sum.add(BigInteger.valueOf(i).pow(i));
		
		sum=sum.mod(BigInteger.valueOf(1000l*1000l*1000l*10l));
		
		System.out.println(sum);
		
	}

}
