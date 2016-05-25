package com.klyserv.projecteuler;

import java.math.BigInteger;

public class Problem100 {
	
	private static final BigInteger _1=BigInteger.ONE;
	private static final BigInteger _2=BigInteger.valueOf(2);
	private static final BigInteger _3=BigInteger.valueOf(3);
	private static final BigInteger _4=BigInteger.valueOf(4);
	
	public static void main(String[] args) {
		BigInteger x=_1;
	      BigInteger y=_1;
	      BigInteger ox=_1;
	      BigInteger oy=_1;
	      for (int n=0; n<100; n++) {
	         ox = x;
	         oy = y;
	         x = ox.multiply(_3).add(oy.multiply(_2)).subtract(_2);
	         y = ox.multiply(_4).add(oy.multiply(_3)).subtract(_3);
	         System.out.println("x= " + x + " y="+y);
	         BigInteger sum=x.add(y);
	         
	         if(sum.compareTo(BigInteger.valueOf(1000l*1000l*1000l*1000l))>0) {
	        	 System.out.println("sum="+sum);
	        	 break;
	         }
	      }
	}

}
