package com.klyserv.projecteuler;

import java.math.BigInteger;

public class Problem025 {
	
	public static void main(String[] args) {
		int pos=3;
		BigInteger prevfib1=BigInteger.ONE;
		BigInteger prevfib2=BigInteger.ONE;
		
		while(true){
			BigInteger t=prevfib1.add(prevfib2);
			prevfib1=prevfib2;
			prevfib2=t;
			
			if(t.toString().length()==1000) {
				System.out.println(pos);
				break;
			}
			
			pos++;
		}
		
		
		
	}

}
